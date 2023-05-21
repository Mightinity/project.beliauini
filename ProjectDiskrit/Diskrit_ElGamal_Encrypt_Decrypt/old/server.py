import socket
import threading
import json
import signal
import sys

print("\nMenjalankan socket server (ELGAMAL ENCRYPT)")

def signal_handler(sig, frame):
    print('\nMenerima sinyal SIGINT, menutup socket server...')
    server_socket.close()
    sys.exit(0)

# SOCKET SERVER
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 10078))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1000)

signal.signal(signal.SIGINT, signal_handler)                                                                     

def contact(client_socket, client_address):
    client_socket.sendall(b'Contact Person:\n')
    client_socket.sendall(b'WA: 0822 2853 7028\n')
    client_socket.sendall(b'WA: 0821 7023 9463\n')

def handle_client(client_socket, client_address):
    print(f'Klien connect dengan IP: {client_address[0]}:{client_address[1]}')
    # client_ip = client_address[0]
    client_socket.sendall(b"\n")
    client_socket.sendall(b"ElGamal Encrypt Program (v1.0)\n")
    client_socket.sendall(b'Masukkan Token: ')
    token = client_socket.recv(1024).decode().strip()

    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    if token in tokens:
        if tokens[token]:
            if tokens[token] == client_address[0]:
                client_socket.sendall(b'Token valid!\n\n')
                #modeEncrypt(client_socket, client_address)
            else:
                client_socket.sendall(b'Mohon maaf, token sudah terdaftar dengan IP yang berbeda\n\n')
                client_socket.sendall(b'Apakah ada kesalahan? hubungi admin.\n')
                contact(client_socket, client_address)
        else:
            tokens[token] = client_address[0]
            with open('tokens.json', 'w') as f:
                json.dump(tokens, f)
            client_socket.sendall(b'Token valid!\n\n')
            #modeEncrypt(client_socket, client_address)
    else:
        client_socket.sendall(b'\nMohon maaf, token tidak valid\n\n')
        client_socket.sendall(b'Ingin mendaftar?\n')
        contact(client_socket, client_address)
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    t = threading.Thread(target=handle_client, args=(client_socket, client_address))
    t.start()