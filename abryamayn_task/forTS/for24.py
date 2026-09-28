try:
    x = float(input("Введите вещественное число X: "))
    n = int(input("Введите целое число N (> 0): "))
    s = 1.0
    term = 1.0
    for i in range(1, n + 1):
        term *= -x * x / ((2 * i - 1) * (2 * i))
        s += term
    print("Значение cos(X):", s)
except Exception as e:
    print("Ошибка:", e)