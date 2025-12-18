n = int(input("Nhập số lượng phần tử: "))
a = []

for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)

k = int(input("Nhập k: "))

k = k % n

for _ in range(k):
    last = a[n - 1]
    for i in range(n - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = last

print("Danh sách sau khi dịch sang phải", k, "vị trí:")
for x in a:
    print(x, end=" ")
