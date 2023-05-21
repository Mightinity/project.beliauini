import socket, threading, json, signal ,sys, os

port = 10050

print("\nMenjalankan socket server (ELGAMAL ENCRYPT) dengan port " + str(port))

def signal_handler(sig, frame):
    print('\nMenerima sinyal SIGINT, menutup socket server...')
    server_socket.close()
    sys.exit(0)

def valuePowMod(value, power, modulus, client_socket):
    digit = value
    modulo = modulus
    pangkat = power

    result = pow(digit, 1, modulo)
    client_socket.sendall(f"{digit}^1 mod {modulo} = {result}\n".encode())
    resultPow = [1]
    resultResult = [digit]

    i = 2
    powNow = 0
    result = 0
    while (i <= pangkat):
        result = pow(digit, i, modulo)
        resultPow.append(i)
        resultResult.append(result)
        digitlain = pow(digit, i//2, modulo)
        client_socket.sendall(f"{digit}^{i} mod {modulo} = [{digit}^{i//2} mod {modulo}] . [{digit}^{i//2} mod {modulo}] mod {modulo}\n".encode())
        client_socket.sendall(f"\t       = [{digitlain}] . [{digitlain}] mod {modulo}\n".encode())
        client_socket.sendall(f"\t       = {digitlain*digitlain} mod {modulo}\n".encode())
        client_socket.sendall(f"\t       = {result}\n".encode())
        powNow = i
        i *= 2
        
    if(powNow < pangkat):
        n = len(resultPow)
        i = n - 1
        while i >= 0:
            if powNow + resultPow[i] == pangkat:
                client_socket.sendall(f"{digit}^{powNow + resultPow[i]} mod {modulo} = [{digit}^{resultPow[i]} mod {modulo}] . [{digit}^{powNow} mod {modulo}] mod {modulo}\n".encode())
                client_socket.sendall(f"\t       = [{resultResult[i]}] . [{result}] mod {modulo}\n".encode())
                client_socket.sendall(f"\t       = {resultResult[i]*result} mod {modulo}\n".encode())
                result = (resultResult[i]*result) % modulo
                client_socket.sendall(f"\t       = {result}\n".encode())
                resultPow.append(powNow + resultPow[i])
                resultResult.append(result)
            elif powNow + resultPow[i] < pangkat:
                client_socket.sendall(f"{digit}^{powNow + resultPow[i]} mod {modulo} = [{digit}^{resultPow[i]} mod {modulo}] . [{digit}^{powNow} mod {modulo}] mod {modulo}\n".encode())
                client_socket.sendall(f"\t       = [{resultResult[i]}] . [{result}] mod {modulo}\n".encode())
                client_socket.sendall(f"\t       = {resultResult[i]*result} mod {modulo}\n".encode())
                result = (resultResult[i]*result) % modulo
                client_socket.sendall(f"\t       = {result}\n".encode())
                resultPow.append(powNow + resultPow[i])
                resultResult.append(result)
            powNow = resultPow[len(resultPow)-1]
            i -= 1
    return result

def note(client_socket):
    logoEnkrip(client_socket)
    client_socket.sendall(b"  Jika kamu baru pertama kali mengerjakan jangan lupa buat deskripsi sendiri\n")
    client_socket.sendall(b"  Tentang publik key dan private key yang dipakai sesuai PDF pak sofyan, oke.\n")
    client_socket.sendall("  Kunci publik (p, 𝛼, β) = (2579, 2, 949) dan kunci private a = 765\n".encode())
    client_socket.sendall(b"  sudah sesuai ya. (tulisan di kunci publik ada yang ga jelas/tanda tanya, itu adalah alpha)\n\n")
    
def inputUser(client_socket, retToken):
    try:
        client_socket.sendall(b"  Silahkan masukkan nilai m(i) kamu = ")
        nilai = int(client_socket.recv(1024).decode().strip())
        with open(f'tokens/{retToken}.json', 'r') as f:
            tokens = json.load(f)
        if nilai not in tokens[retToken]["NAME"]:
            client_socket.sendall(b"  Maaf tidak ada ASCII kode tersebut di nama kamu\n")
            client_socket.close()
        client_socket.sendall(b"  Silahkan pilih angka acak antara 2 sampai 2577 untuk nilai K(i)\n")
        client_socket.sendall(b"  Pilih angka acak yang belum dipilih sebelumnya ya...!!\n")
        client_socket.sendall(b"  Saranku jangan terlalu besar biar ga capek nulisnya nanti = ")
        power = int(client_socket.recv(1024).decode().strip())
        client_socket.sendall(f"  Nilai k yang dipilih adalah {power}".encode())
        client_socket.sendall(b"\n")
        if (power < 2) or (power > 2577):
            raise Exception(b"Input harus lebih besar dari 1 dan lebih kecil dari 2578\n")
        else:
            return nilai, power
    except Exception as e:
        client_socket.sendall(f"Terjadi error: {e}\n".encode())
        client_socket.close()

def gammaValue(value ,power, modulus, client_socket):
    client_socket.sendall(b"==================================================\n")
    client_socket.sendall(f"Proses menghitung rumus 𝛾(i) = 2^{power} mod 2579 <-- lambang gak jelas ini sebenarnya adalah simbol gamma ya\n".encode())
    result = valuePowMod(value, power, modulus, client_socket)
    return result
    
def deltaValue(value, power, modulus, client_socket):
    client_socket.sendall(b"==================================================\n")
    client_socket.sendall(f"Proses menghitung rumus δ = 949^{power} mod 2579\n".encode())
    result = valuePowMod(value, power, modulus, client_socket)
    return result

def finalValue(value, delta, power, modulus, client_socket):
    client_socket.sendall(b"==================================================\n")
    client_socket.sendall(f"Proses menghitung rumus δ = 949^{power} . m mod {modulus}\n".encode())
    client_socket.sendall(f"δ = [949^{power} mod {modulus}] . {value} mod {modulus}\n".encode())
    client_socket.sendall(f"  = [{delta}] . [{value}] mod {modulus}\n".encode())
    client_socket.sendall(f"  = {delta * value} mod {modulus}\n".encode())
    result = (delta * value) % modulus
    client_socket.sendall(f"  = {result}\n".encode())
    return result


def logoEnkrip(client_socket):
    client_socket.sendall(b"        ________                      __\n")
    client_socket.sendall(b"  ___  / / ____/___ _____ ___  ____ _/ /\n")
    client_socket.sendall(b" / _ \/ / / __/ __ `/ __ `__ \/ __ `/ / \n")
    client_socket.sendall(b"/  __/ / /_/ / /_/ / / / / / / /_/ / /  \n")
    client_socket.sendall(b"\___/_/\____/\__,_/_/ /_/ /_/\__,_/_/\n")
    client_socket.sendall(b"  _____                             _   _             \n")
    client_socket.sendall(b" | ____|_ __   ___ _ __ _   _ _ __ | |_(_) ___  _ __  \n")
    client_socket.sendall(b" |  _| | '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \ \n")
    client_socket.sendall(b" | |___| | | | (__| |  | |_| | |_) | |_| | (_) | | | |\n")
    client_socket.sendall(b" |_____|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|\n")
    client_socket.sendall(b"                        |___/|_|                      \n")
    client_socket.sendall(b"\tBy : Kelas Diskrit Pak Sofyan Team\n\n")

def encrypt(client_socket, retToken):
    modulus = 2579
    beta = 949
    value, power = inputUser(client_socket, retToken)
    gamma = gammaValue(2 ,power, modulus, client_socket)
    client_socket.sendall(f"Ditemukan nilai 𝛾 = {gamma} <-- lambang gak jelas ini sebenarnya adalah simbol gamma ya\n\n".encode())
    delta = deltaValue(beta, power, modulus, client_socket)
    client_socket.sendall(f"Ditemukan nilai δ = {delta}\n\n".encode())
    final = finalValue(value, delta, power, modulus, client_socket)
    client_socket.sendall(f"Ditemukan nilai δ(i) = {final}\n\n".encode())
    client_socket.sendall(f"Hasil enkripsi m = {value} dengan k = {power} adalah ({gamma}, {final})\n".encode())
    client_socket.sendall("==================================================\n\n".encode())
    logoEnkrip(client_socket)
    encrypt(client_socket, retToken)
    
def inputUser2(client_socket):
    client_socket.sendall(b"Masukkan nilai yang mau didekripsi dengan ElGamal\n")
    client_socket.sendall(b"Dipisah dengan koma (,). (contoh: 8, 302) : ")
    ct = str(client_socket.recv(1024).decode().strip())
    c1, c2 = ct.split(",")
    c1 = int(c1)
    c2 = int(c2)
    client_socket.sendall(f"\nnilai 𝛾 : {c1}  <-- lambang gak jelas ini sebenarnya adalah simbol gamma ya\n".encode())
    client_socket.sendall(f"nilai δ : {c2}\n".encode())
    return c1, c2

def logoDekrip(client_socket):
    client_socket.sendall(b"        ________                      __\n")
    client_socket.sendall(b"  ___  / / ____/___ _____ ___  ____ _/ /\n")
    client_socket.sendall(b" / _ \/ / / __/ __ `/ __ `__ \/ __ `/ / \n")
    client_socket.sendall(b"/  __/ / /_/ / /_/ / / / / / / /_/ / /  \n")
    client_socket.sendall(b"\___/_/\____/\__,_/_/ /_/ /_/\__,_/_/\n")
    client_socket.sendall(b"  ___                       _   _          \n")
    client_socket.sendall(b" |   \ ___ __ _ _ _  _ _ __| |_(_)___ _ _  \n")
    client_socket.sendall(b" | |) / -_) _| '_| || | '_ \  _| / _ \ ' \ \n")
    client_socket.sendall(b" |___/\___\__|_|  \_, | .__/\__|_\___/_||_|\n")
    client_socket.sendall(b"                  |__/|_|\n")
    client_socket.sendall(b"\tBy : Kelas Diskrit Pak Sofyan Team\n\n")

def decrypt(client_socket):
    logoDekrip(client_socket)
    power = 1813
    modulus = 2579
    client_socket.sendall(b"Untuk proses Dekripsi, pertama-tama harus menghitung pangkat yang akan dipakai\n")
    client_socket.sendall(b"yaitu p-1-a, maka 2579-1-765 = 1813. nilai 1813 yang akan dipakai.\n")
    client_socket.sendall("Lalu hitung 𝛾(simbol gamma)^1813 mod 2579 dan m = δ . 𝛾(simbol gamma)^1813 mod 2579\n\n".encode())
    client_socket.sendall(b"==================================================\n")
    c1, c2 = inputUser2(client_socket)
    client_socket.sendall(b"==================================================\n")
    client_socket.sendall(f"proses menghitung untuk 𝛾^{power} mod {modulus} <-- lambang gak jelas ini sebenarnya adalah simbol gamma ya\n".encode())
    base = valuePowMod(c1, power, modulus, client_socket)
    client_socket.sendall(f"ditemukan  {c1}^1813 mod {modulus} = {base}\n".encode())
    client_socket.sendall(b"==================================================\n")
    client_socket.sendall(f"proses untuk m = δ . 𝛾^{power} mod {modulus} <-- lambang gak jelas ini sebenarnya adalah simbol gamma ya\n".encode())
    client_socket.sendall(f"             m = {c2} . [{c1}^{power} mod {modulus}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = [{c2}] . [{base}] mod {modulus}\n".encode())
    client_socket.sendall(f"               = {c2 * base} mod {modulus}\n".encode())
    m = (c2 * base) % modulus
    client_socket.sendall(f"               = {m}\n".encode())
    client_socket.sendall("--------------------------------------------------\n".encode())
    client_socket.sendall(f"Nilai {m} diubah sesuai ASCII kode jadi {chr(m)}\n".encode())
    client_socket.sendall("==================================================\n".encode())
    decrypt(client_socket)

def convNameToAscii(client_socket, retToken):
    client_socket.sendall(b"\n $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\ $$$$$$\ \n")
    client_socket.sendall(b"$$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|\_$$  _|\n")
    client_socket.sendall(b"$$ /  $$ |$$ /  \__|$$ /  \__|  $$ |    $$ |  \n")
    client_socket.sendall(b"$$$$$$$$ |\$$$$$$\  $$ |        $$ |    $$ |  \n")
    client_socket.sendall(b"$$  __$$ | \____$$\ $$ |        $$ |    $$ |  \n")
    client_socket.sendall(b"$$ |  $$ |$$\   $$ |$$ |  $$\   $$ |    $$ |  \n")
    client_socket.sendall(b"$$ |  $$ |\$$$$$$  |\$$$$$$  |$$$$$$\ $$$$$$\ \n")
    client_socket.sendall(b"\__|  \__| \______/  \______/ \______|\______|\n")
    client_socket.sendall(b"\nTabel ASCII Nama Kamu : ")
    with open(f'tokens/{retToken}.json', 'r') as f:
        tokens = json.load(f)
    # nama = str(client_socket.recv(1024).decode().strip())
    # result = []
    # for kata in nama:
    #     result.append(ord(kata))
    client_socket.sendall(b"\n===========================================\n")
    client_socket.sendall(f"| i  | Karakter  | Plainteks Mi   | ASCII |\n".encode())
    client_socket.sendall(b"===========================================\n")
    for i in range(len(tokens[retToken]['NAME'])):
        if(tokens[retToken]['NAME'][i] == 32):
            client_socket.sendall(f"| {i+1:^2} | {'<spasi>':^9} | {'m'+str(i+1):^14} | {tokens[retToken]['NAME'][i]:^5} |\n".encode())
        else:
            client_socket.sendall(f"| {i+1:^2} | {chr(tokens[retToken]['NAME'][i]):^9} | {'m'+str(i+1):^14} | {tokens[retToken]['NAME'][i]:^5} |\n".encode())
    client_socket.sendall(b"===========================================\n")
    client_socket.sendall(b"\n")
    menu(client_socket, retToken)
    
def menu(client_socket, retToken):
    with open(f'tokens/{retToken}.json', 'r') as f:
        tokens = json.load(f)
    nameArray = []
    if (tokens[retToken]["NAME"] == None or len(tokens[retToken]["NAME"]) == 0):
        client_socket.sendall(b"\n!!! WARNING. Your Name undetected on database\n")
        client_socket.sendall(f"Nama dari token ({retToken}) belum terdaftar di database server\n".encode())
        client_socket.sendall(b"Daftarkan nama kamu sesuai INFOKHS: ")
        name = str(client_socket.recv(1024).decode().strip())
        for word in name:
            nameArray.append(ord(word))
        tokens[retToken]["NAME"] = nameArray
        with open(f'tokens/{retToken}.json', 'w') as f:
            json.dump(tokens, f, indent=2)
        client_socket.sendall(f"Nama {name} berhasil terdaftar di database. Silahkan login kembali!\n".encode())
    else:
        client_socket.sendall(b'\nSilahkan pilih menu\n')
        client_socket.sendall(b"1. Ubah nama ke ASCII kode\n")
        client_socket.sendall(b"2. elGamal Encryption\n")
        client_socket.sendall(b"3. elGamal Decryption\n")
        client_socket.sendall(b"Masukkan pilihan kamu: ")
        choose = int(client_socket.recv(1024).decode().strip())
        if(choose == 1):
            convNameToAscii(client_socket, retToken)
        elif(choose == 2):
            if tokens[retToken]['ENCRYPT'] == "True":
                note(client_socket)
                encrypt(client_socket, retToken)
            else:
                client_socket.sendall(b"Token permission denied!")
        elif(choose == 3):
            if tokens[retToken]['DECRYPT'] == "True":
                decrypt(client_socket)
            else:
                client_socket.sendall(b"Token permission denied!")
        else:
            client_socket.sendall(b"Input jangan aneh-aneh lur, ga ada bounty disini\n")
            menu(client_socket, retToken)

# SOCKET SERVER
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', port))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.listen(1000)

signal.signal(signal.SIGINT, signal_handler)                                                                     

def contact(client_socket, retToken):
    client_socket.sendall(b'Contact Person:\n')
    client_socket.sendall(b'WA: 0822 2853 7028\n')
    client_socket.sendall(b'WA: 0821 7023 9463\n')

def handle_client(client_socket, client_address):
    # global token
    print(f'Klien connect dengan IP: {client_address[0]}:{client_address[1]}')
    # client_ip = client_address[0]
    client_socket.sendall(b"\n")
    client_socket.sendall(b"ElGamal Diskrit Program (v3.1) | (New Database System, New Validation System & Fix Token Crash Bugs) | [Apr 3 2023 15:38]\n")
    client_socket.sendall(b'Masukkan Token: ')
    token = client_socket.recv(1024).decode().strip()

    if os.path.isfile(f"tokens/{token}.json"):
        with open(f'tokens/{token}.json', 'r') as f:
            tokens = json.load(f)
        if tokens[token]['IP']:
            if tokens[token]['IP'] == client_address[0]:
                client_socket.sendall(b'Token valid!\n')
                menu(client_socket, token)
            else:
                client_socket.sendall(b'Mohon maaf, token sudah terdaftar dengan IP yang berbeda\n\n')
                client_socket.sendall(b'Apakah ada kesalahan? hubungi admin.\n')
                contact(client_socket, token)
        else:
            tokens[token]['IP'] = client_address[0]
            with open(f'tokens/{token}.json', 'w') as f:
                json.dump(tokens, f, indent=4)
            client_socket.sendall(b'Token valid!\n')
            menu(client_socket, token)
    else:
        client_socket.sendall(b'\nMohon maaf, token tidak valid\n\n')
        client_socket.sendall(b'Ingin mendaftar?\n')
        contact(client_socket)
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    t = threading.Thread(target=handle_client, args=(client_socket, client_address))
    t.start()
