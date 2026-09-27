try:
    a = float(input("Введите вещественное число A: "))
    n = int(input("Введите целое число N (> 0): "))
    p = 1.0
    for _ in range(n):
        p *= a
        print(p)
except Exception as e:
    print("Ошибка:", e)