import socket

def get_local_ip():
    try:
        # Membuat socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Menghubungkan socket ke server DNS Google
        s.connect(("8.8.8.8", 80))

        # Mendapatkan alamat IP lokal
        local_ip = s.getsockname()[0]

        # Menutup socket
        s.close()

        return local_ip
    except socket.error:
        return "Tidak dapat mengambil alamat IP lokal."

# Memanggil fungsi untuk mendapatkan alamat IP lokal
ip_lokal = get_local_ip()
print("Alamat IP lokal komputer Anda adalah:", ip_lokal)