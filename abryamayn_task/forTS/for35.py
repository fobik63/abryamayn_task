try:
    n = int(input("Введите целое число N (> 2): "))
    a1 = 1
    a2 = 2
    a3 = 3
    print("A 1 =", a1)
    print("A 2 =", a2)
    print("A 3 =", a3)
    for k in range(4, n + 1):
        ak = a3 + a2 - 2 * a1
        print("A", k, "=", ak)
        a1 = a2
        a2 = a3
        a3 = ak
except Exception as e:
    print("Ошибка:", e)