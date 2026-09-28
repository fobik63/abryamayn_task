try:
    n = int(input("Введите целое число N (> 0): "))
    temp = n
    while temp > 1 and temp % 3 == 0:
        temp //= 3
    print(temp == 1)
except Exception as e:
    print("Ошибка:", e)