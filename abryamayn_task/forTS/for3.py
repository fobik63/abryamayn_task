try:
    a = int(input("Введите число A: "))
    b = int(input("Введите число B (B > A): "))
    count = 0
    for i in range(b - 1, a, -1):
        print(i)
        count += 1
    print("N =", count)
except Exception as e:
    print("Ошибка:", e)