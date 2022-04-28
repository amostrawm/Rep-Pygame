import pygame
from random import randint
import time

pygame.init()

screen = pygame.display.set_mode((500, 500))
running = True

x = 100
y = 100
collor1 = randint(1, 255)
collor2 = randint(1, 255)
collor3 = randint(1, 255)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((255, 255, 255))

    while y <= 501:
        pygame.draw.circle(screen, (collor1, collor2, collor3), (x, y), 30)
        pygame.display.flip()
        collor1 = randint(1, 255)
        collor2 = randint(1, 255)
        collor3 = randint(1, 255)
        y = y + 1
        screen.fill((255, 255, 255))
        time.sleep(0.0005)
        if y == 470:
            x = x + 50
            y = 100

        if x >= 500:
            pygame.quit()