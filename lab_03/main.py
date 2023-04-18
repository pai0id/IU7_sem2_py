import tkinter as tk
import GUI

root = tk.Tk()
root.title("Криптография")
root.configure(background='#ffd37a')
root.minsize(300, 300)
copy_right = tk.Label(text="Поляков Андрей ИУ7-22Б", background='#ffd37a', foreground="grey")
copy_right.pack(anchor="n")
app = GUI.App(root)
root.mainloop()
