import socket
import threading
import vlc
import json
import bcrypt

HOST = '0.0.0.0'
PORT = 5555

print("\nMenjalankan b3liau1niChat dengan port " + str(PORT))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1000)

clients = []
passwords = {}

# Baca file password.json dan simpan pada variabel `passwords`
with open('password.json') as f:
    passwords = json.load(f)

def handle_client(client_socket, client_address):
    clients.append(client_socket)   

    # Tanyakan password kepada user dan periksa apakah password yang dimasukkan benar
    authenticated = False
    while not authenticated:
        client_socket.send("Masukkan password: ".encode())
        password_attempt = client_socket.recv(1024).decode().strip()

        if not password_attempt:
            continue

        if bcrypt.checkpw(password_attempt.encode(), passwords['moonap']['password'].encode()):
            authenticated = True
            client_socket.send("Authentication successful!\n".encode())
            client_name = passwords['moonap']['name']
        elif bcrypt.checkpw(password_attempt.encode(), passwords['bimo']['password'].encode()):
            authenticated = True
            client_socket.send("Authentication successful!\n".encode())
            client_name = passwords['bimo']['name']
        else:
            client_socket.send("Password salah. Silakan coba lagi.\n".encode())

    for client in clients:
        if client != client_socket:
            client.send(("Klien " + client_name + " terhubung\n").encode())
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        if data == b"\n":
            continue
        sound = vlc.MediaPlayer("https://proxy.notificationsounds.com/notification-sounds/maybe-one-day-584/download/file-sounds-1131-maybe-one-day.mp3")
        sound.play()
        for client in clients:
            if client != client_socket:
                client.send((client_name + ": " + data.decode()).encode())

    clients.remove(client_socket)
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    t = threading.Thread(target=handle_client, args=(client_socket, client_address))
    t.start()
