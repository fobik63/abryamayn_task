try:
    a = float(input("Введите вещественное число A: "))
    n = int(input("Введите целое число N (> 0): "))
    s = 1.0
    p = 1.0
    for _ in range(n):
        p *= a
        s += p
    print("Сумма:", s)
except Exception as e:
    print("Ошибка:", e)