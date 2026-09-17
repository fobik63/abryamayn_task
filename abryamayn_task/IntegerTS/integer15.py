try:
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    res = b * 100 + a * 10 + c
    print(res)
except ValueError:
    print("Ошибка: введите целое число")
    