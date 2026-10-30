import matplotlib.pyplot as plt

# Dữ liệu các lần kiểm tra và điểm số tương ứng
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

# Vẽ biểu đồ đường
plt.figure(figsize=(6, 4))
plt.plot(lan_kiem_tra, diem_qua_cac_lan, marker="o", color="green")
plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")

# Lưu biểu đồ thành file ảnh và hiển thị
plt.savefig("bieu_do_duong.png")
plt.show()