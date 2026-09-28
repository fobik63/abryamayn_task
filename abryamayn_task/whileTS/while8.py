try:
    n = int(input("Введите целое число N (> 0): "))
    k = 1
    while (k + 1) * (k + 1) <= n:
        k += 1
    print("Наибольшее K:", k)
except Exception as e:
    print("Ошибка:", e)