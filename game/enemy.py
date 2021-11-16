# Module enemy du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
from pygame import key


if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *


class Asteroide:
    """Definition de la classe qui va servir a creer les asteroides et gerer leurs comportements"""

    def __init__(self):
        """Initialisation"""
        speed = randint(6, 10)
        x = width
        y = randint(0, height)
        size = 90
        self.rect = pg.Rect(x, y, size, size)
        self.rect.center = (x+size/2, y+size/2)
        target = randint(0, height)
        coeff = (y-target)/width
        self.speed_x = -(sqrt(1/(1+coeff**2))*speed)
        self.speed_y = coeff*self.speed_x
        l_enemy.append(self)

    def move_rect(self):
        """Fonction qui met un asteroid en mouvement"""
        self.rect = pg.Rect.move(self.rect, self.speed_x, self.speed_y)


# Initialisation d'un objet de la classe Asteroid + creation du mask des asteroid

# Cette ligne est a priori temporaire et devra etre retirer lorsque les asteroides seront vraiment implementes
asteroid = Asteroide()

maskAsteroid = pg.mask.from_surface(pg.transform.scale(
    image["asteroide"].convert_alpha(), (90, 90)))
