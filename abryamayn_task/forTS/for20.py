try:
    n = int(input("Введите целое число N (> 0): "))
    s = 0.0
    f = 1.0
    for i in range(1, n + 1):
        f *= i
        s += f
    print("Сумма факториалов:", s)
except Exception as e:
    print("Ошибка:", e)