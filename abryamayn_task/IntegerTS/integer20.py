try:
    n = int(input())
    res = (n // 3600)
    print(res)
except ValueError:
    print("Ошибка: введите целое число")
    