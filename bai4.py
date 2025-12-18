n = int(input("Nhập số lượng phần tử: "))
a = []

for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)

max1 = a[0]
max2 = None

for i in range(1, n):
    if a[i] > max1:
        max2 = max1
        max1 = a[i]
    elif a[i] != max1:
        if max2 is None or a[i] > max2:
            max2 = a[i]

print("Giá trị lớn thứ hai là:", max2)
