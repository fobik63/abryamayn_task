try:
    n = int(input("Введите целое число N (> 0): "))
    a = 1.0
    for k in range(1, n + 1):
        a = (a + 1.0) / k
        print("A", k, "=", a)
except Exception as e:
    print("Ошибка:", e)