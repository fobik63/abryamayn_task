try:
    price = float(input("Введите цену 1 кг конфет: "))
    for i in range(12, 21, 2):
        w = i / 10
        print(w, "кг:", w * price)
except Exception as e:
    print("Ошибка:", e)