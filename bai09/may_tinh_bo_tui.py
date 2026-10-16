import tkinter as tk
from tkinter import messagebox


cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("300x400")
cua_so.resizable(False, False)


bieu_thuc = tk.StringVar(value="")


hien_thi = tk.Entry(
    cua_so, 
    textvariable=bieu_thuc, 
    font=("Arial", 20), 
    justify="right", 
    bd=5, 
    relief=tk.SUNKEN
)
hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)


def bam_nut(gia_tri):
    hien_tai = bieu_thuc.get()
    bieu_thuc.set(hien_tai + str(gia_tri))


def xoa_man_hinh():
    bieu_thuc.set("")


def tinh_ket_qua():
    try:
        
        ket_qua = eval(bieu_thuc.get())
        bieu_thuc.set(str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0!")
        bieu_thuc.set("")
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
        bieu_thuc.set("")

# Danh sách các nút bấm (Văn bản nút, vị trí hàng, vị trí cột)
cac_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, hang, cot) in cac_nut:
    if text == '=':
        btn = tk.Button(cua_so, text=text, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=tinh_ket_qua)
    elif text == 'C':
        btn = tk.Button(cua_so, text=text, font=("Arial", 14, "bold"), bg="#f44336", fg="white", command=xoa_man_hinh)
    else:
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), command=lambda t=text: bam_nut(t))
    
    btn.grid(row=hang, column=cot, sticky="nsew", padx=5, pady=5)


for i in range(5):
    cua_so.rowconfigure(i, weight=1)
for j in range(4):
    cua_so.columnconfigure(j, weight=1)


cua_so.mainloop()