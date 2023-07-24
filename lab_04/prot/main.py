import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Округлы....")
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
labl = tk.Label(text="Радиус:")
labl.pack()
entr = tk.Entry()
entr.pack()

circles = []

prev = (0, 0, 0)


def draw_circle(x, y, radius, color):
    x0 = x - radius
    y0 = y - radius
    x1 = x + radius
    y1 = y + radius
    canvas.create_oval(x0, y0, x1, y1, outline=color, width=5)


def find_largest_intersecting_circle():
    max_intersect_count = 0
    largest_intersect_circle = None

    for circle in circles:
        intersect_count = 0

        for other_circle in circles:
            if circle != other_circle:
                distance = ((circle[0] - other_circle[0]) ** 2 + (circle[1] - other_circle[1]) ** 2) ** 0.5
                if distance < circle[2] + other_circle[2]:
                    intersect_count += 1

        if intersect_count > max_intersect_count:
            max_intersect_count = intersect_count
            largest_intersect_circle = circle

    return largest_intersect_circle


def highlight_largest_intersect_circle():
    global prev
    largest_circle = find_largest_intersecting_circle()
    if largest_circle:
        if prev[2] != 0:
            draw_circle(prev[0], prev[1], prev[2], "blue")
        x, y, radius, color = largest_circle
        draw_circle(x, y, radius, "green")
        prev = (x, y, radius)


def add_circle(event):
    x = event.x
    y = event.y
    color = "blue"
    draw_circle(x, y, int(entr.get()), color)
    circles.append((x, y, int(entr.get()), color))
    highlight_largest_intersect_circle()


canvas.bind("<Button-1>", add_circle)

root.mainloop()
