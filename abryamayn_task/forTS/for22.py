try:
    x = float(input("Введите вещественное число X: "))
    n = int(input("Введите целое число N (> 0): "))
    s = 1.0
    term = 1.0
    for i in range(1, n + 1):
        term *= x / i
        s += term
    print("Значение exp(X):", s)
except Exception as e:
    print("Ошибка:", e)