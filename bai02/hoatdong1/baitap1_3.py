# Giả lập dữ liệu đã nhập từ Bài 1.1
ho_ten ="Hoang Ngoc Huyen"
nam_sinh = 2006
diem_tb = 8.9

print("--- KẾT QUẢ IN BẰNG 3 CÁCH ---")

# Cách 1: f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# Cách 2: str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))

# Cách 3: Toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))