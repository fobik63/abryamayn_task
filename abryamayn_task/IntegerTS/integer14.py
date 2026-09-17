try:
    n = int(input())
    ab = n // 10
    c = n % 10
    res = c * 100 + ab
    print(res)
except ValueError:
    print("Ошибка: введите целое число")