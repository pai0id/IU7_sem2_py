# Функция для вычисления корня методом простых итераций

def fixed_point_iteration(f, a, b, eps, nmax):
    try:
        phi = lambda x: x + f(x)
        x0 = (a + b) / 2
        for n in range(nmax):
            x1 = phi(x0)
            if abs(x1 - x0) < eps:
                if a <= x0 < b:
                    return x0, n, 0
                else:
                    return 0, 0, 3
            x0 = x1
        return 0, 0, 1
    except Exception:
        return 0, 0, 2

