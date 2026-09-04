import math
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")
# Tạo danh sách chứa các tuple tọa độ
cac_diem = [(0, 0), (3, 4), (6, 8)]

# Dùng vòng lặp for để tính khoảng cách của từng điểm so với gốc tọa độ (0, 0)
for diem in cac_diem:
    x, y = diem
    # Công thức khoảng cách tới (0,0): sqrt((x-0)^2 + (y-0)^2) = sqrt(x^2 + y^2)
    kc_goc = math.sqrt(x ** 2 + y ** 2)
    print(f"Khoang cach tu {diem} den goc toa do (0, 0) la: {round(kc_goc, 2)}")
