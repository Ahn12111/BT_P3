def xuly(n):
    for i in range(1, n + 1):
        #Thêm một bộ phần tử vào dictionary trong đó key: i, value: i*i
        dic.setdefault(i , i * i)

#Taọ một dictionary rỗng
dic = {} 
n = int(input("Nhap mot so nguyen: "))
xuly(n)
print(dic)

