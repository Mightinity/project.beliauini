import socket
import threading
import json
import signal
import sys

print("\nMenjalankan socket server (RSA ENCRYPT)")

def signal_handler(sig, frame):
    print('\nMenerima sinyal SIGINT, menutup socket server...')
    server_socket.close()
    sys.exit(0)

# SOCKET SERVER
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 10100))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1000)

signal.signal(signal.SIGINT, signal_handler)                                                                     

def modeEncrypt(client_socket, client_address):
    logo(client_socket, client_address)
    client_socket.sendall(b"Masukkan nilai yang mau dienkripsi : ")
    base = int(client_socket.recv(1024).decode().strip())
    power = 79
    modulus = 3337 

    powerNow = 1
    current_value = pow(base, powerNow, modulus)
    client_socket.sendall(f"{base} mod {modulus} = {current_value}\n\n".encode())

    powerPrev2 = powerNow
    powerNow += 1
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base} mod {modulus}] . [{base} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value}] . [{current_value}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value * current_value} mod {modulus}\n".encode())
    current_value2 = (current_value * current_value) % modulus
    client_socket.sendall(f"             = {current_value2}\n\n".encode())

    powerPrev3 = powerNow
    powerNow += 1
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev2} mod {modulus}] . [{base}^{powerPrev3} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value}] . [{current_value2}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value * current_value2} mod {modulus}\n".encode())
    current_value3 = (current_value * current_value2) % modulus
    client_socket.sendall(f"             = {current_value3}\n\n".encode())

    powerPrev4 = powerNow
    powerNow += 1
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev3} mod {modulus}] . [{base}^{powerPrev3} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value2}] . [{current_value2}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value2 * current_value2} mod {modulus}\n".encode())
    current_value4 = (current_value2 * current_value2) % modulus
    client_socket.sendall(f"             = {current_value4}\n\n".encode())

    powerPrev7 = powerNow
    powerNow += 3
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev4} mod {modulus}] . [{base}^{powerPrev7} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value3}] . [{current_value4}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value3 * current_value4} mod {modulus}\n".encode())
    current_value7 = (current_value3 * current_value4) % modulus
    client_socket.sendall(f"             = {current_value7}\n\n".encode())

    powerPrev8 = powerNow
    powerNow += 1
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev7 } mod {modulus}] . [{base}^{powerPrev7} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value4}] . [{current_value4}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value4 * current_value4} mod {modulus}\n".encode())
    current_value8 = (current_value4 * current_value4) % modulus
    client_socket.sendall(f"             = {current_value8}\n\n".encode())

    powerPrev15 = powerNow
    powerNow += 7
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev8} mod {modulus}] . [{base}^{powerPrev15} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value7}] . [{current_value8}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value7 * current_value8} mod {modulus}\n".encode())
    current_value15 = (current_value7 * current_value8) % modulus
    client_socket.sendall(f"             = {current_value15}\n\n".encode())

    powerPrev16 = powerNow
    powerNow += 1
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev15} mod {modulus}] . [{base}^{powerPrev15} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value8}] . [{current_value8}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value8 * current_value8} mod {modulus}\n".encode())
    current_value16 = (current_value8 * current_value8) % modulus
    client_socket.sendall(f"             = {current_value16}\n\n".encode())

    powerPrev32 = powerNow
    powerNow += 16
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev32} mod {modulus}] . [{base}^{powerPrev32} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value16}] . [{current_value16}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value16 * current_value16} mod {modulus}\n".encode())
    current_value32 = (current_value16 * current_value16) % modulus
    client_socket.sendall(f"             = {current_value32}\n\n".encode())

    powerPrev64 = powerNow
    powerNow += 32
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev64} mod {modulus}] . [{base}^{powerPrev64} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value32}] . [{current_value32}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value32 * current_value32} mod {modulus}\n".encode())
    current_value64 = (current_value32 * current_value32) % modulus
    client_socket.sendall(f"             = {current_value64}\n\n".encode())

    powerPrev79 = powerNow
    powerNow += 15
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev16} mod {modulus}] . [{base}^{powerPrev79} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = [{current_value15}] . [{current_value64}] mod {modulus}\n".encode())
    client_socket.sendall(f"             = {current_value15 * current_value64} mod {modulus}\n".encode())
    current_value79 = (current_value15 * current_value64) % modulus
    client_socket.sendall(f"             = {current_value79}\n\n".encode())
    client_socket.sendall(f"Hasil {base}^{power} mod {modulus} adalah {pow(base, power, modulus)}\n".encode())
    modeEncrypt(client_socket, client_address)
    
def logo(client_socket, client_address):
    client_socket.sendall("    ____  _____ ___       ______                            __ \n".encode())
    client_socket.sendall("   / __ \/ ___//   |     / ____/___  ____________  ______  / /_\n".encode())
    client_socket.sendall("  / /_/ /\__ \/ /| |    / __/ / __ \/ ___/ ___/ / / / __ \/ __/\n".encode())
    client_socket.sendall(" / _, _/___/ / ___ |   / /___/ / / / /__/ /  / /_/ / /_/ / /_  \n".encode())
    client_socket.sendall("/_/ |_|/____/_/  |_|  /_____/_/ /_/\___/_/   \__, / .___/\__/  \n".encode())
    client_socket.sendall("                                            /____/_/           \n".encode())
    client_socket.sendall(b"                RSA (Rumus Sofyan Arifianto)\n\n")


def contact(client_socket, client_address):
    client_socket.sendall(b'Contact Person:\n')
    client_socket.sendall(b'WA: 0822 2853 7028\n')
    client_socket.sendall(b'WA: 0821 7023 9463\n')

def handle_client(client_socket, client_address):
    print(f'Klien connect dengan IP: {client_address[0]}:{client_address[1]}')
    # client_ip = client_address[0]
    client_socket.sendall(b"\n")
    client_socket.sendall(b"RSA Encrypt Program (v1.0)\n")
    client_socket.sendall(b'Masukkan Token: ')
    token = client_socket.recv(1024).decode().strip()

    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    if token in tokens:
        if tokens[token]:
            if tokens[token] == client_address[0]:
                client_socket.sendall(b'Token valid!\n\n')
                modeEncrypt(client_socket, client_address)
            else:
                client_socket.sendall(b'Mohon maaf, token sudah terkoneksi dengan IP yang berbeda\n\n')
                client_socket.sendall(b'Apakah ada kesalahan? hubungi admin.\n')
                contact(client_socket, client_address)
        else:
            tokens[token] = client_address[0]
            with open('tokens.json', 'w') as f:
                json.dump(tokens, f)
            client_socket.sendall(b'Token valid!\n\n')
            modeEncrypt(client_socket, client_address)
    else:
        client_socket.sendall(b'\nMohon maaf, token tidak valid\n\n')
        client_socket.sendall(b'Ingin mendaftar?\n')
        contact(client_socket, client_address)
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    t = threading.Thread(target=handle_client, args=(client_socket, client_address))
    t.start()