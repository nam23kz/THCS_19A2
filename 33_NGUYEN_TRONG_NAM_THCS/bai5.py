n = int(input("Nhập số lượng phần tử: "))
a = []

for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)

ket_qua = []

for i in range(n):
    trung = False
    for j in range(len(ket_qua)):
        if a[i] == ket_qua[j]:
            trung = True
            break
    if not trung:
        ket_qua.append(a[i])

print("Danh sách sau khi loại bỏ phần tử trùng lặp:")
for x in ket_qua:
    print(x, end=" ")
