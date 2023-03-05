def xuly(str):
    #Hàm split dùng để tác một chuỗi thành các chuỗi theo yêu cầu
    lis = list(str.split(","))
    tup = tuple(lis)
    print(lis)
    print(tup)


str = input("Nhap mot chuoi so: ")
xuly(str)

#Ví dụ đề bài:
#Nhập vào một chuỗi: 21,54,78,35,65
#Kết qủa in ra gồm một list và tuple:
#['21', '54', '78', '35', '65'] (list)
#('21', '54', '78', '35', '65') (tuple)
