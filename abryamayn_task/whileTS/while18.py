try:
    n = int(input("Введите целое число N (> 0): "))
    count = 0
    s = 0
    while n > 0:
        digit = n % 10
        s += digit
        count += 1
        n //= 10
    print("Количество цифр:", count)
    print("Сумма цифр:", s)
except Exception as e:
    print("Ошибка:", e)