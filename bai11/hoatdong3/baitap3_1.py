import matplotlib.pyplot as plt
import pandas as pd

# Đọc file dữ liệu từ thư mục cha
df = pd.read_csv("../diem_sinh_vien.csv")

# Tính điểm trung bình theo môn học
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

# Vẽ biểu đồ cột
plt.figure(figsize=(6, 4))
plt.bar(diem_trung_binh_mon.index, diem_trung_binh_mon.values, color="skyblue")
plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")

# Lưu biểu đồ thành file ảnh và hiển thị
plt.savefig("bieu_do_cot.png")
plt.show()