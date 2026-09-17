try:
    n = int(input())
    units = n % 10
    tens = (n // 10) % 10
    print(units, tens)
except ValueError:
    print("Ошибка: Введите целое число")