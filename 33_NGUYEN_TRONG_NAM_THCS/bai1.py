s = input("Nhập chuỗi: ")

chu_cai = 0
chu_so = 0
ky_tu_dac_biet = 0

for ch in s:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        chu_cai += 1
    elif '0' <= ch <= '9':
        chu_so += 1
    else:
        ky_tu_dac_biet += 1

print("Số ký tự chữ cái:", chu_cai)
print("Số ký tự chữ số:", chu_so)
print("Số ký tự đặc biệt:", ky_tu_dac_biet)
