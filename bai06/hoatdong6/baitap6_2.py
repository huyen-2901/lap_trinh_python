def fibonacci_de_quy(n):
    if n <= 1:  # dieu kien dung
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

# In 10 số Fibonacci đầu tiên
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()