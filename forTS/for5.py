try:
    price = float(input("Введите цену 1 кг конфет: "))
    for i in range(1, 11):
        w = i / 10
        print(round(w, 1), "кг:", w * price)
except Exception as e:
    print("Ошибка:", e)