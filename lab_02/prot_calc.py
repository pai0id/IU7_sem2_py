# Функция для вычисления корня методом хорд
def chord_method(func, a, b, eps, nmax):
    n = 0
    c1 = a
    while n < nmax:
        y_a = func(a)
        y_b = func(b)
        c2 = a - (y_a * (a - b)) / (y_a - y_b)
        y_c = func(c2)
        if abs(c1 - c2) < eps:
            return c2
        if (y_a < 0 < y_c) or (y_a > 0 > y_c):
            b = c2
        else:
            a = c2
        c1 = c2
        n += 1
    return c1
