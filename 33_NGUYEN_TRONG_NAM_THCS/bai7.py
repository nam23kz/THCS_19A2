n = int(input("Nhập số lượng phần tử: "))
a = []

for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)

S = int(input("Nhập tổng cần tìm: "))

print("Các cặp số có tổng bằng", S, "là:")

co_cap = False
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] + a[j] == S:
            print("(", a[i], ",", a[j], ")")
            co_cap = True

if not co_cap:
    print("Không có cặp số nào")
