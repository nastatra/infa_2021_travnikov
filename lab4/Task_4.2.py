import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 500))

# Sky
rect(screen, (102, 255, 255), (0, 0, 700, 500))
# Ground
rect(screen, (51, 204, 51), (0, 250, 700, 250))


# House
def plot_house(X, Y, scale):
    rect(screen, (204, 153, 0), (X - 90 * scale, Y - 70 * scale, 180 * scale, 140 * scale))
    rect(screen, (0, 0, 0), (X - 90 * scale, Y - 70 * scale, 180 * scale, 140 * scale), 2)

    rect(screen, (51, 204, 204), (X - 25 * scale, Y - 20 * scale, 50 * scale, 40 * scale))
    rect(screen, (255, 102, 0), (X - 25 * scale, Y - 20 * scale, 50 * scale, 40 * scale), 2)

    polygon(screen, (204, 0, 0),
            [(X - 90 * scale, Y - 70 * scale), (X + 90 * scale, Y - 70 * scale), (X, Y - 160 * scale)])
    polygon(screen, (0, 0, 0),
            [(X - 90 * scale, Y - 70 * scale), (X + 90 * scale, Y - 70 * scale), (X, Y - 160 * scale)], 2)


# Tree
def plot_tree(X, Y, scale):
    rect(screen, (0, 0, 0), (X - 8 * scale, Y - 90 * scale, 16 * scale, 90 * scale))

    circle(screen, (51, 102, 0), (X, Y - 170 * scale), 30 * scale)
    circle(screen, (0, 0, 0), (X, Y - 170 * scale), 30 * scale, 2)

    circle(screen, (51, 102, 0), (X - 35 * scale, Y - 140 * scale), 30 * scale)
    circle(screen, (0, 0, 0), (X - 35 * scale, Y - 140 * scale), 30 * scale, 2)

    circle(screen, (51, 102, 0), (X + 35 * scale, Y - 140 * scale), 30 * scale)
    circle(screen, (0, 0, 0), (X + 35 * scale, Y - 140 * scale), 30 * scale, 2)

    circle(screen, (51, 102, 0), (X, Y - 125 * scale), 30 * scale)
    circle(screen, (0, 0, 0), (X, Y - 125 * scale), 30 * scale, 2)

    circle(screen, (51, 102, 0), (X + 25 * scale, Y - 103 * scale), 30 * scale)
    circle(screen, (0, 0, 0), (X + 25 * scale, Y - 103 * scale), 30 * scale, 2)

    circle(screen, (51, 102, 0), (X - 25 * scale, Y - 105 * scale), 30 * scale)
    circle(screen, (0, 0, 0), (X - 25 * scale, Y - 105 * scale), 30 * scale, 2)


# Cloud
def plot_cloud(X, Y, scale):
    circle(screen, (255, 255, 255), (X, Y), 30 * scale)
    circle(screen, (0, 0, 0), (X, Y), 30 * scale, 2)

    circle(screen, (255, 255, 255), (X + 30 * scale, Y), 30 * scale)
    circle(screen, (0, 0, 0), (X + 30 * scale, Y), 30 * scale, 2)

    circle(screen, (255, 255, 255), (X + 60 * scale, Y), 30 * scale)
    circle(screen, (0, 0, 0), (X + 60 * scale, Y), 30 * scale, 2)

    circle(screen, (255, 255, 255), (X + 90 * scale, Y), 30 * scale)
    circle(screen, (0, 0, 0), (X + 90 * scale, Y), 30 * scale, 2)

    circle(screen, (255, 255, 255), (X + 65 * scale, Y - 20 * scale), 30 * scale)
    circle(screen, (0, 0, 0), (X + 65 * scale, Y - 20 * scale), 30 * scale, 2)

    circle(screen, (255, 255, 255), (X + 25 * scale, Y - 20 * scale), 30 * scale)
    circle(screen, (0, 0, 0), (X + 25 * scale, Y - 20 * scale), 30 * scale, 2)


# Sun
def plot_sun(X, Y, scale):
    R = 40    # Radius
    N = 20    # Number of rays
    d = 5     # Ray length

    rays = []
    sign = 1
    for i in range(2 * N):
        x1 = R * np.sin(2 * np.pi / (2 * N) * i) * scale + X
        y1 = R * np.cos(2 * np.pi / (2 * N) * i) * scale + Y
        rays.append((x1, y1))
        sign *= (-1)
        R += d * sign

    polygon(screen, (255, 255, 0), rays)
    polygon(screen, (0, 0, 0), rays, 2)


plot_house(190, 265, 1)
plot_tree(520, 300, 1)
plot_cloud(330, 100, 1)
plot_sun(620, 80, 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()