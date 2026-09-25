def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

# Gọi hàm kiểm tra
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong())  # khong truyen so nao -> tra ve 0