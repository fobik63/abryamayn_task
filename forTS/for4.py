try:
    price = float(input("Введите цену 1 кг конфет: "))
    for i in range(1, 11):
        print(i, "кг:", i * price)
except Exception as e:
    print("Ошибка:", e)