try:
    a = int(input("Введите целое число A: "))
    b = int(input("Введите целое число B (B > A): "))
    for i in range(a, b + 1):
        for _ in range(i):
            print(i)
except Exception as e:
    print("Ошибка:", e)