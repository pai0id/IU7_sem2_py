# Найти треугольник, для которого разность площадей,
# образованных делением одной из биссектрис минимальна

import tkinter as tk
import app

root = tk.Tk()
root.title("Треуглы...")
root.configure(background='#ffd37a')
copy_right = tk.Label(text="Поляков Андрей ИУ7-22Б", background='#ffd37a', foreground="grey")
copy_right.pack(anchor="n")
app = app.TriangleApp(root)
root.mainloop()
