try:
    n = int(input("Введите целое число N (> 0): "))
    k = 1
    while k * k <= n:
        k += 1
    print("Наименьшее K:", k)
except Exception as e:
    print("Ошибка:", e)