import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

ballsurface = pygame.Surface((50, 50))
ballsurface.set_colorkey((0, 0, 0))
background = pygame.Surface(screen.get_size())

background.fill((255, 255, 255))

pygame.draw.circle(ballsurface, (0, 255, 0), (25, 25), 10)

pygame.draw.rect(background, (45, 100, 34), (200, 200, 50, 80))
pygame.draw.arc(background, (56, 105, 240), (300, 300, 80, 50), 3.14, 6.28)
pygame.draw.polygon(background, (120, 120, 120), [(20, 30), (100, 100), (50, 150)])


screen.blit(background, (0, 0))
screen.blit(ballsurface, (100, 100))

mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            mainloop = False

    pygame.display.flip()

pygame.quit()