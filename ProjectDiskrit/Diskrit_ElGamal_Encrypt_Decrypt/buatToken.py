import os, requests, random, json, string, re

filename = "tokens"
webhook_url = "https://discord.com/api/webhooks/1092413015565029487/KEgHQxaVj-HAFBJgq33RIRDkKPTkYdof2EjfWjVuWH2Lp6_X2L2v_6kN2mrArFkggR1T"

def generate_token():
    token = f"{generate_segment()}-{generate_segment()}-{generate_segment()}-{generate_segment()}"
    return token

def generate_segment():
    segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return segment


def send_discord_message(message):
    data = {
        "content": message
    }
    requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

def menu():
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
            token_data = {
                new_token: {
                    "ENCRYPT": "True" if encrypt_perm.lower() == "y" else "False",
                    "DECRYPT": "True" if decrypt_perm.lower() == "y" else "False",
                    "IP": None,
                    "NAME": None              
                }
            }
            with open(os.path.join(filename, f'{new_token}.json'), 'w') as f:
                json.dump(token_data, f, indent=2)
            encryptdc = "True" if encrypt_perm.lower() == "y" else "False"
            decryptdc = "True" if decrypt_perm.lower() == "y" else "False"
            print(f"Token berhasil dibuat: {new_token}:")
            send_discord_message(f"```{new_token}:\nEncrypt: {encryptdc}\nDecrypt: {decryptdc}\nIP: terpakai```")
    elif(pilihan == 2):
        new_token = generate_token()
        encrypt_perm = input("Permission for encrypt? (y/N): ")
        decrypt_perm = input("Permission for decrypt? (y/N): ")
        token_data = {
            new_token: {
                "ENCRYPT": "True" if encrypt_perm.lower() == "y" else "False",
                "DECRYPT": "True" if decrypt_perm.lower() == "y" else "False",
                "IP": None,
                "NAME": None              
            }
        }
        with open(os.path.join(filename, f'{new_token}.json'), 'w') as f:
            json.dump(token_data, f, indent=2)
        print(f"Token berhasil dibuat: {new_token}")
        encryptdc = "True" if encrypt_perm.lower() == "y" else "False"
        decryptdc = "True" if decrypt_perm.lower() == "y" else "False"
        send_discord_message(f"```{new_token}:\nEncrypt: {encryptdc}\nDecrypt: {decryptdc}\nIP: terpakai```")
    else:
        print("Error: Pilih antara 1/2\n")
        menu()

if __name__ == "__main__":
    menu()
