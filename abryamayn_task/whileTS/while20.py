try:
    n = int(input("Введите целое число N (> 0): "))
    found = False
    while n > 0:
        if n % 10 == 2:
            found = True
            break
        n //= 10
    print(found)
except Exception as e:
    print("Ошибка:", e)