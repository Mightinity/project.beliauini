import random
import json
import string
import re

def generate_token():
    token = f"{generate_segment()}-{generate_segment()}-{generate_segment()}-{generate_segment()}"
    return token

def generate_segment():
    segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return segment


def menu():
    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    print("Pilih tipe token generate")
    print("1. Custom Token")
    print("2. Random Token")
    pilihan = int(input("Masukkan pilihan: "))
    if (pilihan == 1):
        encrypt_perm = input("Permission for encrypt? (y/N): ")
        decrypt_perm = input("Permission for decrypt? (y/N): ")
        new_token = input("Input custom token (Format: AAAA-BBBB-CCCC-DDDD): ")
        pattern = re.compile(r'^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$')
        if not pattern.match(new_token):
            print("Invalid format token. (Format: AAAA-BBBB-CCCC-DDDD)")
        else:
            tokens[new_token] = {
                    "ENCRYPT": "True" if encrypt_perm.lower() == "y" else "False",
                    "DECRYPT": "True" if decrypt_perm.lower() == "y" else "False",
                    "IP": None,
                    "NAME": None
                }
            with open('tokens.json', 'w') as f:
                json.dump(tokens, f, indent=4)
            print(f"Token berhasil dibuat: {new_token}")
    elif(pilihan == 2):
        new_token = generate_token()
        if new_token not in tokens.keys():
            encrypt_perm = input("Permission for encrypt? (y/N): ")
            decrypt_perm = input("Permission for decrypt? (y/N): ")
            tokens[new_token] = {
                "ENCRYPT": "True" if encrypt_perm.lower() == "y" else "False",
                "DECRYPT": "True" if decrypt_perm.lower() == "y" else "False",
                "IP": None,
                "NAME": None
            }
            with open('tokens.json', 'w') as f:
                json.dump(tokens, f, indent=4)
            print(f"Token berhasil dibuat: {new_token}")
    else:
        print("Error: Pilih antara 1/2\n")
        menu()

if __name__ == "__main__":
    menu()