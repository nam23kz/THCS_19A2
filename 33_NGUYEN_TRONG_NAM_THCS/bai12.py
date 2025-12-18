
def nhap_ma_tran(name):
    m = int(input(f"Nhập số dòng của ma trận {name}: "))
    n = int(input(f"Nhập số cột của ma trận {name}: "))
    print(f"Nhập các phần tử của ma trận {name} (cách nhau bằng dấu cách):")
    ma_tran = []
    for i in range(m):
        while True:
            dong = input(f"Dòng {i+1}: ").split()
            if len(dong) != n:
                print(f"Số phần tử không đúng. Vui lòng nhập lại {n} phần tử.")
            else:
                # Chuyển sang số nguyên
                dong = [int(x) for x in dong]
                ma_tran.append(dong)
                break
    return ma_tran, m, n

def in_ma_tran(ma_tran):
    for dong in ma_tran:
        print(' '.join(map(str, dong)))

# Hàm nhân hai ma trận
def nhan_ma_tran(A, B, m, n, q):
    # A: m x n, B: n x q
    C = [[0 for _ in range(q)] for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A, m, n = nhap_ma_tran("A")
B, p, q = nhap_ma_tran("B")

if n != p:
    print("Không thể nhân hai ma trận này vì số cột của A khác số dòng của B.")
else:
    C = nhan_ma_tran(A, B, m, n, q)
    print("Ma trận kết quả C = A x B là:")
    in_ma_tran(C)
