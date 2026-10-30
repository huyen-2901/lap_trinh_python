import pandas as pd

df = pd.read_csv("diem_sinh_vien.csv")

print("--- ĐIỂM TRUNG BÌNH TỪNG MÔN HỌC ---")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)

print("\n--- THỐNG KÊ CHUNG ---")
print("Điểm trung bình toàn bộ:", round(df["diem"].mean(), 2))
print("Điểm cao nhất:", df["diem"].max())
print("Điểm thấp nhất:", df["diem"].min())