n = int(input("Nhập kích thước ma trận vuông n: "))

# Nhập ma trận
a = []
for i in range(n):
    dong = []
    for j in range(n):
        x = int(input(f"Nhập phần tử a[{i}][{j}]: "))
        dong.append(x)
    a.append(dong)

doi_xung = True

for i in range(n):
    for j in range(i + 1, n):  # chỉ cần kiểm tra nửa trên của ma trận
        if a[i][j] != a[j][i]:
            doi_xung = False
            break
    if not doi_xung:
        break

if doi_xung:
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận không phải là ma trận đối xứng")
