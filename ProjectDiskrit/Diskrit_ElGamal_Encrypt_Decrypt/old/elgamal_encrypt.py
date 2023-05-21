def valuePowMod(value, power, modulus):
    digit = value
    modulo = modulus
    pangkat = power

    result = pow(digit, 1, modulo)
    print(f"{digit}^1 mod {modulo} = {result}")
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
        print(f"{digit}^{i} mod {modulo} = [{digit}^{i//2}] . [{digit}^{i//2}] mod {modulo}")
        print(f"\t       = [{digitlain}] . [{digitlain}] mod {modulo}")
        print(f"\t       = {digitlain*digitlain} mod {modulo}")
        print(f"\t       = {result}")
        print()
        powNow = i
        i *= 2
        
    if(powNow <= pangkat):
        n = len(resultPow)
        i = n - 1
        while i >= 0:
            if powNow + resultPow[i] == pangkat:
                print(f"{digit}^{powNow + resultPow[i]} mod {modulo} = [{digit}^{resultPow[i]}] . [{digit}^{powNow}] mod {modulo}")
                print(f"\t       = [{resultResult[i]}] . [{result}] mod {modulo}")
                print(f"\t       = {resultResult[i]*result} mod {modulo}")
                result = (resultResult[i]*result) % modulo
                print(f"\t       = {result}")
                print()
                resultPow.append(powNow + resultPow[i])
                resultResult.append(result)
            elif powNow + resultPow[i] < pangkat:
                print(f"{digit}^{powNow + resultPow[i]} mod {modulo} = [{digit}^{resultPow[i]}] . [{digit}^{powNow}] mod {modulo}")
                print(f"\t       = [{resultResult[i]}] . [{result}] mod {modulo}")
                print(f"\t       = {resultResult[i]*result} mod {modulo}")
                result = (resultResult[i]*result) % modulo
                print(f"\t       = {result}")
                print()
                resultPow.append(powNow + resultPow[i])
                resultResult.append(result)
            powNow = resultPow[len(resultPow)-1]
            i -= 1
    return result

def note():
    logo()
    print('''    Jika kamu baru pertama kali mengerjakan jangan lupa buat deskripsi sendiri
    Tentang publik key dan private key yang dipakai sesuai PDF pak sofyan, oke.
    Kunci publik (p, 𝛼, β) = (2579, 2, 949) dan kunci private a = 765
    sudah sesuai ya.\n''')
    
def inputUser():
    try:
        nilai = int(input("Silahkan masukkan nilai M(i) kamu = "))
        print("Silahkan pilih angka acak antara 2 sampai 2577 untuk nilai K(i)")
        power = int(input("Saranku jangan terlalu besar biar ga capek nulisnya nanti = "))
        print()
        if (power < 2) or (power > 2577):
            raise Exception("Input harus lebih besar dari 1 dan lebih kecil dari 2578")
        else:
            return nilai, power
    except Exception as e:
        print("Terjadi error:", e)
        exit(0)

def gammaValue(value ,power, modulus):
    print("==================================================")
    print(f"Proses menghitung rumus 𝛾(i) = 2^{power} mod 2579")
    result = valuePowMod(value, power, modulus)
    return result
    
def deltaValue(value, power, modulus):
    print("==================================================")
    print(f"Proses menghitung rumus δ = 949^{power} mod 2579")
    result = valuePowMod(value, power, modulus)
    return result

def finalValue(value, delta, modulus):
    print("==================================================")
    print(f"Proses menghitung rumus δ = [949^{power} . {value}] mod 2579")
    print(f"δ = [949^{power} mod {modulus}] . {value} mod {modulus}")
    print(f"  = [{delta}] . [{value}] mod {modulus}")
    print(f"  = {delta * value} mod {modulus}")
    result = (delta * value) % modulus
    print(f"  = {result}")
    return result

def logo():
    print('''        ________                      __
  ___  / / ____/___ _____ ___  ____ _/ /
 / _ \/ / / __/ __ `/ __ `__ \/ __ `/ / 
/  __/ / /_/ / /_/ / / / / / / /_/ / /  
\___/_/\____/\__,_/_/ /_/ /_/\__,_/_/''')
    print('''  _____                             _   _             
 | ____|_ __   ___ _ __ _   _ _ __ | |_(_) ___  _ __  
 |  _| | '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \ 
 | |___| | | | (__| |  | |_| | |_) | |_| | (_) | | | |
 |_____|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|
                        |___/|_|                      ''')
    print("\tby: Kelas Diskrit Pak Sofyan Team\n")

if __name__ == "__main__":
    note()
    while True:
        modulus = 2579
        beta = 949
        value, power = inputUser()
        gamma = gammaValue(2 ,power, modulus)
        print(f"Ditemukan nilai 𝛾 = {gamma}\n")
        delta = deltaValue(beta, power, modulus)
        print(f"Ditemukan nilai δ = {delta}\n")
        final = finalValue(value, delta, modulus)
        print(f"Ditemukan nilai δ(i) = {final}\n")
        print(f"Hasil enkripsi m = {value} dengan k = {power} adalah ({gamma}, {final})")
        print("==================================================\n")
        logo()