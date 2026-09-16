n = int(input("Введите двузначное число: "))
tens = n // 10
units = n % 10
digit_sum = tens + units
digit_mult = tens * units
print("Сумма цифр:", digit_sum)
print("Произведение цифр:", digit_mult)