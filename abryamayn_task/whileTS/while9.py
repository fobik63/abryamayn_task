try:
    n = int(input("Введите целое число N (> 1): "))
    k = 1
    p = 3
    while p <= n:
        p *= 3
        k += 1
    print("Наименьшее K:", k)
except Exception as e:
    print("Ошибка:", e)