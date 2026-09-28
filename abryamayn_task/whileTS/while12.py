try:
    n = int(input("Введите целое число N (> 1): "))
    k = 0
    s = 0
    while s + (k + 1) <= n:
        k += 1
        s += k
    print("Наибольшее K:", k)
    print("Сумма:", s)
except Exception as e:
    print("Ошибка:", e)