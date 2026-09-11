sinh_vien = {
"ho_ten": "Nguyen Van A",
"nam_sinh": 2004,
"diem_tb": 8.5
}
print(sinh_vien["ho_ten"]) # truy xuat theo khoa
print(sinh_vien.get("diem_tb")) # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co")) # get() voi gia tri mac dinh neu khong co khoa