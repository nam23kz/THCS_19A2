n = int(input("Nhập kích thước ma trận vuông n: "))

a = []
for i in range(n):
    dong = []
    for j in range(n):
        x = int(input(f"Nhập phần tử a[{i}][{j}]: "))
        dong.append(x)
    a.append(dong)

tong = 0
for i in range(n):
    tong += a[i][n - 1 - i]

print("Tổng các phần tử trên đường chéo phụ là:", tong)
