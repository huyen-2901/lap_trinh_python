import tkinter as tk

# Hàm xử lý khi bấm nút Submit
def xu_ly_submit():
    ho_ten = entry_ho_ten.get()
    tuoi = entry_tuoi.get()
    email = entry_email.get()
    nhan_ket_qua.config(
        text=f"Da nhan: {ho_ten} - {tuoi} tuoi - {email}"
    )

# Hàm xử lý khi bấm nút Xóa (Yêu cầu mở rộng)
def xu_ly_xoa():
    entry_ho_ten.delete(0, tk.END)
    entry_tuoi.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    nhan_ket_qua.config(text="")

# Khởi tạo cửa sổ
cua_so = tk.Tk()
cua_so.title("Form nhap thong tin")
cua_so.geometry("400x300")
cua_so.resizable(False, False)

# Các nhãn và ô nhập liệu
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Nút Submit và nút Xóa
nut_submit = tk.Button(cua_so, text="Submit", command=xu_ly_submit)
nut_submit.grid(row=3, column=0, padx=10, pady=15)

nut_xoa = tk.Button(cua_so, text="Xoa", command=xu_ly_xoa)
nut_xoa.grid(row=3, column=1, padx=10, pady=15)

# Nhãn hiển thị kết quả
nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 11), fg="blue")
nhan_ket_qua.grid(row=4, column=0, columnspan=2, pady=10)

# Vòng lặp chính giữ cửa sổ hiển thị
cua_so.mainloop()