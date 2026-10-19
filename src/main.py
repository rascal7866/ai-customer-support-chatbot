import argparse
import json
from pathlib import Path
from .chatbot import load_faq, answer


def main():
    parser = argparse.ArgumentParser(description='ChatCactus-inspired customer support demo')
    parser.add_argument('--question', required=True)
    parser.add_argument('--faq', default=str(Path(__file__).resolve().parent.parent / 'examples' / 'faq.json'))
    parser.add_argument('--ai', action='store_true', help='Use optional OpenAI fallback')
    args = parser.parse_args()
    print(json.dumps(answer(args.question, load_faq(args.faq), args.ai), indent=2))


if __name__ == '__main__':
    main()
