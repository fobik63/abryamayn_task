try:
    a = float(input("Введите положительное число A: "))
    b = float(input("Введите положительное число B (B < A): "))
    while a >= b:
        a -= b
    print("Длина незанятой части:", a)
except Exception as e:
    print("Ошибка:", e)