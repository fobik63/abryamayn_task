try:
    n = int(input("Введите целое число N (> 1): "))
    a1 = 1.0
    a2 = 2.0
    print("A 1 =", a1)
    print("A 2 =", a2)
    for k in range(3, n + 1):
        a3 = (a1 + 2 * a2) / 3
        print("A", k, "=", a3)
        a1 = a2
        a2 = a3
except Exception as e:
    print("Ошибка:", e)