try:
    n = int(input("Введите целое число N (> 1): "))
    f1, f2 = 1, 1
    while f2 <= n:
        f1, f2 = f2, f1 + f2
    print("Первое число Фибоначчи > N:", f2)
except Exception as e:
    print("Ошибка:", e)