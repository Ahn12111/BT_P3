def giaithua(n):
    if (n == 1):
        return 1
    return n * giaithua(n- 1)

n = int(input("Nhap vao mot so: "))
print("{}!: {}". format(n, giaithua(n)))