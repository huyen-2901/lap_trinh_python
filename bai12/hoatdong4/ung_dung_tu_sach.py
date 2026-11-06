
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import os
import sys

# Kết nối với module cơ sở dữ liệu ở hoạt động 3
duong_dan = os.path.join(os.path.dirname(__file__), "..", "hoatdong3")
sys.path.append(os.path.abspath(duong_dan))

import csdl_sach as db


class UngDungTuSach:

    def __init__(self, root):
        self.root = root
        self.root.title("Quan ly Tu sach ca nhan")
        self.root.geometry("600x500")

        db.tao_bang_neu_chua_co()

        # Tiêu đề
        lbl_tieu_de = tk.Label(
            root,
            text="QUAN LY TU SACH CA NHAN",
            font=("Arial", 16, "bold")
        )
        lbl_tieu_de.pack(pady=10)

        # Khung nhập thông tin
        khung_nhap = tk.Frame(root)
        khung_nhap.pack(pady=5)

        tk.Label(khung_nhap, text="Tên sách:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.o_ten_sach = tk.Entry(khung_nhap, width=35)
        self.o_ten_sach.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="Tác giả:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.o_tac_gia = tk.Entry(khung_nhap, width=35)
        self.o_tac_gia.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="Thể loại:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )

        self.chon_the_loai = ttk.Combobox(
            khung_nhap,
            width=32,
            state="readonly",
            values=[
                "Ky nang song",
                "Tieu thuyet",
                "Lich su",
                "Khoa hoc",
                "Kinh te",
                "Khac"
            ]
        )
        self.chon_the_loai.grid(row=2, column=1, padx=5, pady=5)
        self.chon_the_loai.current(0)

        # Danh sách sách
        tk.Label(
            root,
            text="DANH SACH SACH",
            font=("Arial", 11, "bold")
        ).pack(pady=5)

        self.danh_sach = tk.Listbox(root, width=75, height=12)
        self.danh_sach.pack(pady=5)

        # Khung nút chức năng
        khung_nut = tk.Frame(root)
        khung_nut.pack(pady=10)

        tk.Button(
            khung_nut,
            text="Them sach",
            width=15,
            command=self.them_sach
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            khung_nut,
            text="Danh dau da doc",
            width=15,
            command=self.danh_dau_da_doc
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            khung_nut,
            text="Xoa sach",
            width=15,
            command=self.xoa_sach
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            khung_nut,
            text="Thong ke",
            width=15,
            command=self.xu_ly_thong_ke
        ).grid(row=0, column=3, padx=5)

        self.hien_thi_danh_sach()

    # Hiển thị danh sách sách
    def hien_thi_danh_sach(self):
        self.danh_sach.delete(0, tk.END)

        danh_sach_sach = db.lay_toan_bo_sach()

        for sach in danh_sach_sach:
            trang_thai = "Da doc" if sach[4] == 1 else "Chua doc"

            noi_dung = (
                str(sach[0]) + " - " +
                sach[1] + " - " +
                sach[2] + " - " +
                sach[3] + " - " +
                trang_thai
            )

            self.danh_sach.insert(tk.END, noi_dung)

    # Thêm sách
    def them_sach(self):
        ten_sach = self.o_ten_sach.get().strip()
        tac_gia = self.o_tac_gia.get().strip()
        the_loai = self.chon_the_loai.get()

        if ten_sach == "" or tac_gia == "":
            messagebox.showwarning(
                "Thong bao",
                "Vui long nhap day du ten sach va tac gia!"
            )
            return

        db.them_sach(ten_sach, tac_gia, the_loai)

        self.o_ten_sach.delete(0, tk.END)
        self.o_tac_gia.delete(0, tk.END)

        self.hien_thi_danh_sach()

        messagebox.showinfo("Thong bao", "Them sach thanh cong!")

    # Lấy mã sách đang chọn
    def lay_id_sach_dang_chon(self):
        vi_tri = self.danh_sach.curselection()

        if not vi_tri:
            messagebox.showwarning(
                "Thong bao",
                "Vui long chon mot cuon sach!"
            )
            return None

        noi_dung = self.danh_sach.get(vi_tri[0])
        id_sach = int(noi_dung.split(" - ")[0])

        return id_sach

    # Đánh dấu sách đã đọc
    def danh_dau_da_doc(self):
        id_sach = self.lay_id_sach_dang_chon()

        if id_sach is None:
            return

        db.danh_dau_da_doc(id_sach)
        self.hien_thi_danh_sach()

        messagebox.showinfo(
            "Thong bao",
            "Da danh dau sach da doc!"
        )

    # Xóa sách
    def xoa_sach(self):
        id_sach = self.lay_id_sach_dang_chon()

        if id_sach is None:
            return

        xac_nhan = messagebox.askyesno(
            "Xac nhan",
            "Ban co chac chan muon xoa sach nay?"
        )

        if xac_nhan:
            db.xoa_sach(id_sach)
            self.hien_thi_danh_sach()

            messagebox.showinfo(
                "Thong bao",
                "Xoa sach thanh cong!"
            )

    # Thống kê theo thể loại
    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_the_loai()

        if len(du_lieu) == 0:
            messagebox.showwarning(
                "Thong bao",
                "Chua co du lieu de thong ke!"
            )
            return

        the_loai = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]

        plt.figure(figsize=(8, 5))
        plt.bar(the_loai, so_luong)

        plt.title("Thong ke so luong sach theo the loai")
        plt.xlabel("The loai")
        plt.ylabel("So luong sach")
        plt.xticks(rotation=20)

        plt.tight_layout()

        # Lưu biểu đồ vào thư mục hoạt động 5
        thu_muc = os.path.join(
            os.path.dirname(__file__),
            "..",
            "hoatdong5"
        )

        os.makedirs(thu_muc, exist_ok=True)

        duong_dan_anh = os.path.join(
            thu_muc,
            "thong_ke_the_loai.png"
        )

        plt.savefig(duong_dan_anh)
        plt.show()


# Chạy chương trình
if __name__ == "__main__":
    cua_so = tk.Tk()
    ung_dung = UngDungTuSach(cua_so)
    cua_so.mainloop()
