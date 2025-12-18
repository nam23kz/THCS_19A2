m = int(input("Nhập số dòng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

a = []
for i in range(m):
    dong = []
    for j in range(n):
        x = int(input(f"Nhập phần tử a[{i}][{j}]: "))
        dong.append(x)
    a.append(dong)

max_tong = None
hang_max = -1

for i in range(m):
    tong = 0
    for j in range(n):
        tong += a[i][j]
    if max_tong is None or tong > max_tong:
        max_tong = tong
        hang_max = i

print(f"Hàng có tổng lớn nhất là hàng thứ {hang_max} với tổng = {max_tong}")
