try:
    n = int(input("Введите целое число N (степень 2): "))
    k = 0
    while n > 1:
        n //= 2
        k += 1
    print("Показатель степени K:", k)
except Exception as e:
    print("Ошибка:", e)