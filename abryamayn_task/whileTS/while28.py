try:
    eps = float(input("Введите вещественное число eps (> 0): "))
    k = 2
    a_prev = 2.0
    a_curr = 2.0 + 1.0 / a_prev
    while abs(a_curr - a_prev) >= eps:
        a_prev = a_curr
        a_curr = 2.0 + 1.0 / a_prev
        k += 1
    print("Номер K:", k)
    print("A(K-1):", a_prev)
    print("A(K):", a_curr)
except Exception as e:
    print("Ошибка:", e)