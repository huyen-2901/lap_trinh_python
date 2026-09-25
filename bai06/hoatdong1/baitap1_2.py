# 1. Hàm không trả về giá trị (trả về None)
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return  # ham khong tra ve gia tri (tra ve None)

# 2. Hàm trả về nhiều giá trị qua tuple
def chia_lay_thuong_du(a, b):
    return a // b, a % b  # tra ve nhieu gia tri qua tuple

# Gọi hàm thử nghiệm
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")