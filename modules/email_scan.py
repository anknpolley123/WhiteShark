import re

def find_emails(file):
    with open(file, "r") as f:
        data = f.read()

    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", data)
    return set(emails)
