import pygame
running = True
x = 125
y = 250


class Screen:
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.draw.circle(screen, (255, 255, 255), (250, 250), 30)
    pygame.display.flip()


class DrawCircle:
    def __init__(self, x, y):
        screen = Screen.screen
        self.x = x
        self.y = y
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 30)
        pygame.display.flip()


def fill():
    screen = Screen.screen
    screen.fill((255, 255, 255))


while running:
    Screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    DrawCircle(x, y)






