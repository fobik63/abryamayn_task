try:
    n = int(input())
    a = n // 100
    bc = n % 100
    res = bc * 10 + a
    print(res)
except ValueError:
    print("Ошибка: введите целое число")