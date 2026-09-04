ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In ra theo tung hang
for hang in ma_tran:
    print(hang)

# In ra tung phan tu, duyat theo hang roi theo cot
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In ra theo tung hang
for hang in ma_tran:
    print(hang)

# In ra tung phan tu, duyat theo hang roi theo cot
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()
# Tính tổng tất cả phần tử trong ma_tran bằng 2 vòng for lồng nhau
tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran += phan_tu

print("Tong tat ca phan tu trong ma tran:", tong_ma_tran)