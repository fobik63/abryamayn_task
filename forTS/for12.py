try:
    n = int(input("Введите целое число N (> 0): "))
    p = 1.0
    for i in range(1, n + 1):
        p *= (1.0 + i * 0.1)
    print("Произведение:", p)
except Exception as e:
    print("Ошибка:", e)