import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((550, 650))
#Drawing house
rect(screen, (255, 0, 255), (50, 400, 200, 200))
rect(screen, (0, 0, 255), (50, 400, 200, 200), 5)
polygon(screen, (55, 255, 200), [(50,400), (150,350),
                               (250,400), (50,400)])
polygon(screen, (0, 0, 255), [(50,400), (150,350),
                               (250,400), (50,400)], 5)
circle(screen, (0, 255, 0), (150, 475), 50)
circle(screen, (255, 255, 255), (150, 475), 50, 5)

#Drawing shaded square 
x1 = 300; y1 = 400
x2 = 500; y2 = 600
N = 8
color = (255, 255, 255)
rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N)
x = x1 
y = y1
for i in range(N): #hatching
    line(screen, color, (x, y1), (x, y2))
    line(screen, color, (x1, y), (x2, y))
    x += h
    y += h

#Drawing angry smail 
a = 220
b = 155 
circle(screen, (255, 255, 0), (a+50, a-50), b) #head
rect(screen, (0, 0, 0), (a-40, a+20, 175, 35)) #mouth

#eyes
circle(screen, (255, 0, 0), (a-10, a-80), 32)
circle(screen, (0, 0, 0), (a-10, a-80), 16)
circle(screen, (255, 0, 0), (a+110, a-80), 28)
circle(screen, (0, 0, 0), (a+110, a-80), 14)

#brows
polygon(screen, (0, 0, 0), [(a-53,a-147), (a-45,a-160), (a+30,a-90)])
polygon(screen, (0, 0, 0), [(a+40,a-105), (a-45,a-160), (a+30,a-90)])
polygon(screen, (0, 0, 0), [(a+55,a-100), (a+65,a-85), (a+130,a-145)])
polygon(screen, (0, 0, 0), [(a+140,a-130), (a+65,a-85), (a+130,a-145)])                             


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()