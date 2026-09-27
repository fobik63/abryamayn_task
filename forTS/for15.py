try:
    a = float(input("Введите вещественное число A: "))
    n = int(input("Введите целое число N (> 0): "))
    res = 1.0
    for _ in range(n):
        res *= a
    print("Результат:", res)
except Exception as e:
    print("Ошибка:", e)