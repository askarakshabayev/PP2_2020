import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))


ballsurface = pygame.Surface((50, 50))
ballsurface.set_colorkey((0, 0, 0))

pygame.draw.circle(ballsurface, (255, 0, 0), (25, 25), 20, 2) # R G B

screen.blit(background, (0, 0))
screen.blit(ballsurface, (40, 240))

color1 = 0
color2 = 0

running = True

t = 0  # pattern

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.draw.line(screen, (255 - color1, 0, 0), (32 * t, 0), (0, 480 - 24 * t))
    pygame.draw.line(screen, (0, 255 - color2, 0), (32 * t, 480), (640, (480 - 24 * t)))

    screen.blit(ballsurface, (240, 40))
    t = t + 1
    if t > 20:
        t = 0
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
    pygame.display.flip()

pygame.quit()
