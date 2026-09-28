try:
    n = int(input("Введите число Фибоначчи N (> 1): "))
    f1, f2 = 1, 1
    k = 2
    while f2 < n:
        f1, f2 = f2, f1 + f2
        k += 1
    print("Порядковый номер K:", k)
except Exception as e:
    print("Ошибка:", e)