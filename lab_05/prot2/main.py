import pygame
import sys
from math import cos, sin


def rotate(base, dot, anglle):
    x1 = (dot[0] - base[0]) * cos(anglle) - (dot[1] - base[1]) * sin(anglle) + base[0]
    y1 = (dot[0] - base[0]) * sin(anglle) + (dot[1] - base[1]) * cos(anglle) + base[1]
    dot[0] = x1
    dot[1] = y1


def draw_tank(base, wheel_ang):
    dot1 = [base[0] - 50, base[1] + 100]
    dot2 = [dot1[0] - 500, dot1[1]]
    dot3 = [dot2[0] - 50, dot2[1] - 100]
    dot4 = [dot3[0] + 100, dot3[1]]
    dot5 = [dot4[0], dot4[1] - 50]
    dot6 = [dot5[0] - 120, dot5[1]]
    dot7 = [dot6[0], dot6[1] - 20]
    dot8 = [dot7[0] + 120, dot7[1]]
    dot9 = [dot8[0], dot8[1] - 80]
    dot10 = [dot9[0] + 300, dot9[1]]
    dot11 = [dot10[0], dot10[1] + 150]
    dot12 = [base[0], base[1]]
    dots = [dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11, dot12]

    pygame.draw.polygon(screen, (180, 255, 0), dots)

    wheel1 = dot1
    wheel2 = [wheel1[0] - 150, wheel1[1]]
    wheel3 = [wheel2[0] - 170, wheel2[1]]
    wheel4 = dot2
    wheels = [wheel1, wheel2, wheel3, wheel4]

    for w in wheels:
        pygame.draw.circle(screen, (0, 0, 0), w, 50)
        tmp_p1 = [w[0] + 20, w[1] + 20]
        tmp_p2 = [w[0] - 20, w[1] + 20]
        rotate(w, tmp_p1, wheel_ang)
        rotate(w, tmp_p2, wheel_ang)
        pygame.draw.circle(screen, (255, 255, 255), tmp_p1, 5)
        pygame.draw.circle(screen, (255, 255, 255), tmp_p2, 5)


pygame.init()

screen_width = 1800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Анимация")

x = 800
y = 400
angle = 0
speed = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x -= speed
    if x < 0:
        x = screen_width

    angle -= 0.01
    if angle > 360:
        angle = 0

    pygame.draw.rect(screen, (255, 255, 255), [[0, 0], [2000, 2000]])
    draw_tank((x, y), angle)

    pygame.display.flip()

    clock.tick(240)
