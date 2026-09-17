try:
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    res = c * 100 + b * 10 + a
    print(res)
except ValueError:
    print("Ошибка: введите целое число")