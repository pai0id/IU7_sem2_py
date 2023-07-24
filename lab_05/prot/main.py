import pygame
import sys
from math import cos, sin, pi


def rotate(base, dot, anglle):
    x1 = (dot[0] - base[0]) * cos(anglle) - (dot[1] - base[1]) * sin(anglle) + base[0]
    y1 = (dot[0] - base[0]) * sin(anglle) + (dot[1] - base[1]) * cos(anglle) + base[1]
    dot[0] = x1
    dot[1] = y1


def draw_tri(x1, y1, angle1):
    base = (x1, y1)
    dot1 = [x1, y1 + 75]
    dot2 = [x1 + 50, y1 - 50]
    dot3 = [x1 - 50, y1 - 50]

    rotate((x1, y1), dot1, angle1)
    rotate((x1, y1), dot2, angle1)
    rotate((x1, y1), dot3, angle1)

    pygame.draw.polygon(screen, (180, 0, 0), [dot1, dot2, base])
    pygame.draw.polygon(screen, (0, 180, 0), [base, dot3, dot1])
    pygame.draw.polygon(screen, (0, 0, 180), [dot3, dot2, base])


pygame.init()

screen_width = 1600
screen_height = 1600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Анимация")

base = [600, 800]

angle = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, (255, 255, 255), [[0, 0], [2000, 2000]])

    angle += pi / 18

    draw_tri(base[0], base[1], angle)

    rotate([800, 800], base, pi / 36)

    pygame.display.flip()

    clock.tick(24)
