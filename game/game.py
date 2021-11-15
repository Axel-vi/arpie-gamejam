import pygame as pg
from pygame.locals import *


def detect_collision(ship, L):
    for i in range(len(L)):
        if ship.colliderect(L[i]):
            mask_ship = pg.mask.from_surface(ship)
            mask_enemy = pg.mask.from_surface(L[i])
            if mask_ship.overlap(mask_enemy, (L[i].left - ship.left, L[i].top - ship.top)) != None:
                return True
    return False
