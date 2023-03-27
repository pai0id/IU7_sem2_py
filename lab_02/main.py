from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from matplotlib.figure import Figure
import numpy as np
from tkinter import ttk
import calc
from math import *

root = Tk()
root.title("Метод простых итераций")
root.geometry("1150x700+400+50")
root.resizable(False, False)
root.configure(background='#ffd37a')


def func(x):
    return eval(equation_entry.get())


# Функция для построения графика функции
def plot_function(a, b, step, eps, nmax):
    eeps = 0.001
    code_err_range = 4
    # Вычисление значения функции на сетке узлов
    x = np.linspace(a, b, int((b - a + 1) * 10000))
    y = [func(i) for i in x]
    dy = np.gradient(y, x)
    ddy = np.gradient(dy, x)
    x_for_roots = []
    x_tmp = a
    while x_tmp < b:
        x_for_roots.append(x_tmp)
        x_tmp = float(x_tmp + step)
        if abs(x_tmp) < eeps:
            x_tmp = 0
    x_for_roots.append(b)
    y_for_roots = [func(i) for i in x_for_roots]
    # Вычисление корней, экстремумов и точек перегиба
    roots = []
    results = []
    extremums = []
    inflections = []
    for i in range(1, len(x) - 1):
        if abs(dy[i]) < eeps and (dy[i - 1] * dy[i + 1]) < 0 and abs(dy[i - 1] * dy[i + 1]) < eeps:
            extremums.append((x[i], y[i]))
        if abs(ddy[i]) < eeps and (ddy[i - 1] * ddy[i + 1]) < 0 and abs(ddy[i - 1] * ddy[i + 1]) < eeps:
            inflections.append((x[i], y[i]))
    for i in range(len(x_for_roots) - 1):
        if y_for_roots[i] * y_for_roots[i + 1] > 0:
            results.append((i + 1, f"[{x_for_roots[i]:.5g};{x_for_roots[i + 1]:.5g}]", "-", "-", 0, code_err_range))
        else:
            x_tmp, n, code = calc.fixed_point_iteration(func, x_for_roots[i], x_for_roots[i + 1], eps, nmax)
            if not code:
                y_tmp = func(x_tmp)
                roots.append((x_tmp, y_tmp))
                results.append(
                    (i + 1, f"[{x_for_roots[i]:.5g};{x_for_roots[i+1]:.5g}]", f"{x_tmp:.5g}", f"{y_tmp:.1g}", n, code))
            else:
                results.append((i + 1, f"[{x_for_roots[i]:.5g};{x_for_roots[i + 1]:.5g}]", "-", "-", 0, code))
    ax.plot(x, y, label='f(x)')
    for i in range(len(roots)):
        if i == 0:
            ax.plot(roots[i][0], roots[i][1], 'go', label='Корень')
        else:
            ax.plot(roots[i][0], roots[i][1], 'go')
    for i in range(len(extremums)):
        if i == 0:
            ax.plot(extremums[i][0], extremums[i][1], 'ro', label='Экстремум')
        else:
            ax.plot(extremums[i][0], extremums[i][1], 'ro')
    for i in range(len(inflections)):
        if i == 0:
            ax.plot(inflections[i][0], inflections[i][1], 'bo', label='Точка перегиба')
        else:
            ax.plot(inflections[i][0], inflections[i][1], 'bo')
    ax.legend()
    # Добавляем рисунок на холст
    canvas.draw()

    window = Tk()
    window.title("Report")
    window.geometry("1200x500")
    columns = ("№ корня", "Отрезок", "х'", "f(x')", "Кол-во итераций", "Код ошибки")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=True)
    for head in columns:
        tree.heading(head, text=head, anchor='center')
        tree.column(head, anchor='center')
    for res in results:
        tree.insert("", END, values=res)


# Функция для обработки входных данных
def calculate():
    try:
        func(1)
        a = float(a_entry.get())
        b = float(b_entry.get())
        if b <= a:
            warn.set("b should be > a")
            return -1
        step = float(step_entry.get())
        if step <= 0:
            warn.set("step should be > 0")
            return -1
        eps = float(eps_entry.get())
        if eps <= 0:
            warn.set("eps should be > 0")
            return -1
        nmax = int(nmax_entry.get())
        if nmax <= 0:
            warn.set("nmax should be > 0")
            return -1
    except NameError:
        warn.set("Not a function")
        return -2
    except ValueError:
        warn.set("Incorrect number")
        return -3
    except Exception:
        warn.set("Error")
        return -4
    plot_function(a, b, step, eps, nmax)


# Создание графического интерфейса

equation_label = Label(root, text='Введите функцию f(x):', background='#ffd37a')
equation_label.grid(row=0, column=0, columnspan=3)
equation_entry = Entry(root, width=50, borderwidth=5, background='#c9c9c9', justify='center')
equation_entry.grid(row=1, column=0, columnspan=3)
a_label = Label(root, text='Введите начало отрезка a:', background='#ffd37a')
a_label.grid(row=2, column=0, columnspan=3)
a_entry = Entry(root, width=50, borderwidth=5, background='#c9c9c9', justify='center')
a_entry.grid(row=3, column=0, columnspan=3)
b_label = Label(root, text='Введите конец отрезка b:', background='#ffd37a')
b_label.grid(row=4, column=0, columnspan=3)
b_entry = Entry(root, width=50, borderwidth=5, background='#c9c9c9', justify='center')
b_entry.grid(row=5, column=0, columnspan=3)
step_label = Label(root, text='Введите шаг:', background='#ffd37a')
step_label.grid(row=6, column=0, columnspan=3)
step_entry = Entry(root, width=50, borderwidth=5, background='#c9c9c9', justify='center')
step_entry.grid(row=7, column=0, columnspan=3)
eps_label = Label(root, text='Введите точность eps:', background='#ffd37a')
eps_label.grid(row=8, column=0, columnspan=3)
eps_entry = Entry(root, width=50, borderwidth=5, background='#c9c9c9', justify='center')
eps_entry.grid(row=9, column=0, columnspan=3)
nmax_label = Label(root, text='Введите максимальное число итераций nmax:', background='#ffd37a')
nmax_label.grid(row=10, column=0, columnspan=3)
nmax_entry = Entry(root, width=50, borderwidth=5, background='#c9c9c9', justify='center')
nmax_entry.grid(row=11, column=0, columnspan=3)
calculate_button = Button(root, text='Вычислить', command=calculate, background='#ff8400', borderwidth=3,
                          activebackground='#ba6000')
calculate_button.grid(row=12, column=0, columnspan=3)
warn = StringVar()
warn.set("")
warning = Label(root, textvariable=warn, foreground='red', background='#ffd37a')
warning.grid(row=13, column=0, columnspan=3)
fig = Figure(figsize=(6, 6), dpi=100, facecolor='#c9c9c9')
ax = fig.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=4, columnspan=3, rowspan=12)

root.mainloop()
