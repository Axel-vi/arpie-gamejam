import pygame as pg
from pygame.locals import *
from game.graphics import *
from game.constant import *


def detect_collision(ship, L, maskShip, maskEnemy, maskForegrnd, abs_decor):
    global foregrnd
    for i in range(len(L)):
        if ship.rect.colliderect(L[i].rect):
            return maskShip.overlap(maskEnemy, (L[i].rect.left - ship.rect.left, L[i].rect.top - ship.rect.top)) != None
    return maskShip.overlap(maskForegrnd, (abs_decor - ship.rect.left, foregrnd.top - ship.rect.top)) != None
