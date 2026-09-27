try:
    n = int(input("Введите целое число N (> 0): "))
    s = 0
    for i in range(n, 2 * n + 1):
        s += i ** 2
    print("Сумма:", s)
except Exception as e:
    print("Ошибка:", e)