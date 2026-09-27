try:
    k = int(input("Введите целое число K: "))
    n = int(input("Введите целое число N (N > 0): "))

    for i in range(n):
         print(k)

except ValueError:
    print("Ошибка: введено не целое число")