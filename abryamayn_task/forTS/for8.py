try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B (B > A): "))
    p = 1
    for i in range(a, b + 1):
        p *= i
    print("Произведение:", p)
except Exception as e:
    print("Ошибка:", e)