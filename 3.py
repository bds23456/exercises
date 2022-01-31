import pygame
from pygame.draw import *
from random import randint
pygame.init()

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
    FPS = 40
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
             
    def hit(x, y, r, x_mouse, y_mouse) :
        if (x_mouse - x)**2 + (y_mouse - y)**2 < r**2 :
            return True
        else :
            return False

    def click (event) :  
        global ball, score
        if hit(ball[0], ball[1], ball[2], event.pos[0], event.pos[1]) :
            print("Поймали! ")
            score += 1 
            pygame.display.set_caption("Ваш счет= " + str(score))
            ball = new_ball()
        else :
            print("Промах...")     
        
    def new_ball():
        return [randint(50, screen_width-50),     #x
                randint(50, screen_height-50),    #y
                randint(20, 50),                  #r
                randint(-10, 10),                 #Vx
                randint(-10, 10),                 #Vy
                COLORS[randint(0, 5)]]            #color

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    global score 
    score = 0
    global ball
    ball = new_ball()  
    
    while not finished:
        clock.tick(FPS)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)                
        screen.fill(BLACK)
        circle(screen, ball[5], (ball[0], ball[1]), ball[2])  
        pygame.display.update()          
        ball[0] += ball[3]
        ball[1] += ball[4]
        if (ball[0] > screen_width - ball[2]) or (ball[0] < ball[2]) :
            ball[3] *= -1                
        if (ball[1] > screen_height - ball[2]) or (ball[1] < ball[2]) :
            ball[4] *= -1    
    pygame.quit()

main()