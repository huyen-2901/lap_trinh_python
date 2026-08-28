# --- BƯỚC 1: NHẬP DỮ LIỆU TỪ BÀN PHÍM ---
ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoại: ")
email = input("Nhap email: ")

# --- BƯỚC 2: XỬ LÝ VÀ KIỂM TRA DỮ LIỆU (KHÔNG DÙNG IF) ---
# 1. Chuẩn hóa họ tên: xóa khoảng trắng thừa và viết hoa chữ cái đầu
ho_ten_chuan = " ".join(ho_ten.split()).title()

# 2. Kiểm tra SĐT hợp lệ: độ dài chuỗi bằng đúng 10 ký tự (Trả về True/False)
sdt_hop_le = len(sdt) == 10

# 3. Kiểm tra Email hợp lệ: chuỗi có chứa ký tự '@' (Trả về True/False)
email_hop_le = "@" in email

# --- BƯỚC 3: IN KẾT QUẢ RA MÀN HÌNH ---
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoại hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")