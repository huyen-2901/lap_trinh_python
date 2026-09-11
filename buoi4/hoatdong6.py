doan_van = "python la ngon ngu lap trinh python de hoc python de dung"

# Tách đoạn văn thành danh sách các từ
danh_sach_tu = doan_van.split()

# Khởi tạo dictionary để lưu tần suất xuất hiện của từ
tan_suat = {}

# Đếm số lần xuất hiện của từng từ
for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

# In kết quả
print("Tan suat xuat hien cac tu:")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")