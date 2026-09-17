try:
    n = int(input())
    res = (n // 60)
    print(res)
except ValueError:
    print("Ошибка: введите целое число")