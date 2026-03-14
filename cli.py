import argparse
from brain.ingest_url import ingest_url
from brain.insights import generate_insights

from brain.capture import capture
from brain.process_inbox import process_inbox
from brain.rag import ask
from brain.chat import interactive_chat
from brain.doctor import run_doctor
from brain.timeline import generate_timeline
from brain.zettelkasten import generate_zettels
from brain.weave import weave_notes



def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("command")
    parser.add_argument("text", nargs="?")

    args = parser.parse_args()

    if args.command == "capture":
        capture(args.text)

    elif args.command == "process":
        process_inbox()

    elif args.command == "ask":
        answer = ask(args.text)
        print(answer)
    elif args.command == "ingest-url":
        ingest_url(args.text)
    elif args.command == "insights":
        generate_insights()
    elif args.command == "chat":
        interactive_chat()
    elif args.command == "doctor":
        run_doctor()
    elif args.command == "timeline":
        generate_timeline()
    elif args.command == "zettel":
        generate_zettels()
    elif args.command == "weave":
        weave_notes()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()