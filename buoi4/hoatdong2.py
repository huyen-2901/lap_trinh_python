# Hoạt động 2: Duyệt Dictionary bằng for - keys/values/items

diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

# 1. Duyệt qua các keys (tên môn học)
for mon in diem_mon_hoc.keys():
    print(mon)

# 2. Duyệt qua các values (điểm số)
for diem in diem_mon_hoc.values():
    print(diem)

# 3. Duyệt qua cả key và value bằng items()
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

# 4. Tính và in điểm trung bình
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))