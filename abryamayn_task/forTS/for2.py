try:
    a = int(input("Введите A: "))
    b = int(input("Введите B (A < B): "))

    count = 0
    for i in range(a, b + 1):
        print(i)
        count += 1

    print("Количество чисел N:", count)

except ValueError:
    print("Ошибка: введите целые числа!")