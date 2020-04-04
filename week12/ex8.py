import pygame
import random

pygame.init()

try:
    spritesheet = pygame.image.load("char9.bmp")
except Exception as e:
    print(str(e))

screen = pygame.display.set_mode((800, 600))
spritesheet.convert()
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

screen.blit(background, (0, 0))

lions = []

sz = 128
w, h = 128, 64

for i in range(4):
    lions.append(spritesheet.subsurface((sz * i, 64, w, h)))

for i in range(2):
    lions.append(spritesheet.subsurface((sz * i, 198, w, h)))

for i in range(len(lions)):
    lions[i].set_colorkey((0, 0, 0))

# for i in range(len(lions)):
#     screen.blit(lions[i], (i * (sz + 1), 0))

mainloop = True

FPS = 60
cycletime = 0
interval = 0.05
picnr = 0
clock = pygame.time.Clock()
x = 300
y = 300

while mainloop:
    millis = clock.tick(FPS)
    seconds = millis / 1000.0

    cycletime += seconds
    if cycletime > interval:
        picnr += 1
        if picnr > 5:
            picnr = 0
        cycletime = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            mainloop = False

    screen.fill((255, 255, 255))
    mypicture = lions[picnr]
    screen.blit(mypicture, (x, y))
    x += 2

    if x > screen.get_size()[0]:
        x = 0 - 128
    pygame.display.flip()

