import socket
import threading
import json
import signal
import sys

print("\nMenjalankan socket server (RSA DECRYPT)")

def signal_handler(sig, frame):
    print('\nMenerima sinyal SIGINT, menutup socket server...')
    server_socket.close()
    sys.exit(0)

# SOCKET SERVER
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 10098))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1000)

signal.signal(signal.SIGINT, signal_handler)                                                                     

def modeDecrypt(client_socket, client_address):
    logo(client_socket, client_address)
    client_socket.sendall(b"Masukkan nilai yang mau didekripsi : ")
    base = int(client_socket.recv(1024).decode().strip())
    power = 1019
    modulus = 3337 

    powerNow = 1
    current_value = pow(base, powerNow, modulus)
    client_socket.sendall(f"{base} mod {modulus} = {current_value}\n\n".encode())
    powerPrev2 = powerNow
    powerNow += 1
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base} mod {modulus}] . [{base} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = [{current_value}] . [{current_value}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = {current_value * current_value} mod {modulus}\n".encode())
    current_value2 = (current_value * current_value) % modulus
    client_socket.sendall(f"               = {current_value2}\n\n".encode())
    powerPrev3 = powerNow
    powerNow += 1
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base} mod {modulus}] . [{base}^{powerPrev3} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = [{current_value}] . [{current_value2}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = {current_value * current_value2} mod {modulus}\n".encode())
    current_value3 = (current_value * current_value2) % modulus
    client_socket.sendall(f"               = {current_value3}\n\n".encode())
    powerPrev4 = powerNow
    powerNow += 1
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev3} mod {modulus}] . [{base}^{powerPrev3} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = [{current_value2}] . [{current_value2}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = {current_value2 * current_value2} mod {modulus}\n".encode())
    current_value4 = (current_value2 * current_value2) % modulus
    client_socket.sendall(f"               = {current_value4}\n\n".encode())
    powerPrev8 = powerNow
    powerNow += 4
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev8} mod {modulus}] . [{base}^{powerPrev8} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = [{current_value4}] . [{current_value4}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = {current_value4 * current_value4} mod {modulus}\n".encode())
    current_value8 = (current_value4 * current_value4) % modulus
    client_socket.sendall(f"               = {current_value8}\n\n".encode())
    powerPrev16 = powerNow
    powerNow += 8
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev16} mod {modulus}] . [{base}^{powerPrev16} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = [{current_value8}] . [{current_value8}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = {current_value8 * current_value8} mod {modulus}\n".encode())
    current_value16 = (current_value8 * current_value8) % modulus
    client_socket.sendall(f"               = {current_value16}\n\n".encode())
    powerPrev32 = powerNow
    powerNow += 16
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev32} mod {modulus}] . [{base}^{powerPrev32} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                = [{current_value16}] . [{current_value16}] mod {modulus}\n".encode())
    client_socket.sendall(f"                = {current_value16 * current_value16} mod {modulus}\n".encode())
    current_value32 = (current_value16 * current_value16) % modulus
    client_socket.sendall(f"                = {current_value32}\n\n".encode())
    powerPrev64 = powerNow
    powerNow += 32
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev64} mod {modulus}] . [{base}^{powerPrev64} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                = [{current_value32}] . [{current_value32}] mod {modulus}\n".encode())
    client_socket.sendall(f"                = {current_value32 * current_value32} mod {modulus}\n".encode())
    current_value64 = (current_value32 * current_value32) % modulus
    client_socket.sendall(f"                = {current_value64}\n\n".encode())
    powerPrev128 = powerNow
    powerNow += 64
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev128} mod {modulus}] . [{base}^{powerPrev128} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value64}] . [{current_value64}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value64 * current_value64} mod {modulus}\n".encode())
    current_value128 = (current_value64 * current_value64) % modulus
    client_socket.sendall(f"                 = {current_value128}\n\n".encode())
    powerPrev256 = powerNow
    powerNow += 128
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev256} mod {modulus}] . [{base}^{powerPrev256} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value128}] . [{current_value128}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value128 * current_value128} mod {modulus}\n".encode())
    current_value256 = (current_value128 * current_value128) % modulus
    client_socket.sendall(f"                 = {current_value256}\n\n".encode())
    powerPrev512 = powerNow
    powerNow += 256
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev512} mod {modulus}] . [{base}^{powerPrev512} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value256}] . [{current_value256}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value256 * current_value256} mod {modulus}\n".encode())
    current_value512 = (current_value256 * current_value256) % modulus
    client_socket.sendall(f"                 = {current_value512}\n\n".encode())
    powerPrev768 = powerNow
    powerNow += 256
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev512} mod {modulus}] . [{base}^{powerPrev768} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value256}] . [{current_value512}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value256 * current_value512} mod {modulus}\n".encode())
    current_value768 = (current_value256 * current_value512) % modulus
    client_socket.sendall(f"                 = {current_value768}\n\n".encode())
    powerPrev896 = powerNow
    powerNow += 128
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev256} mod {modulus}] . [{base}^{powerPrev896} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value128}] . [{current_value768}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value128 * current_value768} mod {modulus}\n".encode())
    current_value896 = (current_value128 * current_value768) % modulus
    client_socket.sendall(f"                 = {current_value896}\n\n".encode())
    powerPrev960 = powerNow
    powerNow += 64
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev128} mod {modulus}] . [{base}^{powerPrev960} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value64}] . [{current_value896}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value64 * current_value896} mod {modulus}\n".encode())
    current_value960 = (current_value64 * current_value896) % modulus
    client_socket.sendall(f"                 = {current_value960}\n\n".encode())
    powerPrev992 = powerNow
    powerNow += 32
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev64} mod {modulus}] . [{base}^{powerPrev992} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value32}] . [{current_value960}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value32 * current_value960} mod {modulus}\n".encode())
    current_value992 = (current_value32 * current_value960) % modulus
    client_socket.sendall(f"                 = {current_value992}\n\n".encode())
    powerPrev1008 = powerNow
    powerNow += 16
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev32} mod {modulus}] . [{base}^{powerPrev1008} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value16}] . [{current_value992}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value16 * current_value992} mod {modulus}\n".encode())
    current_value1008 = (current_value16 * current_value992) % modulus
    client_socket.sendall(f"                 = {current_value1008}\n\n".encode())
    powerPrev1016 = powerNow
    powerNow += 8
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev16} mod {modulus}] . [{base}^{powerPrev1016} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value8}] . [{current_value1008}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value8 * current_value1008} mod {modulus}\n".encode())
    current_value1016 = (current_value8 * current_value1008) % modulus
    client_socket.sendall(f"                 = {current_value1016}\n\n".encode())
    powerPrev1019 = powerNow
    powerNow += 3
    client_socket.sendall(f"{base}^{powerNow} mod {modulus} = [{base}^{powerPrev4} mod {modulus}] . [{base}^{powerPrev1019} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = [{current_value3}] . [{current_value1016}] mod {modulus}\n".encode())
    client_socket.sendall(f"                 = {current_value3 * current_value1016} mod {modulus}\n".encode())
    current_value1019 = (current_value3 * current_value1016) % modulus
    client_socket.sendall(f"                 = {current_value1019}\n\n".encode())
    client_socket.sendall(f"Hasil {base}^{power} mod {modulus} adalah {pow(base, power, modulus)}\n\n".encode())
    modeDecrypt(client_socket, client_address)
    

