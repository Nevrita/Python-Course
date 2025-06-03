import pygame
import math

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Moving and Color Changing Sprites")

sprite1 = pygame.Surface((50, 50))
sprite2 = pygame.Surface((50, 50))

x1, x2 = 50, 150
angle = 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += 0.05
    color1 = (
        int((math.sin(angle) + 1) * 127),
        0,
        int((math.cos(angle) + 1) * 127)
    )
    color2 = (
        0,
        int((math.sin(angle + math.pi/2) + 1) * 127),
        int((math.cos(angle + math.pi/2) + 1) * 127)
    )

    sprite1.fill(color1)
    sprite2.fill(color2)

    x1 += 1
    x2 += 1

    if x1 > 350:
        x1 = 0
    if x2 > 350:
        x2 = 0

    screen.fill((255, 255, 255))
    screen.blit(sprite1, (x1, 100))
    screen.blit(sprite2, (x2, 150))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()