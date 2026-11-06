
import sqlite3

TEN_FILE_CSDL = "chi_tieu.db"


# Kết nối cơ sở dữ liệu
def ket_noi_csdl():
    ket_noi = sqlite3.connect(TEN_FILE_CSDL)
    return ket_noi


# Tạo bảng giao dịch nếu chưa tồn tại
def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS giao_dich (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ngay TEXT NOT NULL,
            ten_giao_dich TEXT NOT NULL,
            loai TEXT NOT NULL,
            so_tien REAL NOT NULL,
            danh_muc TEXT NOT NULL,
            ghi_chu TEXT
        )
    """)

    ket_noi.commit()
    ket_noi.close()


# Thêm giao dịch
def them_giao_dich(ngay, ten_giao_dich, loai, so_tien, danh_muc, ghi_chu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        INSERT INTO giao_dich
        (ngay, ten_giao_dich, loai, so_tien, danh_muc, ghi_chu)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (ngay, ten_giao_dich, loai, so_tien, danh_muc, ghi_chu))

    ket_noi.commit()
    ket_noi.close()


# Lấy toàn bộ giao dịch
def lay_toan_bo_giao_dich():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT * FROM giao_dich
        ORDER BY ngay DESC, id DESC
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua


# Xóa giao dịch
def xoa_giao_dich(id_giao_dich):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute(
        "DELETE FROM giao_dich WHERE id = ?",
        (id_giao_dich,)
    )

    ket_noi.commit()
    ket_noi.close()


# Thống kê tổng thu và tổng chi
def thong_ke_thu_chi():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT loai, SUM(so_tien)
        FROM giao_dich
        GROUP BY loai
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua


# Thống kê chi tiêu theo danh mục
def thong_ke_theo_danh_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()

    con_tro.execute("""
        SELECT danh_muc, SUM(so_tien)
        FROM giao_dich
        WHERE loai = 'Chi'
        GROUP BY danh_muc
    """)

    ket_qua = con_tro.fetchall()
    ket_noi.close()

    return ket_qua
