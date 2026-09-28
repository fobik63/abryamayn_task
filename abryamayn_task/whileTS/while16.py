try:
    p = float(input("Введите процент P (0 < P < 50): "))
    day_dist = 10.0
    total = 10.0
    k = 1
    while total <= 200:
        day_dist += day_dist * p / 100
        total += day_dist
        k += 1
    print("Количество дней K:", k)
    print("Суммарный пробег S:", total)
except Exception as e:
    print("Ошибка:", e)