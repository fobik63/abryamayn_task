try:
    n = int(input("Введите целое число N (> 0): "))
    s = 0
    for i in range(1, n + 1):
        s += (2 * i - 1)
        print("Текущий квадрат:", s)
except Exception as e:
    print("Ошибка:", e)