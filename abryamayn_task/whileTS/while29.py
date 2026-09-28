try:
    eps = float(input("Введите вещественное число eps (> 0): "))
    k = 3
    a1 = 1.0
    a2 = 2.0
    ak = (a1 + 2 * a2) / 3
    while abs(ak - a2) >= eps:
        a1 = a2
        a2 = ak
        ak = (a1 + 2 * a2) / 3
        k += 1
    print("Номер K:", k)
    print("A(K-1):", a2)
    print("A(K):", ak)
except Exception as e:
    print("Ошибка:", e)