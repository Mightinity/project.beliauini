import requests
import json

# Definisikan URL dan header
bin_id = "6422be5cace6f33a22febef8"
api_key = "$2b$10$q8I27tTa0dak4w.o5HppW.QgTkQPd1.vv0GqIKeqxad.yuTN9HGOu"
url = f"https://api.jsonbin.io/v3/b/{bin_id}"
headers = {
    "Content-Type": "application/json",
    "X-Master-Key": api_key
}

response = requests.get(url, headers=headers)
data = response.json()

# Data JSON baru
new_data = data, {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Kirim permintaan POST untuk membuat data JSON baru pada JSONBin


response = requests.post(url, headers=headers, json=new_data)



# Cetak pesan hasil dari permintaan POST
if response.status_code == 200:
    print("Data JSON baru berhasil ditambahkan ke JSONBin")
else:
    print("Gagal menambahkan data JSON baru ke JSONBin")
