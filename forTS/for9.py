try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B (B > A): "))
    s = 0
    for i in range(a, b + 1):
        s += i ** 2
    print("Сумма квадратов:", s)
except Exception as e:
    print("Ошибка:", e)