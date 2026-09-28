try:
    a = float(input("Введите положительное число A: "))
    b = float(input("Введите положительное число B (B < A): "))
    count = 0
    while a >= b:
        a -= b
        count += 1
    print("Количество отрезков B:", count)
except Exception as e:
    print("Ошибка:", e)