try:
    n = int(input("Введите целое число N (> 0): "))
    f = 1.0
    for i in range(1, n + 1):
        f *= i
    print("Факториал N!:", f)
except Exception as e:
    print("Ошибка:", e)