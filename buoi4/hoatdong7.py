# Khởi tạo dictionary quản lý điểm
quan_ly_diem = {
    "Nguyen Van A": [8.0, 7.5, 9.0],
    "Tran Thi B": [6.0, 6.5, 5.5],
    "Le Van C": [9.0, 9.5, 8.5],
}

# Thêm sinh viên mới
quan_ly_diem["Pham Thi D"] = [7.0, 8.0, 7.5]

# Sửa điểm môn đầu tiên của một sinh viên
quan_ly_diem["Tran Thi B"][0] = 7.0

# Tính điểm trung bình cho từng sinh viên
diem_trung_binh = {}
for ho_ten, danh_sach_diem in quan_ly_diem.items():
    diem_trung_binh[ho_ten] = round(sum(danh_sach_diem) / len(danh_sach_diem), 2)

# In bảng điểm trung bình và kiểm tra đạt loại Giỏi
print("BẢNG ĐIỂM TRUNG BÌNH:")
for ho_ten, dtb in diem_trung_binh.items():
    dat_loai_gioi = dtb >= 8.0
    print(f"{ho_ten:<15} - DTB: {dtb:<5} - Dat loai Gioi? {dat_loai_gioi}")