s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))

tu = ""
ket_qua = []

for ch in s:
    if ch != ' ':
        tu += ch
    else:
        if len(tu) > n:
            ket_qua.append(tu)
        tu = ""

if len(tu) > n:
    ket_qua.append(tu)

print("Các từ có độ dài lớn hơn", n, "là:")
for t in ket_qua:
    print(t)
