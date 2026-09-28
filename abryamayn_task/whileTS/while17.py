try:
    n = int(input("Введите целое число N (> 0): "))
    while n > 0:
        print(n % 10)
        n //= 10
except Exception as e:
    print("Ошибка:", e)