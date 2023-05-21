import json

print("Pilih kategori")
print("1. Reset IP")
print("2. Reset NAME")
choose = int(input("Masukkan pilihan: "))

if (choose == 1):
	tokenreset = input("\nMasukkan token yang ingin direset IP: ")
	with open(f"tokens/{tokenreset}.json", "r") as f:
		data = json.load(f)
	if data[tokenreset]:
		if data[tokenreset]["IP"] == None:
			print(f"Error: IP Token ({tokenreset}) sudah bernilai null")
		else:
			data[tokenreset]["IP"] = None
			with open(f"tokens/{tokenreset}.json", "w") as f:
				json.dump(data, f, indent=2)
			print(f"Success: IP untuk token ({tokenreset}) berhasil direset")
	else:
		print(f"Error: Token ({tokenreset}) tidak valid!")
if (choose == 2):
	ipreset = input("\nMasukkan token yang ingin direset NAME: ")
	with open(f"tokens/{ipreset}.json", "r") as f:
		data = json.load(f)
	if data[ipreset]:
		if ((data[ipreset]["NAME"] == None) or (len(data[ipreset]["NAME"]) == 0)):
			print(f"Error: NAME Token ({ipreset}) sudah bernilai null")
		else:
			data[ipreset]["NAME"] = None
			with open(f"tokens/{ipreset}.json", "w") as f:
				json.dump(data, f, indent=2)
			print(f"Success: NAME untuk token ({ipreset}) berhasil direset")
	else:
		print(f"Error: Token ({ipreset}) tidak valid!")
else:
	print("Pilih kategori 1/2")



