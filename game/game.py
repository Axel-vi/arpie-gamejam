import pygame as pg
from pygame.locals import *
from game.graphics import *
from game.constant import *


def detect_collision(ship, L, maskShip, maskEnemy, foregrnd, maskForegrnd):
    for i in range(len(L)):
        if ship.rect.colliderect(L[i].rect):
            return maskShip.overlap(maskEnemy, (L[i].rect.left - ship.rect.left, L[i].rect.top - ship.rect.top)) != None
    # if ship.rect.colliderect(foregrnd):
    #     print("oui")
    return maskShip.overlap(maskForegrnd, (foregrnd.left - ship.rect.left, foregrnd.top - ship.rect.top)) != None
    # return False
