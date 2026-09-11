# Giả định dictionary ban đầu
sinh_vien = {
    "ten": "Nguyen Van A",
    "diem_tb": 8.0
}

# --- Bài tập 1.2: Thêm / sửa / xóa ---

# Thêm khóa mới
sinh_vien["lop"] = "CNTT01"

# Sửa giá trị của khóa đã có
sinh_vien["diem_tb"] = 9.0

# In ra dictionary sau khi thêm và sửa
print(sinh_vien)

# Xóa theo khóa, trả về giá trị vừa xóa
diem_cu = sinh_vien.pop("diem_tb")

# In kết quả sau khi xóa
print(sinh_vien, "- diem da xoa:", diem_cu)

# Cập nhật / thêm nhiều khóa cùng lúc
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"})

# In kết quả sau khi cập nhật
print(sinh_vien)


# --- Hoạt động 2: Duyệt Dictionary bằng for - keys/values/items ---

diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}