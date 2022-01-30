import pygame
from pygame.draw import *
from random import randint
pygame.init()

x, y, r, score = 0, 0, 0, 0

def main():
    answer = 0
    answer = int(input("1. Рисование кружков мышью" + "\n" +
                        "2. Игра поймай шарик " + "\n" +
                        "Чем хотели бы заняться? "))
    if answer == 1 : 
        drawing_circle_by_mouse()
    elif answer == 2 :
        catch_the_ball()
    else : 
        print("Ошибка! ")

def drawing_circle_by_mouse ():
    FPS = 30
    screen = pygame.display.set_mode((400, 400))

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    circle(screen, RED, event.pos, 30)
                    pygame.display.update()
                elif event.button == 2:
                    circle(screen, GREEN, event.pos, 30)
                    pygame.display.update()
                elif event.button == 3:
                    circle(screen, BLUE, event.pos, 30)
                    pygame.display.update()
                elif event.button == 4:
                    circle(screen, (255, 255, 0), event.pos, 30)
                    pygame.display.update()
                elif event.button == 5:
                    circle(screen, (0, 255, 255), event.pos, 30)
                    pygame.display.update()
    pygame.quit()

def catch_the_ball():
    global score
    FPS = 30
    screen_width = 400
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

    def new_ball(n=1):
        '''drawing n new moving balls '''
        global x, y, r             
        speed_x = randint(-10, 10) / 100
        speed_y = randint(-10, 10) / 100
        for __ in range(n) :
            x = randint(50, screen_width-50)
            y = randint(50, screen_height-50)
            r = randint(10, 60)
            color = COLORS[randint(0, 5)]                
            for __ in range(1000) :
                circle(screen, color, (x, y), r)
                pygame.display.update()
                screen.fill(BLACK)                
                x += speed_x
                if (x > screen_width - r) or (x < r) :
                    speed_x = -speed_x
                y += speed_y
                if (y > screen_height - r) or (y < r) :
                    speed_y = -speed_y

    def click (event) :        
        global x, y, r, score
        if (event.pos[0] - x)**2 + (event.pos[1] - y)**2 < r**2 :
            print("Поймали! ")
            score += 1
            pygame.display.set_caption("Ваш счет= " + str(score))
            x = -1000
        else :
            print("Промах...")

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
        new_ball()
        
    pygame.quit()


#main()
catch_the_ball()