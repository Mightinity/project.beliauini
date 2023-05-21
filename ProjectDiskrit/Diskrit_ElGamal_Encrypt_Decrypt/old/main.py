angka = int(input("Masukkan angka: "))

num = 2
prevnum = 1

array = []

while (num < angka):
    print(f"{num} = {prevnum} + {num//2}")
    num += num
    prevnum += prevnum
    nilaitetap = num
    array.append(num)
    arrlen = len(array)-1
    numbaru = nilaitetap//2
    while (nilaitetap > angka):
        if angka in array:
            break;
        print(f"numbaru = {numbaru}")
        if (numbaru != angka):
            arrlen = arrlen
            numbaru = numbaru + array[arrlen]
            print(arrlen)
            print(array)
        print(f"numbaru = {numbaru} + {array[arrlen]}")
        # arrlen = arrlen-1
        # numbaru2 = numbaru + array[arrlen]
        # print(f"a. numbaru2 = {numbaru2} + {array[arrlen]}")
        # array.append(numbaru2)
        # print("SUKSES")



    # while (nilaitetap > angka):
    #     print(f"numbaru2 = {numbaru2}")
    #     print(f"numbaru2 = {nilaitetap//2} + {array[arrlen]}")
    #     print(arrlen)
    #     print(array)
    #     if (numbaru2 > angka):
    #         arrlen = arrlen-1
    #     else:
    #         arrlen = arrlen-1
    #         array.append(numbaru2)
    #         numbaru2 = numbaru2 + array[arrlen]
    #         print("SUKSES")
    #         print(f"numbaru2 = {numbaru2}")
    #         array.append(numbaru2)
    #         break






    # if (numbaru == angka):
    #     break





        # print(f"numbaru = {numbaru}")
        # num = num + (num//2)
        # # 2048 = 2048 // 2
        # print(num)
        # numbaru = (num//2)
        # print(f"{numbaru} = {num//2} + {(numbaru//2)}")
        # # if (num < angka):
        # #     print(num)

print(array)





    # if num == angka:
    #     break;




# while (running):
#     print(f"{num} = {prevnum} + {(num//2)}")
#     prevnum = prevnum + (num//2)
#     num += num
#     # print(f"num = {num}")
#     if num > angka:
#         num2 = num - (num//2)
#         num3 = num2 + (num2//2)
#         # print(f"num2 = {num2}")
#         if num2 < angka:
#             print(f"{num3} = {num2} + {(num2//2)}")
#             num2 = num3
#             break;
