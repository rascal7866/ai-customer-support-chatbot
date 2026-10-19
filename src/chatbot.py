import json
import os
import re
from pathlib import Path


def load_faq(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def answer(question, faq, use_ai=False):
    words = set(re.findall(r'[a-z0-9]+', question.lower()))
    scored = []
    for item in faq:
        terms = set(re.findall(r'[a-z0-9]+', (item['question'] + ' ' + ' '.join(item.get('keywords', []))).lower()))
        scored.append((len(words & terms), item))
    score, match = max(scored, key=lambda x: x[0], default=(0, None))
    if score >= 2:
        return {'answer': match['answer'], 'source': match['question'], 'escalate': False}
    if use_ai:
        from urllib.request import Request, urlopen
        key = os.environ.get('OPENAI_API_KEY')
        if not key:
            raise ValueError('OPENAI_API_KEY is required for AI mode')
        context = '\n'.join(f"Q: {x['question']}\nA: {x['answer']}" for x in faq)
        payload = json.dumps({'model': os.getenv('OPENAI_MODEL', 'gpt-4.1-mini'), 'messages': [{'role': 'system', 'content': 'Answer using only this FAQ. If not covered, say you cannot answer and recommend human support.\n' + context}, {'role': 'user', 'content': question}], 'temperature': 0}).encode()
        request = Request('https://api.openai.com/v1/chat/completions', data=payload, headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
        with urlopen(request, timeout=30) as response:
            data = json.load(response)
        return {'answer': data['choices'][0]['message']['content'], 'source': 'AI response grounded in FAQ', 'escalate': False}
    return {'answer': 'I could not find an answer in the knowledge base. Please contact a human support agent.', 'source': None, 'escalate': True}
