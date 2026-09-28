try:
    n = int(input("Введите целое число N (> 0): "))
    s = 0.0
    for i in range(1, n + 1):
        s += float(i) ** i
    print("Сумма:", s)
except Exception as e:
    print("Ошибка:", e)