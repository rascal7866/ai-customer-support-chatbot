import unittest
from src.chatbot import answer

FAQ = [{'question': 'How do I track my order?', 'keywords': ['tracking', 'shipping'], 'answer': 'Use your tracking link.'}]

class ChatbotTests(unittest.TestCase):
    def test_known_question(self):
        result = answer('How do I track my order?', FAQ)
        self.assertFalse(result['escalate'])
        self.assertEqual(result['answer'], 'Use your tracking link.')

    def test_unknown_question(self):
        self.assertTrue(answer('purple elephant', FAQ)['escalate'])

if __name__ == '__main__':
    unittest.main()
