s = input("Nhập chuỗi: ")

ket_qua = ""
truoc_la_khoang_trang = False

for ch in s:
    if ch != ' ':
        ket_qua += ch
        truoc_la_khoang_trang = False
    else:
        if not truoc_la_khoang_trang:
            ket_qua += ch
            truoc_la_khoang_trang = True

if len(ket_qua) > 0 and ket_qua[0] == ' ':
    ket_qua = ket_qua[1:]

if len(ket_qua) > 0 and ket_qua[-1] == ' ':
    ket_qua = ket_qua[:-1]

print("Chuỗi sau khi xóa khoảng trắng thừa:")
print(ket_qua)
