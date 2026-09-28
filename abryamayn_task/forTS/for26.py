try:
    x = float(input("Введите вещественное число X (|X| < 1): "))
    n = int(input("Введите целое число N (> 0): "))
    s = x
    term = x
    for i in range(1, n + 1):
        term *= -x * x
        s += term / (2 * i + 1)
    print("Значение arctg(X):", s)
except Exception as e:
    print("Ошибка:", e)