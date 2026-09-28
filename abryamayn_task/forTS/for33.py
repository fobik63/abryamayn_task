try:
    n = int(input("Введите целое число N (> 1): "))
    f1 = 1
    f2 = 1
    print("F 1 =", f1)
    print("F 2 =", f2)
    for k in range(3, n + 1):
        f3 = f1 + f2
        print("F", k, "=", f3)
        f1 = f2
        f2 = f3
except Exception as e:
    print("Ошибка:", e)