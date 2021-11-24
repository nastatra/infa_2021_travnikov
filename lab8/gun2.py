import math
from random import choice
from random import randint
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.gy = 2
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= self.gy / 2
        self.x += self.vx
        self.y -= self.vy
        if self.x - self.r <= 0 or self.x + self.r >= WIDTH:
            self.x -= self.vx
            self.vx = -0.7 * self.vx
            self.vy = 0.7 * self.vy
        elif self.y - self.r <= 0 or self.y + self.r >= HEIGHT:
            self.y += self.vy
            self.vy = -0.7 * self.vy
            self.vx = 0.7 * self.vx

    def stop(self):
        if self.vx * self.vx + self.vy * self.vy < 0.2:
            return True
        else:
            return False

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
#        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r, width = 1)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x) * (self.x - obj.x) + (self.y - obj.y) *
                   (self.y - obj.y)) <= (self.r + obj.r) * (self.r + obj.r):
            return True
        else:
            return False

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """Рисует пушку. Направление зависит от прицеливания."""
        x0 = 40
        y0 = 450
        length_scale = 2
        width = 8
        x0l = x0 - width / 2 * math.sin(self.an)
        x0r = x0 + width / 2 * math.sin(self.an)
        y0l = y0 + width / 2 * math.cos(self.an)
        y0r = y0 - width / 2 * math.cos(self.an)
        x_end = x0 + length_scale * self.f2_power * math.cos(self.an)
        y_end = y0 + length_scale * self.f2_power * math.sin(self.an)
        x1l = x_end - width / 2 * math.sin(self.an)
        x1r = x_end + width / 2 * math.sin(self.an)
        y1l = y_end + width / 2 * math.cos(self.an)
        y1r = y_end - width / 2 * math.cos(self.an)
        pygame.draw.polygon(self.screen, self.color, [[x0l, y0l], [x0r, y0r], [x1r, y1r], [x1l, y1l]])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.live = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        r = self.r = randint(2, 50)
        x = self.x = randint(WIDTH * 0.5, WIDTH - r)
        y = self.y = randint(HEIGHT * 0.3, HEIGHT - r)
        self.vx = randint(-1, 1)
        self.vy = randint(-1, 1)
        color = self.color = choice(GAME_COLORS) #RED
        self.live = 1

    def move(self):
        """ Переместить цель по прошествии единицы времени. """
        self.x += self.vx
        self.y -= self.vy
        if self.x - self.r <= 0 or self.x + self.r >= WIDTH:
            self.x -= self.vx
            self.vx = - self.vx
            self.vy = self.vy
        elif self.y - self.r <= 0 or self.y + self.r >= HEIGHT:
            self.y += self.vy
            self.vy = - self.vy
            self.vx = self.vx

    def hit(self):
        """Попадание шарика в цель."""
        global points
        points += 1

    def draw(self):
        """Рисование цели."""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r, width = 3)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
points = 0
balls = []
targets = []

clock = pygame.time.Clock()
gun = Gun(screen)
for t in range(3):
    target = Target(screen)
    targets.append(target)
finished = False

string1 = 'Целей подбито:  ' + str(0)
string2 = ''
while not finished:
    screen.fill(WHITE)
    gun.draw()
    for t in targets:
        t.move()
        t.draw()
    for b in balls:
        b.draw()

    font = pygame.font.Font(None, 22)
    text1 = font.render(string1, True, BLACK)
    screen.blit(text1, (20, 20))

    font = pygame.font.Font(None, 28)
    text2 = font.render(string2, True, BLACK)
    screen.blit(text2, (250, 100))

    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            string2 = ''
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        for t in targets:
            if b.hittest(t) and t.live:
                t.live = 0
                t.hit()

                string1 = 'Целей подбито:  ' + str(points)

                if bullet < 1:
                    shut = ' выстрелов'
                elif bullet == 1:
                    shut = ' выстрел'
                elif bullet <= 4:
                    shut = ' выстрела'
                else:
                    shut = ' выстрелов'
                string2 = 'Вы поразили цель за ' + str(bullet) + shut

                t.new_target()
                bullet = 0

        if b.stop():
            balls.remove(b)

    gun.power_up()

pygame.quit()