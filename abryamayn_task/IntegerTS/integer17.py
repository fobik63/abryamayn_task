try:
    n = int(input())
    res = (n // 100) % 10
    print(res)
except ValueError:
    print("Ошибка: введите целое число")
    