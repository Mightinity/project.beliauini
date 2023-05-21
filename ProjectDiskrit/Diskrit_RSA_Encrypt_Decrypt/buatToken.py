import random
import json
import string

def generate_token():
    token = f"{generate_segment()}-{generate_segment()}-{generate_segment()}-{generate_segment()}"
    return token

def generate_segment():
    segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return segment

with open('tokens.json', 'r') as f:
    tokens = json.load(f)

while True:
    new_token = generate_token()
    if new_token not in tokens.keys():
        tokens[new_token] = None
        with open('tokens.json', 'w') as f:
            json.dump(tokens, f, indent=4)
        break

print("Token berhasil dibuat: " + new_token)