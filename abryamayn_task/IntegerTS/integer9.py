try:
    n = int(input())
    print(n // 100)
except ValueError:
    print("Ошибка: введите целое число")