try:
    a = float(input("Введите положительное число A: "))
    b = float(input("Введите положительное число B: "))
    c = float(input("Введите положительное число C: "))
    count_a = 0
    temp_a = a
    while temp_a >= c:
        temp_a -= c
        count_a += 1
    count_b = 0
    temp_b = b
    while temp_b >= c:
        temp_b -= c
        count_b += 1
    total = 0
    for _ in range(count_b):
        total += count_a
    print("Количество квадратов:", total)
except Exception as e:
    print("Ошибка:", e)