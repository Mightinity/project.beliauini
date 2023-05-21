import requests

url = 'https://api.jsonbin.io/v3/b'
headers = {
  'Content-Type': 'application/json',
  'X-Master-Key': '$2b$10$q8I27tTa0dak4w.o5HppW.QgTkQPd1.vv0GqIKeqxad.yuTN9HGOu',
  'X-Bin-Name': "TOKEN RSA DISKRIT"
}
data = {
    "GHBU-ZYJT-V9SK-QKRG": "127.0.0.1", "USER-WIJA-YA00-READ": "terpakai","L7VF-JWZP-PMY2-B341": "terpakai","XQT4-QZVD-4L04-PTQ7": "terpakai","USER-KEMA-LDIN-0001": "terpakai","ARYA-MAND-ALA0-1230": "terpakai","USER-MIRZ-A009-READ": "terpakai"}

req = requests.post(url, json=data, headers=headers)
print(req.text)