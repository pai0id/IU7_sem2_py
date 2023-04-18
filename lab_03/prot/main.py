import tkinter as tk
from tkinter import filedialog
from tkinter import Image
from PIL import Image, ImageDraw, ImageTk


class App:
    def __init__(self, master):
        self.master = master

        self.file_path = ""
        self.image_label = tk.Label(self.master)

        self.select_image_button = tk.Button(text="Выбрать изображение", command=self.select_image,
                                             bg="#cee007", activebackground="#919e03", borderwidth=5)
        self.select_image_button.pack()

        self.jail_button = tk.Button(text="За решетку!", command=self.jail_img)
        self.jail_button.pack()

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

    def jail_img(self):
        if self.file_path != "":
            image = Image.open(self.file_path)
            pixels = image.load()
            width, height = image.size
            cnt = 0
            for row in range(3, height - 3):
                for col in range(3, width - 3):
                    if (col - cnt) % 50 == 0:
                        pixels[col, row] = (0, 0, 0)
                    elif (col + cnt) % 50 == 0:
                        pixels[col, row] = (0, 0, 0)
                cnt += 1

            self.file_path = f"{self.file_path.rstrip('.bmp').rstrip('_enc')}_enc.bmp"
            image.save(self.file_path)
            
            self.image_label.destroy()
            self.image = Image.open(self.file_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label = tk.Label(self.master, image=self.photo)
            self.image_label.pack()


root = tk.Tk()
root.title("Кот")
app = App(root)
root.mainloop()
