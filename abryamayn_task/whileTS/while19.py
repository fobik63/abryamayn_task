try:
    n = int(input("Введите целое число N (> 0): "))
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    print("Перевернутое число:", rev)
except Exception as e:
    print("Ошибка:", e)