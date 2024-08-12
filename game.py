import pygame
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((500,400))
pygame.display.set_caption("Mi juego")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()