try:
    n = int(input())
    res = (n // 1000) % 10
    print(res)
except ValueError:
    print("Ошибка: введите целое число")