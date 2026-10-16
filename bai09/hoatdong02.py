import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du Radiobutton")
cua_so.geometry("300x200")

nhan_ket_qua = tk.Label(cua_so, text="")

bien_loai_tai_khoan = tk.StringVar(value="ca_nhan") # giá trị mặc định

tk.Label(cua_so, text="Chon loai tai khoan:", font=("Arial", 12)).pack(pady=10)

tk.Radiobutton(cua_so, text="Ca nhan", variable=bien_loai_tai_khoan, value="ca_nhan").pack(anchor="w", padx=30)
tk.Radiobutton(cua_so, text="Doanh nghiep", variable=bien_loai_tai_khoan, value="doanh_nghiep").pack(anchor="w", padx=30)

def xem_loai_tai_khoan():
    # Đã sửa lỗi thụt lề và cập nhật văn bản trực tiếp lên giao diện
    nhan_ket_qua.config(text=f"Ban da chon: {bien_loai_tai_khoan.get()}")

tk.Button(cua_so, text="Xac nhan", command=xem_loai_tai_khoan).pack(pady=10)

nhan_ket_qua.pack(pady=5)

cua_so.mainloop()