
import json
import os
import re
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


STOP_WORDS = {
    "a", "an", "and", "are", "can", "do", "for", "how",
    "i", "in", "is", "me", "my", "of", "on", "the",
    "to", "what", "where", "who", "you", "your"
}

FALLBACK_MESSAGE = (
    "I could not find a reliable answer in the knowledge base. "
    "Please contact a human support agent."
)


def load_faq(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))

    if not isinstance(data, list):
        raise ValueError("FAQ knowledge base must be a JSON list.")

    for item in data:
        if not isinstance(item, dict) or not all(
            isinstance(item.get(field), str)
            for field in ("question", "answer")
        ):
            raise ValueError("Each FAQ needs a question and answer.")

        if not isinstance(item.get("keywords", []), list):
            raise ValueError("FAQ keywords must be a list.")

    return data


def tokenize(text):
    return {
        word
        for word in re.findall(r"[a-z0-9]+", text.lower())
        if word not in STOP_WORDS
    }


def answer(question, faq, use_ai=False):
    if not isinstance(question, str) or not question.strip():
        return {
            "answer": "Please enter a customer support question.",
            "source": None,
            "escalate": False
        }

    words = tokenize(question)
    scored = []

    for item in faq:
        terms = tokenize(
            item["question"] + " " +
            " ".join(item.get("keywords", []))
        )
        score = len(words & terms)
        scored.append((score, item))

    score, match = max(
        scored,
        key=lambda result: result[0],
        default=(0, None)
    )

    if score >= 2:
        return {
            "answer": match["answer"],
            "source": match["question"],
            "escalate": False
        }

    if not use_ai:
        return {
            "answer": FALLBACK_MESSAGE,
            "source": None,
            "escalate": True
        }

    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        return {
            "answer": (
                "AI support is not configured. "
                "Please contact a human support agent."
            ),
            "source": None,
            "escalate": True
        }

    context = "\n".join(
        f"Q: {item['question']}\nA: {item['answer']}"
        for item in faq
    )

    payload = json.dumps({
        "model": os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a customer support assistant. "
                    "Use only the FAQ information provided below. "
                    "Do not invent policies or business information. "
                    "If the FAQ does not answer the question, "
                    "respond with exactly: ESCALATE_TO_HUMAN\n\n"
                    + context
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 0
    }).encode("utf-8")

    request = Request(
        "https://api.openai.com/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urlopen(request, timeout=30) as response:
            data = json.load(response)

        ai_answer = data["choices"][0]["message"]["content"]

        if not isinstance(ai_answer, str) or not ai_answer.strip():
            raise ValueError("Empty AI response")

        if "ESCALATE_TO_HUMAN" in ai_answer:
            return {
                "answer": FALLBACK_MESSAGE,
                "source": None,
                "escalate": True
            }

        return {
            "answer": ai_answer,
            "source": "AI response based on FAQ",
            "escalate": False
        }

    except (HTTPError, URLError, TimeoutError, ValueError, KeyError,
            IndexError, TypeError):
        return {
            "answer": (
                "AI support is temporarily unavailable. "
                "Please contact a human support agent."
            ),
            "source": None,
            "escalate": True
        }
