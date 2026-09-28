try:
    n = int(input("Введите целое число N (> 1): "))
    k = 0
    s = 0
    while s < n:
        k += 1
        s += k
    print("Наименьшее K:", k)
    print("Сумма:", s)
except Exception as e:
    print("Ошибка:", e)