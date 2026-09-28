try:
    a = float(input("Введите число A: "))
    b = float(input("Введите число B (B > A): "))
    n = int(input("Введите целое число N (> 1): "))
    h = (b - a) / n
    print("Длина отрезка H:", h)
    for i in range(n + 1):
        print(a + i * h)
except Exception as e:
    print("Ошибка:", e)