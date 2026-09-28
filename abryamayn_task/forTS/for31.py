try:
    n = int(input("Введите целое число N (> 0): "))
    a = 2.0
    for k in range(1, n + 1):
        a = 2.0 + 1.0 / a
        print("A", k, "=", a)
except Exception as e:
    print("Ошибка:", e)