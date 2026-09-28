try:
    n = int(input("Введите число Фибоначчи N (> 1): "))
    f1, f2 = 1, 1
    while f2 < n:
        f1, f2 = f2, f1 + f2
    print("Предыдущее число Фибоначчи:", f1)
    print("Последующее число Фибоначчи:", f1 + f2)
except Exception as e:
    print("Ошибка:", e)