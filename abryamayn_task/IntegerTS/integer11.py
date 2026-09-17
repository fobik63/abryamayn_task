try:
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("Сумма:", a + b + c)
    print("Произведение:", a * b * c)
except ValueError:
    print("Ошибка: введите целое число")