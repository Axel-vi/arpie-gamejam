import pygame as pg
from pygame.locals import *
from game.constant import *
from game.graphics import *


def detect_collision(ship, L, maskShip, maskEnemy):
    for i in range(len(L)):
        if ship.rect.colliderect(L[i].rect):
            return maskShip.overlap(maskEnemy, (L[i].rect.left - ship.rect.left, L[i].rect.top - ship.rect.top)) != None

    return False
