n = int(input("Nhập số lượng phần tử: "))
a = []

for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)

tong_chan = 0
tong_le = 0

for i in range(n):
    if a[i] % 2 == 0:
        tong_chan += a[i]
    else:
        tong_le += a[i]

print("Tổng các số chẵn:", tong_chan)
print("Tổng các số lẻ:", tong_le)
