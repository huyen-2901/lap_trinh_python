
import tkinter as tk
from tkinter import ttk, messagebox
import csdl_chi_tieu as db
import matplotlib.pyplot as plt
import os


class UngDungChiTieu:

    def __init__(self, root):
        self.root = root
        self.root.title("QUAN LY CHI TIEU CA NHAN")
        self.root.geometry("1000x650")

        db.tao_bang_neu_chua_co()

        # Tieu de
        tieu_de = tk.Label(
            root,
            text="QUAN LY CHI TIEU CA NHAN",
            font=("Arial", 20, "bold")
        )
        tieu_de.pack(pady=15)

        # Khung nhap thong tin
        khung_nhap = tk.LabelFrame(
            root,
            text="THONG TIN GIAO DICH",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )
        khung_nhap.pack(fill="x", padx=20, pady=10)

        tk.Label(khung_nhap, text="Ngay giao dich:").grid(
            row=0, column=0, padx=5, pady=8, sticky="w"
        )

        self.o_ngay = tk.Entry(khung_nhap, width=25)
        self.o_ngay.grid(row=0, column=1, padx=5, pady=8)
        self.o_ngay.insert(0, "2026-11-06")

        tk.Label(khung_nhap, text="Ten giao dich:").grid(
            row=0, column=2, padx=5, pady=8, sticky="w"
        )

        self.o_ten = tk.Entry(khung_nhap, width=25)
        self.o_ten.grid(row=0, column=3, padx=5, pady=8)

        tk.Label(khung_nhap, text="Loai giao dich:").grid(
            row=1, column=0, padx=5, pady=8, sticky="w"
        )

        self.chon_loai = ttk.Combobox(
            khung_nhap,
            values=["Thu", "Chi"],
            state="readonly",
            width=22
        )
        self.chon_loai.grid(row=1, column=1, padx=5, pady=8)
        self.chon_loai.current(1)

        tk.Label(khung_nhap, text="So tien (VND):").grid(
            row=1, column=2, padx=5, pady=8, sticky="w"
        )

        self.o_so_tien = tk.Entry(khung_nhap, width=25)
        self.o_so_tien.grid(row=1, column=3, padx=5, pady=8)

        tk.Label(khung_nhap, text="Danh muc:").grid(
            row=2, column=0, padx=5, pady=8, sticky="w"
        )

        self.chon_danh_muc = ttk.Combobox(
            khung_nhap,
            values=[
                "An uong",
                "Di lai",
                "Hoc tap",
                "Mua sam",
                "Giai tri",
                "Luong",
                "Thuong",
                "Khac"
            ],
            state="readonly",
            width=22
        )
        self.chon_danh_muc.grid(row=2, column=1, padx=5, pady=8)
        self.chon_danh_muc.current(0)

        tk.Label(khung_nhap, text="Ghi chu:").grid(
            row=2, column=2, padx=5, pady=8, sticky="w"
        )

        self.o_ghi_chu = tk.Entry(khung_nhap, width=25)
        self.o_ghi_chu.grid(row=2, column=3, padx=5, pady=8)

        # Khung nut chuc nang
        khung_nut = tk.Frame(root)
        khung_nut.pack(pady=10)

        tk.Button(
            khung_nut,
            text="THEM GIAO DICH",
            width=18,
            command=self.them_giao_dich
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            khung_nut,
            text="XOA GIAO DICH",
            width=18,
            command=self.xoa_giao_dich
        ).grid(row=0, column=1, padx=8)

        tk.Button(
            khung_nut,
            text="THONG KE",
            width=18,
            command=self.thong_ke
        ).grid(row=0, column=2, padx=8)

        # Bang danh sach giao dich
        khung_bang = tk.LabelFrame(
            root,
            text="DANH SACH GIAO DICH",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )
        khung_bang.pack(fill="both", expand=True, padx=20, pady=10)

        cot = (
            "id",
            "ngay",
            "ten",
            "loai",
            "so_tien",
            "danh_muc",
            "ghi_chu"
        )

        self.bang = ttk.Treeview(
            khung_bang,
            columns=cot,
            show="headings",
            height=12
        )

        self.bang.heading("id", text="Ma")
        self.bang.heading("ngay", text="Ngay")
        self.bang.heading("ten", text="Ten giao dich")
        self.bang.heading("loai", text="Loai")
        self.bang.heading("so_tien", text="So tien")
        self.bang.heading("danh_muc", text="Danh muc")
        self.bang.heading("ghi_chu", text="Ghi chu")

        self.bang.column("id", width=45, anchor="center")
        self.bang.column("ngay", width=100, anchor="center")
        self.bang.column("ten", width=180)
        self.bang.column("loai", width=70, anchor="center")
        self.bang.column("so_tien", width=120, anchor="e")
        self.bang.column("danh_muc", width=120)
        self.bang.column("ghi_chu", width=150)

        thanh_cuon = ttk.Scrollbar(
            khung_bang,
            orient="vertical",
            command=self.bang.yview
        )

        self.bang.configure(yscrollcommand=thanh_cuon.set)

        self.bang.pack(side="left", fill="both", expand=True)
        thanh_cuon.pack(side="right", fill="y")

        self.hien_thi_giao_dich()

    # Hien thi danh sach giao dich
    def hien_thi_giao_dich(self):
        for dong in self.bang.get_children():
            self.bang.delete(dong)

        danh_sach = db.lay_toan_bo_giao_dich()

        for giao_dich in danh_sach:
            self.bang.insert(
                "",
                tk.END,
                values=(
                    giao_dich[0],
                    giao_dich[1],
                    giao_dich[2],
                    giao_dich[3],
                    "{:,.0f}".format(giao_dich[4]),
                    giao_dich[5],
                    giao_dich[6]
                )
            )

    # Them giao dich
    def them_giao_dich(self):
        ngay = self.o_ngay.get().strip()
        ten = self.o_ten.get().strip()
        loai = self.chon_loai.get()
        so_tien = self.o_so_tien.get().strip()
        danh_muc = self.chon_danh_muc.get()
        ghi_chu = self.o_ghi_chu.get().strip()

        if ngay == "" or ten == "" or so_tien == "":
            messagebox.showwarning(
                "Thong bao",
                "Vui long nhap day du thong tin bat buoc!"
            )
            return

        try:
            so_tien = float(so_tien)

            if so_tien <= 0:
                messagebox.showwarning(
                    "Thong bao",
                    "So tien phai lon hon 0!"
                )
                return

        except ValueError:
            messagebox.showwarning(
                "Thong bao",
                "So tien phai la mot con so!"
            )
            return

        if not loai or not danh_muc:
            messagebox.showwarning(
                "Thong bao",
                "Vui long chon loai giao dich va danh muc!"
            )
            return

        db.them_giao_dich(
            ngay,
            ten,
            loai,
            so_tien,
            danh_muc,
            ghi_chu
        )

        self.o_ten.delete(0, tk.END)
        self.o_so_tien.delete(0, tk.END)
        self.o_ghi_chu.delete(0, tk.END)

        self.hien_thi_giao_dich()

        messagebox.showinfo(
            "Thong bao",
            "Them giao dich thanh cong!"
        )

    # Xoa giao dich
    def xoa_giao_dich(self):
        lua_chon = self.bang.selection()

        if not lua_chon:
            messagebox.showwarning(
                "Thong bao",
                "Vui long chon giao dich can xoa!"
            )
            return

        thong_tin = self.bang.item(lua_chon[0])
        id_giao_dich = thong_tin["values"][0]

        xac_nhan = messagebox.askyesno(
            "Xac nhan",
            "Ban co chac chan muon xoa giao dich nay?"
        )

        if xac_nhan:
            db.xoa_giao_dich(id_giao_dich)
            self.hien_thi_giao_dich()

            messagebox.showinfo(
                "Thong bao",
                "Xoa giao dich thanh cong!"
            )

    # Thong ke thu chi va ve bieu do
    def thong_ke(self):
        ket_qua = db.thong_ke_thu_chi()

        tong_thu = 0
        tong_chi = 0

        for loai, so_tien in ket_qua:
            if loai == "Thu":
                tong_thu = so_tien
            elif loai == "Chi":
                tong_chi = so_tien

        so_du = tong_thu - tong_chi

        messagebox.showinfo(
            "THONG KE CHI TIEU",
            "Tong thu: {:,.0f} VND\n"
            "Tong chi: {:,.0f} VND\n"
            "So du: {:,.0f} VND".format(
                tong_thu,
                tong_chi,
                so_du
            )
        )

        # Lay du lieu chi tieu theo danh muc
        du_lieu = db.thong_ke_theo_danh_muc()

        if len(du_lieu) == 0:
            messagebox.showwarning(
                "Thong bao",
                "Chua co du lieu chi tieu de ve bieu do!"
            )
            return

        danh_muc = [dong[0] for dong in du_lieu]
        so_tien = [dong[1] for dong in du_lieu]

        # Ve bieu do
        plt.figure(figsize=(9, 5))
        plt.bar(danh_muc, so_tien)

        plt.title("THONG KE CHI TIEU THEO DANH MUC")
        plt.xlabel("Danh muc")
        plt.ylabel("So tien (VND)")
        plt.xticks(rotation=20)

        plt.tight_layout()

        # Luu bieu do vao thu muc du an
        duong_dan = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "bieu_do_chi_tieu.png"
        )

        plt.savefig(duong_dan)
        plt.show()


# Chay chuong trinh
if __name__ == "__main__":
    cua_so = tk.Tk()
    ung_dung = UngDungChiTieu(cua_so)
    cua_so.mainloop()
