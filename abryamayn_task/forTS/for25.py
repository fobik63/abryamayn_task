try:
    x = float(input("Введите вещественное число X (|X| < 1): "))
    n = int(input("Введите целое число N (> 0): "))
    s = 0.0
    p = 1.0
    sign = 1.0
    for i in range(1, n + 1):
        p *= x
        s += sign * p / i
        sign = -sign
    print("Значение ln(1 + X):", s)
except Exception as e:
    print("Ошибка:", e)