x = 10
x += 5     # x = 15
print("Sau x += 5:", x)

x -= 3     # x = 12
print("Sau x -= 3:", x)

x *= 2     # x = 24
print("Sau x *= 2:", x)

x /= 4     # x = 6.0
print("Sau x /= 4:", x)

x //= 2    # x = 3.0
print("Sau x //= 2:", x)

x **= 3    # x = 27.0
print("Sau x **= 3:", x)
# Kiểm tra phần tử trong list bằng 'in'
danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?:", 3 in danh_sach)  # True

# So sánh 2 biến cùng tham chiếu tới 1 list bằng 'is'
list_a = [1, 2, 3]
list_b = list_a  
print("list_a và list_b cùng tham chiếu?:", list_a is list_b)  