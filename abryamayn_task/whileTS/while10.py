try:
    n = int(input("Введите целое число N (> 1): "))
    k = 0
    p = 1
    while p * 3 < n:
        p *= 3
        k += 1
    print("Наибольшее K:", k)
except Exception as e:
    print("Ошибка:", e)