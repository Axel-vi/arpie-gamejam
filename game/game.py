import pygame as pg
from pygame.locals import *
from game.graphics import *


def detect_collision(ship, L, maskShip, maskAsteroid, maskForegrnd, abs_decor):
    """ Cette fonction detecte les collisions entre des objets. Elle prend en argument :
    \n- ship qui est un objet de la classe "Vaisseau" (doit avoir un attribut '.rect' !)
    \n- L qui est une liste d'ennemis : objets de la classe "Asteroide" (doit avoir un attribut '.rect' !)
    \n- maskShip, maskAsteroid, maskForegrnd, qui sont les mask des images associées (ces objets sont deja crees)
    \n- abs_decor : l'entier relatif qui donne la position du bord de l'image de décor par rapport au bord de la fenetre visible (pour pouvoir gerer le defilement du decor)
    """
    global foregrnd
    for i in range(len(L)):
        if ship.rect.colliderect(L[i].rect):
            return maskShip.overlap(maskAsteroid, (L[i].rect.left - ship.rect.left, L[i].rect.top - ship.rect.top)) != None
    return maskShip.overlap(maskForegrnd, (abs_decor - ship.rect.left, foregrnd.top - ship.rect.top)) != None
