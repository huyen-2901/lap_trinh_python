import requests
response = requests.get("https://api.github.com/repos/python/cpython")

# Kiểm tra nếu kết nối thành công (mã trạng thái 200)
if response.status_code == 200:
    du_lieu = response.json()
    print("Ten repository:", du_lieu["full_name"])
    print("So luot gan sao (stars):", du_lieu["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu["language"])
else:
    print("Goi API that bai, ma loi:", response.status_code)