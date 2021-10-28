import pygame
from pygame.draw import *
from math import sin, pi, cos

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
CYAN =  (128, 166, 255)
YELLOW = (255, 255, 0)
BROWN = (150, 75, 0)
BEJEV = (245, 245, 220)
ORANGE = (255, 128, 0)

def main():
    build_picture()
def build_picture():
    surroundings()
    beach()
    ship()
    umbrella()
    clouds()
    clouds2()
    clouds3()
    ship2()
    umbrella2()
def surroundings():
    rect(screen, CYAN, (0, 0, 600, 186))
    rect(screen, BLUE, (0, 186, 600, 92))
    rect(screen, YELLOW, (0, 278, 600, 122))
    circle(screen, YELLOW, (537, 55), 40)
def beach():
    for i in range(1,10):
        ellipse(screen, YELLOW, (60*(2*i-2),270.5,60,15))
        ellipse(screen, BLUE, (60*(2*i -1),270.5,60,15))
def ship():
    circle(screen, BROWN,(352, 205), 30, width = 0, draw_top_right= False, draw_top_left= False, draw_bottom_left= True)
    rect(screen, BROWN, (352, 205, 143, 30))
    polygon(screen, BROWN, [[495, 205], [559, 205], [495, 235]])
    rect(screen, BLACK, (410, 110, 7, 95))
    polygon(screen, BEJEV, [[417, 110], [477, 157.5], [437, 157.5]])
    polygon(screen, BEJEV, [[477, 157.5], [437, 157.5], [417, 205]])
    polygon(screen, BLACK, [[417, 110], [477, 157.5], [437, 157.5]], width = 1)
    polygon(screen, BLACK, [[477, 157.5], [437, 157.5], [417, 205]], width = 1)
    circle(screen, BLACK, (510, 215), 8)
    circle(screen, WHITE, (510, 215), 5)
    line(screen, BLACK, (352, 205), (352, 235))
    line(screen, BLACK, (495, 205), (495, 235))
def umbrella():
    rect(screen, ORANGE, (92, 235, 7, 150))
    polygon(screen, RED, [[27, 265], [164, 265],[92, 235],[99,235]])
    rect(screen, RED, (92, 235, 7, 30))
    rect(screen, BROWN, (92, 235, 7, 31), width = 1)
    line(screen, BLACK, (352, 205), (352, 235))
    line(screen, BLACK, (495, 205), (495, 235))
    line(screen, BLACK, (92, 238), (45, 265))
    line(screen, BLACK, (92, 238), (65, 265))
    line(screen, BLACK, (92, 238), (80, 265))
    line(screen, BLACK, (99, 238), (111, 265))
    line(screen, BLACK, (99, 238), (131, 265))
    line(screen, BLACK, (99, 238), (151, 265))
def clouds():
    circle(screen, WHITE, (130, 45), 13)
    circle(screen, BLACK, (130, 45), 13, width = 1)
    circle(screen, WHITE, (146, 45), 13)
    circle(screen, BLACK, (146, 45), 13, width = 1)
    circle(screen, WHITE, (118, 60), 13)
    circle(screen, BLACK, (118, 60), 13, width = 1)
    circle(screen, WHITE, (135, 60), 13)
    circle(screen, BLACK, (135, 60), 13, width = 1)
    circle(screen, WHITE, (153, 60), 13)
    circle(screen, BLACK, (153, 60), 13, width = 1)
    circle(screen, WHITE, (166, 45), 13)
    circle(screen, BLACK, (166, 45), 13, width = 1)
    circle(screen, WHITE, (171, 60), 13)
    circle(screen, BLACK, (171, 60), 13, width = 1)
def clouds2():
    for k in range(1, 4):
        circle(screen, WHITE, (240 + 20 * (2 * k - 1), 45),25)
        circle(screen, BLACK, (240 + 20 * (2 * k - 1), 45), 25, width = 1)
        circle(screen, WHITE, (215 + 20 * (2 * k - 1), 60), 25)
        circle(screen, BLACK, (215 + 20 * (2 * k - 1), 60), 25, width = 1)
        if k == 3:
            circle(screen, WHITE, (215 + 20 * (2 * k - 1), 60), 25)
            circle(screen, BLACK, (215 + 20 * (2 * k - 1), 60), 25, width = 1)
def clouds3():
    for j in range(1, 4):
        circle(screen, WHITE, (70 + 20 * (2 * j - 1), 130), 30)
        circle(screen, BLACK, (70 + 20 * (2 * j - 1), 130), 30, width = 1)
        circle(screen, WHITE, (50 + 20 * (2 * j - 1), 145), 30)
        circle(screen, BLACK, (50 + 20 * (2 * j - 1), 145), 30, width = 1)
        if j == 3:
            circle(screen, WHITE, (50 + 20 * (2 * j - 1), 145), 30)
            circle(screen, BLACK, (50 + 20 * (2 * j - 1), 145), 30, width = 1)
def ship2():
    circle(screen, BROWN,(175, 200), 10, width = 0, draw_top_right= False, draw_top_left= False, draw_bottom_left= True)
    rect(screen, BROWN, (175, 200, 45, 10))
    line(screen, BLACK, (175, 200), (175, 210))
    polygon(screen, BROWN, [[220, 200], [240, 200], [220, 209]])
    line(screen, BLACK, (220, 200), (220, 210))
    rect(screen, BLACK, (187.7, 169, 2.3, 31))
    polygon(screen, BEJEV, [[190, 169], [195, 184.5], [205, 184.5]])
    polygon(screen, BEJEV, [[190, 200], [195, 184.5], [205, 184.5]])
    polygon(screen, BLACK, [[190, 169], [195, 184.5], [205, 184.5]], width = 1)
    polygon(screen, BLACK, [[190, 200], [195, 184.5], [205, 184.5]], width = 1)
    circle(screen, BLACK, (226.5, 203), 3.5)
    circle(screen, WHITE, (226.5, 203), 2)

def umbrella2():
    rect(screen, ORANGE, (250, 275, 3.5, 75))
    polygon(screen, RED, [[250, 275], [253.5, 275],[225, 285],[278.5,285]])
    rect(screen, BROWN, (250, 275, 3.9, 12), width = 1)
    line(screen, BLACK, (250, 278), (230, 285))
    line(screen, BLACK, (250, 278), (238, 285))
    line(screen, BLACK, (250, 278), (245, 285))
    line(screen, BLACK, (253.5, 278), (257, 285))
    line(screen, BLACK, (253.5, 278), (265, 285))
    line(screen, BLACK, (253.5, 278), (272, 285))
def sunbeams():
    r = 40
    n = 40
    alpha = ((n - 2)/ n) * pi
    x = 2 * r * sin(pi / n)
    a = 537
    b = 15
    for i in range(1, n):
        polygon(screen, YELLOW, [[a, b], [a + cos((pi - alpha) / 2) * x, b + sin((pi - alpha) / 2) * x], [a + cos((pi - alpha) / 2) * x, b - sin((pi - alpha) / 2) * x]])
        a += sin((pi - alpha) / 2) * x
        b += cos((pi - alpha) / 2) * x


main()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()