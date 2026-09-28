try:
    p = float(input("Введите процент P (0 < P < 25): "))
    s = 1000.0
    k = 0
    while s <= 1100:
        s += s * p / 100
        k += 1
    print("Количество месяцев K:", k)
    print("Итоговый размер вклада S:", s)
except Exception as e:
    print("Ошибка:", e)