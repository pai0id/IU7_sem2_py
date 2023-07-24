import pygame
import sys
from math import cos, sin


def draw_cloud(scr, x, y):
    pygame.draw.circle(scr, (255, 255, 255), (x - 70, y), 60)
    pygame.draw.circle(scr, (255, 255, 255), (x + 70, y), 60)
    pygame.draw.circle(scr, (255, 255, 255), (x, y), 70)


pygame.init()

screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Анимация")

background_image = pygame.image.load("background0.png")

animation_set = [pygame.image.load(f"{i}.png") for i in range(1, 11)]

x_link = 0
y_link = 800
angle_link = 0

y_clouds = 90
x_cloud1 = 400
x_cloud2 = 900
x_cloud3 = 1500

sun_cords = (1800, 90)
angle_rays = 0

sprite_speed = 10
cloud_speed = 3

clock = pygame.time.Clock()

i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x_link += sprite_speed
    x_cloud1 += cloud_speed
    x_cloud2 += cloud_speed
    x_cloud3 += cloud_speed

    angle_rays += 1

    if angle_rays >= 30:
        angle_rays = 0

    if x_cloud1 > screen_width:
        x_cloud1 = 0
    if x_cloud2 > screen_width:
        x_cloud2 = 0
    if x_cloud3 > screen_width:
        x_cloud3 = 0

    if x_link > screen_width:
        x_link = 0
        y_link = 800

    if 800 <= x_link < 1000:
        angle_link -= 18
        y_link -= 5

    screen.blit(background_image, (0, 0))

    pygame.draw.circle(screen, (255, 255, 0), sun_cords, 100)

    rotated_sprite = pygame.transform.rotate(animation_set[i // 10], angle_link)

    screen.blit(rotated_sprite, (x_link, y_link))

    for j in range(12):
        a_new = j * 30 + angle_rays
        x_st_new = cos(a_new) - 120 * sin(a_new) + sun_cords[0]
        y_st_new = sin(a_new) + 120 * cos(a_new) + sun_cords[1]
        x_ed_new = cos(a_new) - 170 * sin(a_new) + sun_cords[0]
        y_ed_new = sin(a_new) + 170 * cos(a_new) + sun_cords[1]
        pygame.draw.line(screen, (255, 255, 0), (x_st_new, y_st_new), (x_ed_new, y_ed_new), 5)

    draw_cloud(screen, x_cloud1, y_clouds)
    draw_cloud(screen, x_cloud2, y_clouds)
    draw_cloud(screen, x_cloud3, y_clouds)

    i += 1
    if i == 60:
        i = 0

    pygame.display.flip()

    clock.tick(240)
