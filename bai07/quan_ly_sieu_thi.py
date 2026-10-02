
danh_sach_san_pham = [
    {"ma_sp": "SP001", "ten_sp": "Sua tuoi", "loai_sp": "Do uong", "gia": 30000, "so_luong": 20},
    {"ma_sp": "SP002", "ten_sp": "Mi goi", "loai_sp": "Thuc pham", "gia": 5000, "so_luong": 100},
    {"ma_sp": "SP003", "ten_sp": "Nuoc suoi", "loai_sp": "Do uong", "gia": 10000, "so_luong": 50},
    {"ma_sp": "SP004", "ten_sp": "Banh quy", "loai_sp": "Banh keo", "gia": 25000, "so_luong": 30}
]

lich_su_ban_hang = []



def nhap_so_nguyen(thong_bao, toi_thieu=0):
    while True:
        try:
            so = int(input(thong_bao))

            if so < toi_thieu:
                print(f"Vui long nhap so lon hon hoac bang {toi_thieu}.")
            else:
                return so

        except ValueError:
            print("Du lieu khong hop le, vui long nhap so nguyen.")



def tim_san_pham_theo_ma(ma_sp):
    for sp in danh_sach_san_pham:
        if sp["ma_sp"] == ma_sp:
            return sp
    return None



def hien_thi_san_pham():
    if len(danh_sach_san_pham) == 0:
        print("Chua co san pham nao.")
        return

    print("\n" + "=" * 90)
    print(f"{'Ma SP':<12}{'Ten san pham':<20}{'Loai SP':<18}"
          f"{'Gia ban':>15}{'So luong':>15}")
    print("-" * 90)

    for sp in danh_sach_san_pham:
        print(f"{sp['ma_sp']:<12}{sp['ten_sp']:<20}"
              f"{sp['loai_sp']:<18}{sp['gia']:>15,}"
              f"{sp['so_luong']:>15}")

    print("=" * 90)
  
def xem_san_pham_con_hang():
    co_hang = False

    print("\nCAC SAN PHAM CON HANG:")

    for sp in danh_sach_san_pham:
        if sp["so_luong"] > 0:
            print(f"{sp['ma_sp']} - {sp['ten_sp']} - "
                  f"{sp['so_luong']} san pham")
            co_hang = True

    if not co_hang:
        print("Hien khong con san pham nao trong kho.")


def them_san_pham():
    ma_sp = input("Nhap ma san pham: ").strip().upper()

    if ma_sp == "":
        print("Ma san pham khong duoc de trong.")
        return

    if tim_san_pham_theo_ma(ma_sp) is not None:
        print("Ma san pham da ton tai.")
        return

    ten_sp = input("Nhap ten san pham: ").strip()
    loai_sp = input("Nhap loai san pham: ").strip()

    if ten_sp == "" or loai_sp == "":
        print("Ten va loai san pham khong duoc de trong.")
        return

    gia = nhap_so_nguyen("Nhap gia ban: ", 1)
    so_luong = nhap_so_nguyen("Nhap so luong ban dau: ", 0)

    san_pham = {
        "ma_sp": ma_sp,
        "ten_sp": ten_sp,
        "loai_sp": loai_sp,
        "gia": gia,
        "so_luong": so_luong
    }

    danh_sach_san_pham.append(san_pham)

    print("Them san pham thanh cong.")


# 6. NHAP THEM HANG
def nhap_them_hang():
    ma_sp = input("Nhap ma san pham can nhap: ").strip().upper()
    sp = tim_san_pham_theo_ma(ma_sp)

    if sp is None:
        print("Khong tim thay san pham.")
        return

    so_luong = nhap_so_nguyen("Nhap so luong hang them: ", 1)

    sp["so_luong"] += so_luong

    print(f"Da nhap them {so_luong} san pham {sp['ten_sp']}.")
    print(f"So luong ton kho hien tai: {sp['so_luong']}")


# 7. BAN HANG
def ban_hang():
    ma_sp = input("Nhap ma san pham can ban: ").strip().upper()
    sp = tim_san_pham_theo_ma(ma_sp)

    if sp is None:
        print("Khong tim thay san pham.")
        return

    if sp["so_luong"] == 0:
        print("San pham da het hang.")
        return

    print(f"San pham: {sp['ten_sp']}")
    print(f"Don gia: {sp['gia']:,} VND")
    print(f"So luong ton kho: {sp['so_luong']}")

    so_luong = nhap_so_nguyen("Nhap so luong can mua: ", 1)

    if so_luong > sp["so_luong"]:
        print("So luong trong kho khong du.")
        return

    thanh_tien = sp["gia"] * so_luong

    # Cap nhat ton kho
    sp["so_luong"] -= so_luong

    # Luu lich su giao dich
    giao_dich = {
        "ma_sp": sp["ma_sp"],
        "ten_sp": sp["ten_sp"],
        "so_luong": so_luong,
        "don_gia": sp["gia"],
        "thanh_tien": thanh_tien
    }

    lich_su_ban_hang.append(giao_dich)

    print("\n--- HOA DON BAN HANG ---")
    print(f"Ma san pham: {sp['ma_sp']}")
    print(f"Ten san pham: {sp['ten_sp']}")
    print(f"So luong mua: {so_luong}")
    print(f"Don gia: {sp['gia']:,} VND")
    print(f"TONG THANH TOAN: {thanh_tien:,} VND")
    print(f"So luong con lai: {sp['so_luong']}")


# 8. THONG KE DOANH THU
def thong_ke_doanh_thu():
    if len(lich_su_ban_hang) == 0:
        print("Chua co giao dich ban hang nao.")
        return

    tong_doanh_thu = 0

    print("\n" + "=" * 85)
    print("LICH SU BAN HANG")
    print("-" * 85)
    print(f"{'Ma SP':<12}{'Ten san pham':<20}"
          f"{'So luong':>12}{'Don gia':>18}{'Thanh tien':>20}")
    print("-" * 85)

    for gd in lich_su_ban_hang:
        print(f"{gd['ma_sp']:<12}{gd['ten_sp']:<20}"
              f"{gd['so_luong']:>12}"
              f"{gd['don_gia']:>18,}"
              f"{gd['thanh_tien']:>20,}")

        tong_doanh_thu += gd["thanh_tien"]

    print("-" * 85)
    print(f"TONG DOANH THU: {tong_doanh_thu:,} VND")
    print("=" * 85)


# 9. MENU CHINH
def menu():
    while True:
        print("\n========== QUAN LY SIEU THI MINI ==========")
        print("1. Hien thi danh sach san pham")
        print("2. Xem san pham con hang")
        print("3. Them san pham moi")
        print("4. Nhap them hang")
        print("5. Ban hang")
        print("6. Thong ke doanh thu")
        print("0. Thoat chuong trinh")
        print("===========================================")

        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_san_pham()

        elif lua_chon == "2":
            xem_san_pham_con_hang()

        elif lua_chon == "3":
            them_san_pham()

        elif lua_chon == "4":
            nhap_them_hang()

        elif lua_chon == "5":
            ban_hang()

        elif lua_chon == "6":
            thong_ke_doanh_thu()

        elif lua_chon == "0":
            print("Da thoat chuong trinh.")
            break

        else:
            print("Lua chon khong hop le, vui long nhap lai.")


# CHAY CHUONG TRINH
menu()