import math

try:
    a = float(input("Введите число A: "))
    b = float(input("Введите число B (B > A): "))
    n = int(input("Введите целое число N (> 1): "))
    h = (b - a) / n
    print("Длина отрезка H:", h)
    for i in range(n + 1):
        x = a + i * h
        print("F(", x, ") =", 1 - math.sin(x))
except Exception as e:
    print("Ошибка:", e)