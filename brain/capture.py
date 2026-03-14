from pathlib import Path
import datetime

INBOX = "knowledge/inbox"


def capture(text):

    filename = f"{datetime.datetime.now().timestamp()}.txt"

    path = Path(INBOX) / filename

    with open(path, "w") as f:
        f.write(text)

    print("Saved to:", path)