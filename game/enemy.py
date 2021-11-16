# Module enemy du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
import pygame as pg
from pygame import key


if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *


class Asteroide:
    """Definition de la classe qui va servir a creer les asteroides et gerer leurs comportements"""

    def __init__(self):
        """Initialisation"""
        self.speed = randint(6, 10)
        self.x = width
        self.y = randint(0, height)
        self.size = 90
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)
        self.rect.center = (self.x+self.size/2, self.y+self.size/2)
        self.target = randint(0, height)
        self.coeff = (self.y-self.target)/width
        self.speed_x = -(sqrt(1/(1+self.coeff**2))*self.speed)
        self.speed_y = self.coeff*self.speed_x
        l_enemy.append(self)

    def move_rect(self):
        """Fonction qui met un asteroid en mouvement"""
        self.rect = pg.Rect.move(self.rect, self.speed_x, self.speed_y)


# Initialisation d'un objet de la classe Asteroid + creation du mask des asteroid

# Cette ligne est a priori temporaire et devra etre retirer lorsque les asteroides seront vraiment implementes
asteroid = Asteroide()

# maskAsteroid = pg.mask.from_surface(pg.transform.scale(
#     image["asteroide"].convert_alpha(), (90, 90)))
