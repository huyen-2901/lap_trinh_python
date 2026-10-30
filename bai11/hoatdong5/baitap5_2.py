import requests

# Gọi API tỷ giá ngoại tệ công khai với đồng tiền cơ sở là USD
response = requests.get("https://open.er-api.com/v6/latest/USD")

# Kiểm tra kết nối thành công
if response.status_code == 200:
    du_lieu = response.json()
    # Lấy tỷ giá quy đổi sang VND từ cấu trúc JSON trả về
    ty_gia_vnd = du_lieu["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Khong lay được ty gia, ma loi:", response.status_code)