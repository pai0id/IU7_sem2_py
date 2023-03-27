from tkinter import *
import prot_calc
from math import *

root = Tk()
root.geometry("500x450+400+50")
root.resizable(False, False)


def func(x):
    return eval(equation_entry.get())


# Функция для обработки входных данных
def calculate():
    a = float(a_entry.get())
    b = float(b_entry.get())
    eps = float(eps_entry.get())
    nmax = int(nmax_entry.get())
    got = prot_calc.chord_method(func, a, b, eps, nmax)
    res.set(f"{got:.5g}")


equation_label = Label(root, text='Введите функцию f(x):')
equation_label.pack()
equation_entry = Entry(root, width=50, borderwidth=5, justify='center')
equation_entry.pack()
a_label = Label(root, text='Введите начало отрезка a:')
a_label.pack()
a_entry = Entry(root, width=50, borderwidth=5, justify='center')
a_entry.pack()
b_label = Label(root, text='Введите конец отрезка b:')
b_label.pack()
b_entry = Entry(root, width=50, borderwidth=5, justify='center')
b_entry.pack()
eps_label = Label(root, text='Введите точность eps:')
eps_label.pack()
eps_entry = Entry(root, width=50, borderwidth=5, justify='center')
eps_entry.pack()
nmax_label = Label(root, text='Введите максимальное число итераций nmax:')
nmax_label.pack()
nmax_entry = Entry(root, width=50, borderwidth=5, justify='center')
nmax_entry.pack()
calculate_button = Button(root, text='Вычислить', command=calculate, borderwidth=3,
                          activebackground='#ba6000')
calculate_button.pack()
res = StringVar()
res.set("")
result = Label(root, textvariable=res, background='#ffd37a')
result.pack()

root.mainloop()
