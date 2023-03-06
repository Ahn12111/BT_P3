class BinhPhuong:
    def __init__(self, number):
        self.bp = number *number

num = float(input("Nhap vao mot so: "))
binhphuong = BinhPhuong(num)
print("binh phuong cua {} : {}".format(num,binhphuong.bp))