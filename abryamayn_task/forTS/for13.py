try:
    n = int(input("Введите целое число N (> 0): "))
    s = 0.0
    sign = 1.0
    for i in range(1, n + 1):
        s += sign * (1.0 + i * 0.1)
        sign = -sign
    print("Значение выражения:", s)
except Exception as e:
    print("Ошибка:", e)