import tkinter as tk
from tkinter import filedialog
from tkinter import Image
from PIL import Image, ImageTk
import crypt


class App:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master, borderwidth=5, background='#ffd37a')
        self.frame.pack()

        self.file_path = ""
        self.image_label = tk.Label(self.master)

        self.select_image_button = tk.Button(self.frame, text="Выбрать изображение", command=self.select_image,
                                             bg="#cee007", activebackground="#919e03", borderwidth=5)
        self.select_image_button.pack()

        self.message = tk.StringVar()
        self.message_entry = tk.Entry(self.frame, textvariable=self.message, borderwidth=5)
        self.message_entry.pack()

        self.encrypt_button = tk.Button(self.frame, text="Зашифровать", command=self.encrypt_img)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(self.frame, text="Расшифровать", command=self.decrypt_img)
        self.decrypt_button.pack()

    def select_image(self):
        prev_file = self.file_path
        self.file_path = tk.filedialog.askopenfilename(filetypes=[("BMP", "*.bmp")])
        try:
            self.image = Image.open(self.file_path)
        except Exception:
            return

        if self.file_path != "" and self.file_path != prev_file:
            if self.image_label:
                self.image_label.destroy()

            self.image = Image.open(self.file_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label = tk.Label(self.master, image=self.photo)
            self.image_label.pack()

    def encrypt_img(self):
        if self.file_path != "" and self.message.get() != "":
            self.file_path, code = crypt.encrypt_image(self.file_path, self.message.get())
            if code == 1:
                self.message.set("Unsupported format")
                return
            self.image_label.destroy()
            self.image = Image.open(self.file_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label = tk.Label(self.master, image=self.photo)
            self.image_label.pack()

    def decrypt_img(self):
        if self.file_path != "":
            self.message.set(str(crypt.decrypt_image(self.file_path)))
