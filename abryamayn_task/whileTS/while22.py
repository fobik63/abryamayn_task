try:
    n = int(input("Введите целое число N (> 1): "))
    is_prime = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            is_prime = False
            break
        d += 1
    print(is_prime)
except Exception as e:
    print("Ошибка:", e)