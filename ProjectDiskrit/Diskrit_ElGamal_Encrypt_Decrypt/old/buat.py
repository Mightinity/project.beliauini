import random
import json
import requests
import string

# ganti <YOUR_SECRET_KEY> dengan API Secret Key dari JSONBin
url = "https://api.jsonbin.io/v3/b/64220056c0e7653a059779ce"

headers = {
    "Content-Type": "application/json",
    "X-Master-Key": "$2b$10$q8I27tTa0dak4w.o5HppW.QgTkQPd1.vv0GqIKeqxad.yuTN9HGOu"
}

# ambil data dari JSONBin
response = requests.get(url, headers=headers)
tokens = response.json()

def generate_token():
    token = f"{generate_segment()}-{generate_segment()}-{generate_segment()}-{generate_segment()}"
    return token

def generate_segment():
    segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return segment

while True:
    new_token = generate_token()
    if new_token not in tokens.keys():
        tokens[new_token] = None
        # update data di JSONBin
        response = requests.put(url, json=tokens, headers=headers)
        print("Token berhasil dibuat: " + new_token)
        break
