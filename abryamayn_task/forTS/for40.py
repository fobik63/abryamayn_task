try:
    a = int(input("Введите целое число A: "))
    b = int(input("Введите целое число B (B > A): "))
    count = 1
    for i in range(a, b + 1):
        for _ in range(count):
            print(i)
        count += 1
except Exception as e:
    print("Ошибка:", e)