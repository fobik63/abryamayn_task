try:
    n = int(input("Введите целое положительное число N: "))
    k = int(input("Введите целое положительное число K: "))
    q = 0
    while n >= k:
        n -= k
        q += 1
    print("Частное:", q)
    print("Остаток:", n)
except Exception as e:
    print("Ошибка:", e)