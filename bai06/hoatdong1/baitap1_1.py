# 1. Hàm tìm Ước số chung lớn nhất (USCLN)
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 2. Hàm tìm Bội số chung nhỏ nhất (BSCNN)
def bscnn(a, b):
    return a * b // uscln(a, b)

# 3. Hàm kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Tối ưu hóa kiểm tra tới căn bậc hai của n
        if n % i == 0:
            return False
    return True

# 4. Hàm kiểm tra số hoàn thiện
def kiem_tra_so_hoan_thien(n):
    if n <= 0:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n


# ==========================================
# GỌI THỬ MỖI HÀM VỚI ÍT NHẤT 3 BỘ DỮ LIỆU
# ==========================================

print("--- KIỂM TRA HÀM USCLN ---")
print("USCLN(24, 36) =", uscln(24, 36))
print("USCLN(17, 13) =", uscln(17, 13))
print("USCLN(100, 25) =", uscln(100, 25))

print("\n--- KIỂM TRA HÀM BSCNN ---")
print("BSCNN(4, 6) =", bscnn(4, 6))
print("BSCNN(5, 7) =", bscnn(5, 7))
print("BSCNN(12, 18) =", bscnn(12, 18))

print("\n--- KIỂM TRA HÀM NGỦYÊN TỐ ---")
print("29 có phải số nguyên tố?", kiem_tra_nguyen_to(29))
print("15 có phải số nguyên tố?", kiem_tra_nguyen_to(15))
print("1 có phải số nguyên tố?", kiem_tra_nguyen_to(1))

print("\n--- KIỂM TRA HÀM SỐ HOÀN THIỆN ---")
print("28 có phải số hoàn thiện?", kiem_tra_so_hoan_thien(28))  # 28 = 1 + 2 + 4 + 7 + 14
print("6 có phải số hoàn thiện?", kiem_tra_so_hoan_thien(6))     # 6 = 1 + 2 + 3
print("12 có phải số hoàn thiện?", kiem_tra_so_hoan_thien(12))