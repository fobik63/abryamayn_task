try:
    x = float(input("Введите вещественное число X: "))
    n = int(input("Введите целое число N (> 0): "))
    s = x
    term = x
    for i in range(1, n + 1):
        term *= -x * x / ((2 * i) * (2 * i + 1))
        s += term
    print("Значение sin(X):", s)
except Exception as e:
    print("Ошибка:", e)