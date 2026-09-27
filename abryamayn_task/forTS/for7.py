try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B (B > A): "))
    s = 0
    for i in range(a, b + 1):
        s += i
    print("Сумма:", s)
except Exception as e:
    print("Ошибка:", e)