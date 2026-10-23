import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()

        duong_dan = os.path.join(
            os.path.dirname(__file__),
            "form_dang_nhap.ui"
        )

        uic.loadUi(duong_dan, self)

        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Lỗi", "Vui lòng nhập đầy đủ tài khoản và mật khẩu!")
        elif tai_khoan == "huyen" and mat_khau == "123456":
            QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
        else:
            QMessageBox.critical(self, "Lỗi", "Sai tài khoản hoặc mật khẩu!")


app = QApplication(sys.argv)
cua_so = CuaSoDangNhap()
cua_so.show()
sys.exit(app.exec_())