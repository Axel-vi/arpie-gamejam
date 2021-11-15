import pygame as pg
from pygame.locals import *


def detect_collision(ship, L):
    for i in range(len(L)):
        if ship.rect.colliderect(L[i].rect):
            mask_ship = pg.mask.from_surface(ship.rect)
            mask_enemy = pg.mask.from_surface(L[i].rect)
            if mask_ship.overlap(mask_enemy, (L[i].rect.left - ship.rect.left, L[i].rect.top - ship.rect.top)) != None:
                return True
    return False
