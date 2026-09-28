try:
    a = float(input("Введите число A (> 1): "))
    k = 0
    s = 0.0
    while s <= a:
        k += 1
        s += 1 / k
    print("Наименьшее K:", k)
    print("Сумма:", s)
except Exception as e:
    print("Ошибка:", e)