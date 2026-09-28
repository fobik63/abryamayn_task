try:
    a = int(input("Введите положительное число A: "))
    b = int(input("Введите положительное число B: "))
    while b != 0:
        a, b = b, a % b
    print("НОД:", a)
except Exception as e:
    print("Ошибка:", e)