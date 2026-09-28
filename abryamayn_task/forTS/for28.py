try:
    x = float(input("Введите вещественное число X (|X| < 1): "))
    n = int(input("Введите целое число N (> 0): "))
    s = 1.0
    term = 1.0
    for i in range(1, n + 1):
        term *= -1 * (2 * i - 3) * x / (2 * i)
        s += term
    print("Значение sqrt(1 + X):", s)
except Exception as e:
    print("Ошибка:", e)