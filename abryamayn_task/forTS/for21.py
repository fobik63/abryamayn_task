try:
    n = int(input("Введите целое число N (> 0): "))
    s = 1.0
    f = 1.0
    for i in range(1, n + 1):
        f *= i
        s += 1.0 / f
    print("Приближенное значение e:", s)
except Exception as e:
    print("Ошибка:", e)