def logo(client_socket, client_address):
    client_socket.sendall("    ____  _____ ___       ____                             __ \n".encode())
    client_socket.sendall("   / __ \/ ___//   |     / __ \___  ____________  ______  / /_\n".encode())
    client_socket.sendall("  / /_/ /\__ \/ /| |    / / / / _ \/ ___/ ___/ / / / __ \/ __/\n".encode())
    client_socket.sendall(" / _, _/___/ / ___ |   / /_/ /  __/ /__/ /  / /_/ / /_/ / /_  \n".encode())
    client_socket.sendall("/_/ |_|/____/_/  |_|  /_____/\___/\___/_/   \__, / .___/\__/  \n".encode())
    client_socket.sendall("                                           /____/_/           \n".encode())
    client_socket.sendall(b"                RSA (Rumus Sofyan Arifianto)\n\n")


def contact(client_socket, client_address):
    client_socket.sendall(b'Contact Person:\n')
    client_socket.sendall(b'WA: 0822 2853 7028\n')
    client_socket.sendall(b'WA: 0821 7023 9463\n')

def handle_client(client_socket, client_address):
    print(f'Klien connect dengan IP: {client_address[0]}:{client_address[1]}')
    # client_ip = client_address[0]
    client_socket.sendall(b"\n")
    client_socket.sendall(b"RSA Decrypt Program (v1.0)\n")
    client_socket.sendall(b'Masukkan Token: ')
    token = client_socket.recv(1024).decode().strip()

    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    if token in tokens:
        if tokens[token]:
            if tokens[token] == client_address[0]:
                client_socket.sendall(b'Token valid!\n\n')
                modeDecrypt(client_socket, client_address)
            else:
                client_socket.sendall(b'Mohon maaf, token sudah terkoneksi dengan IP yang berbeda\n\n')
                client_socket.sendall(b'Apakah ada kesalahan? hubungi admin.\n')
                contact(client_socket, client_address)
        else:
            tokens[token] = client_address[0]
            with open('tokens.json', 'w') as f:
                json.dump(tokens, f)
            client_socket.sendall(b'Token valid!\n\n')
            modeDecrypt(client_socket, client_address)
    else:
        client_socket.sendall(b'\nMohon maaf, token belum terdaftar\n\n')
        client_socket.sendall(b'Ingin mendaftar?\n')
        contact(client_socket, client_address)
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    t = threading.Thread(target=handle_client, args=(client_socket, client_address))
    t.start()