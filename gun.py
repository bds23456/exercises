import numpy as np
from random import choice, randint
import pygame
from color import *

FPS = 30

WIDTH = 800
HEIGHT = 600

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = 40
        self.y = 450
        self.width = 10        
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1
        if event.type == pygame.MOUSEBUTTONDOWN :
            self.power_up()
            self.draw()

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = np.arctan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * np.cos(self.an) / level
        new_ball.vy = - self.f2_power * np.sin(self.an) / level
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
    
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 5
            else :
                self.f2_power = 100
            self.color = RED
        else:
            self.color = GREY

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if pygame.mouse.get_focused():
            mouse_pos = pygame.mouse.get_pos()
            self.set_angle(mouse_pos)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def set_angle(self, target_pos):
        '''Sets gun's direction to target position.'''
        self.an = np.arctan2(target_pos[1] - self.y, target_pos[0] - self.x)

    def draw(self):
        '''Draws the gun on the screen.'''
        gun_shape = []
        vec_1 = np.array([int(7*np.cos(self.an - np.pi/2)), int(7*np.sin(self.an - np.pi/2))])
        vec_2 = np.array([int(2*self.f2_power*np.cos(self.an)), int(2*self.f2_power*np.sin(self.an))])
        gun_pos = np.array([self.x, self.y])
        gun_shape.append((gun_pos + vec_1).tolist())
        gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
        gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
        gun_shape.append((gun_pos - vec_1).tolist())
        pygame.draw.polygon(self.screen, self.color, gun_shape)

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
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        if (self.x > WIDTH - self.r) or (self.x < self.r) :
            self.vx *= -1
            self.live -= 10
        if (self.y > HEIGHT - self.r) or (self.y < self.r) :
            self.vy *= -1
            self.live -= 10

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        a = (obj.x - self.x)**2 + (obj.y - self.y)**2
        if  a < (self.r + obj.r)**2 :
            return True
        else :
            return False

class Target:
    def __init__(self, screen: pygame.Surface) :
        self.screen = screen
        self.x = randint(400, 750)
        self.y = randint(250, 550)
        self.r = randint(5, 50)
        self.color = RED
        self.vx = randint(1, 5)
        self.vy = randint(1, 5)        
        self.live = 1
        self.points = 0
    
    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(400, 750)
        self.y = randint(250, 550)
        self.r = randint(5, 50)
        self.color = RED
        self.vx = randint(1, 5)
        self.vy = randint(1, 5)
        self.live = 1
        self.points = 0

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def move(self):
        """Переместить цель по прошествии единицы времени.

        Метод описывает перемещение цели за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, 
        и стен по краям области движения цели (размер области 400х350).
        """
        self.x += self.vx
        self.y -= self.vy
        if (self.x < 280 + self.r) or (self.x > 800 - self.r) :
            self.vx *= -1
        if (self.y < self.r) or (self.y > 600 - self.r) :
            self.vy *= -1

def score_table() :
    textSurfaceObj1 = fontObj.render("Игра \"Пушка\". ", True, BLACK)
    textSurfaceObj2 = fontObj.render("Сделано выстрелов: " + str(bullet), True, BLACK)
    textSurfaceObj3 = fontObj.render("Попаданий: " + str(all_points), True, BLACK)
    textSurfaceObj4 = fontObj.render("Счет: " + str(all_points - bullet), True, BLACK)
    screen.blit(textSurfaceObj1, [30, 30])
    screen.blit(textSurfaceObj2, [30, 60])
    screen.blit(textSurfaceObj3, [30, 90])
    screen.blit(textSurfaceObj4, [30, 120])

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра \"Пушка\" ")
clock = pygame.time.Clock()
fontObj = pygame.font.Font(None, 30)

bullet = 0
all_points = 0
level = 6
balls = []
targets = []
gun = Gun(screen)
for i in range(level) :
    targets.append(Target(screen))
finished = False


while not finished:
    screen.fill(WHITE)
    score_table()
    gun.draw()
    for t in targets :
        t.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    gun.power_up()
    for t in targets:
        t.move()
        for b in balls:
            b.move()
            if b.live < 0:
                balls.remove(b)
            if b.hittest(t) and t.live:
                t.live = 0
                t.hit()
                all_points += t.points
                t.new_target()                

pygame.quit()