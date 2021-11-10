import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 20
scrn_length = 800
scrn_width = 600
screen = pygame.display.set_mode((scrn_length, scrn_width))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    ''' Рисует новый шарик '''

    global x, y, dx, dy, r, color, angle
    r = randint(10, 100)
    x = randint(r, scrn_length - r)
    y = randint(r, scrn_width - r)
    color = COLORS[randint(0, 5)]
    angle = randint(0, 360)
    dx = step * np.cos(angle * np.pi / 180)
    dy = -step * np.sin(angle * np.pi / 180)
    circle(screen, color, (x, y), r)

def move_ball():
    ''' Двигает шарик с отражением от стенок на случайный угол '''

    global x, y, dx, dy, r, angle, step

    if x - r + dx <= 0:
        angle = randint(-90, 90)
    elif x + r + dx >= scrn_length:
        angle = randint(90, 270)
    elif y - r + dy <= 0:
        angle = randint(180, 360)
    elif y + r + dy >= scrn_width:
        angle = randint(0, 180)
    dx = step * np.cos(angle * np.pi / 180)
    dy = -step * np.sin(angle * np.pi / 180)
    x += dx
    y += dy

    screen.fill(WHITE)
    circle(screen, color, (x, y), r)

def click(event):
    ''' Обрабатывает клики мыши '''

    x_click = event.pos[0]
    y_click = event.pos[1]
    counting(x_click, y_click)

def counting(x_click, y_click):
    ''' Подсчитывает очки при попаданию по шарику.
    При поадании старый шарик стирается, рисуется новый'''

    global score

    if ((x - x_click) * (x - x_click) + (y - y_click) * (y - y_click)) <= r * r:
        score += 1
        print(score)
        screen.fill(WHITE)
        new_ball()


score = 0
step = 5      # Шаг при движении шарика
screen.fill(WHITE)
new_ball()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    move_ball()
    pygame.display.update()

pygame.quit()