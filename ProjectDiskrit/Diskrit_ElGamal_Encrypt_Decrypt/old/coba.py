angka = int(input("Masukkan angka: "))

num = 2
prevnum = 1

array = [prevnum]

while (num <= angka):
    print(f"{num} = {num//2} + {prevnum}")
    num += num
    prevnum += prevnum
    array.append(prevnum)
    print(array)
    arrlen = (len(array)-1)
    if angka in array:
        print("SUKSES")
        break