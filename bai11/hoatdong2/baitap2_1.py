import pandas as pd

df = pd.read_csv("diem_sinh_vien.csv")

print("--- 5 DÒNG ĐẦU TIÊN ---")
print(df.head())

print("\n--- KÍCH THƯỚC BẢNG (Số dòng, Số cột) ---")
print(df.shape)
print("\n--- DANH SÁCH TÊN CỘT ---")
print(df.columns.tolist())