import re

def find_phones(file):
    with open(file, "r") as f:
        data = f.read()

    phones = re.findall(r"\+?\d{10,13}", data)
    return set(phones)
