import re

email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
hash_regex = r"\b[a-fA-F0-9]{32,64}\b"

def process_data(lines):
    results = []

    for line in lines:
        email = re.findall(email_regex, line)
        hash_val = re.findall(hash_regex, line)

        username = None
        parts = line.split(":")

        if len(parts) > 1:
            username = parts[0]

        results.append({
            "email": email[0] if email else None,
            "username": username,
            "password_hash": hash_val[0] if hash_val else None
        })

    # Remove duplicates
    unique = [dict(t) for t in {tuple(d.items()) for d in results}]
    return unique