try:
    n = int(input("Введите целое число N (> 0): "))
    res = 1.0
    while n > 0:
        res *= n
        n -= 2
    print("Двойной факториал N!!:", res)
except Exception as e:
    print("Ошибка:", e)