import pandas as pd

df = pd.read_csv("diem_sinh_vien.csv")

# Tính điểm trung bình của từng sinh viên (làm tròn 2 chữ số)
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print("--- ĐIỂM TRUNG BÌNH TỪNG SINH VIÊN ---")
print(diem_tb_sv)

# Lọc danh sách đạt và không đạt (ngưỡng >= 5.0)
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\n--- SINH VIÊN ĐẠT (>= 5.0) ---")
print(sinh_vien_dat)

print("\n--- SINH VIÊN KHÔNG ĐẠT (< 5.0) ---")
print(sinh_vien_khong_dat)