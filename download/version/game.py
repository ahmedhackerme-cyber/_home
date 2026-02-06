import pygame

pygame.init()

p = pygame.display.set_mode((800,500))
title = pygame.display.set_caption("Game Ahmed")

fps = pygame.time.Clock()

while True:

    fps.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
