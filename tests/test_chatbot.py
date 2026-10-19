
import os
import unittest
from unittest.mock import patch

from src.chatbot import answer, tokenize, load_faq


FAQ = [
    {
        "question": "How do I track my order?",
        "keywords": ["tracking", "shipping"],
        "answer": "Use your tracking link."
    },
    {
        "question": "What is your return policy?",
        "keywords": ["refund", "return"],
        "answer": "Contact support for returns."
    }
]


class ChatbotTests(unittest.TestCase):

    def test_known_question(self):
        result = answer("How do I track my order?", FAQ)

        self.assertFalse(result["escalate"])
        self.assertEqual(
            result["answer"],
            "Use your tracking link."
        )

    def test_unknown_question(self):
        result = answer("purple elephant", FAQ)

        self.assertTrue(result["escalate"])
        self.assertIsNone(result["source"])

    def test_refund_question(self):
        result = answer("What is your refund policy?", FAQ)

        self.assertFalse(result["escalate"])
        self.assertEqual(
            result["answer"],
            "Contact support for returns."
        )

    def test_empty_question(self):
        result = answer("", FAQ)

        self.assertFalse(result["escalate"])
        self.assertIn("Please enter", result["answer"])

    def test_empty_knowledge_base(self):
        result = answer("Where is my order?", [])

        self.assertTrue(result["escalate"])

    def test_stop_words(self):
        result = tokenize("What is your return policy?")

        self.assertNotIn("what", result)
        self.assertNotIn("your", result)
        self.assertIn("return", result)
        self.assertIn("policy", result)

    def test_missing_api_key(self):
        with patch.dict(os.environ, {}, clear=True):
            result = answer(
                "purple elephant",
                FAQ,
                use_ai=True
            )

        self.assertTrue(result["escalate"])
        self.assertIn("not configured", result["answer"])

    def test_load_faq(self):
        import json
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "faq.json"
            path.write_text(
                json.dumps(FAQ),
                encoding="utf-8"
            )

            result = load_faq(path)

        self.assertEqual(result, FAQ)


if __name__ == "__main__":
    unittest.main()
