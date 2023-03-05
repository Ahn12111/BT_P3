def xuly():
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 != 0):
            print(i, end = ', ')

print("Cac so chia het cho 7, nhung khong phai boi so cua 5: ")
xuly()