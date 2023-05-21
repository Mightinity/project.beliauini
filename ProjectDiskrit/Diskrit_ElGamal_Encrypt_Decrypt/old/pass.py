import bcrypt
import json

# buat dictionary password
passwords = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# enkripsi password dan simpan dalam dictionary
for user, password in passwords.items():
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    passwords[user] = hashed_password.decode()

# simpan dictionary dalam file JSON
with open('data.json', 'w') as f:
    json.dump(passwords, f, indent=4)
