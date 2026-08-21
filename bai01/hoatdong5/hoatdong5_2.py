diem = 6.5
tuoi = 20

ket_qua_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm đạt loại Khá:", ket_qua_kha)  


ket_qua_tuoi = (tuoi < 18) or (tuoi > 60)
print("Chưa đủ 18 hoặc trên 60 tuổi:", ket_qua_tuoi)  


print("Phủ định điều kiện điểm Khá:", not ket_qua_kha)   
print("Phủ định điều kiện tuổi:", not ket_qua_tuoi)      