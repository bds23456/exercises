import math
from random import choice
from random import randint
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
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0]-40 == 0 :
                self.an = 45
            else :
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-40))
                self.rotate(self.an)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.polygon(self.screen, 
                            self.color, 
                            [(self.x + self.f2_power, self.y + self.f2_power), 
                            (self.x, self.y),
                            (self.x + 20, self.y),
                            (self.x + 20 + self.f2_power, self.y + self.f2_power)]) 

        # FIXIT don't know how to do it
    def rotate(self, angle):        
        angle = (180 / math.pi) * -angle
        self.image = pygame.transform.rotate(self.screen, int(angle))
        self.polygon = self.image.get_rect(center=(self.x , self.y))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 2
            self.color = RED
        else:
            self.color = GREY

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
        self.r = 17
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
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(5, 50)
        self.color = RED
        self.live = 1
        self.points = 0
    
    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.color = RED
        self.live = 1

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

def text() :
    textSurfaceObj1 = fontObj.render("Игра \"Пушка\". ", True, BLACK)
    textSurfaceObj2 = fontObj.render("Сделано выстрелов: " + str(bullet), True, BLACK)
    textSurfaceObj3 = fontObj.render("Попаданий: " + str(target.points), True, BLACK)
    textSurfaceObj4 = fontObj.render("Счет: " + str(target.points - bullet), True, BLACK)
    screen.blit(textSurfaceObj1, [30, 30])
    screen.blit(textSurfaceObj2, [30, 60])
    screen.blit(textSurfaceObj3, [30, 90])
    screen.blit(textSurfaceObj4, [30, 120])

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра \"Пушка\" ")
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False
fontObj = pygame.font.Font(None, 30)

while not finished:
    screen.fill(WHITE)
    text()
    gun.draw()
    target.draw()
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

    for b in balls:
        b.move()
        if b.live < 0:
            balls.remove(b)
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()

pygame.quit()
