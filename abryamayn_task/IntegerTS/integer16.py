try:
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    res = a * 100 + c * 10 + b
    print(res)
except ValueError:
    print("Ошибка: введите целое число")