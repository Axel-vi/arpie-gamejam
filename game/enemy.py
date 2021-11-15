# Module enemy du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
from pygame import key


if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

# Apparition des astéroides :


class Asteroide:
    def __init__(self):
        speed = randint(6, 10)
        x = width
        y = randint(0, height)
        size = 30
        self.rect = pg.Rect(x, y, size, size)
        self.rect.center = (x+size/2, y+size/2)
        target = randint(0, height)
        coeff = (y-target)/width
        self.speed_x = -(sqrt(1/(1+coeff**2))*speed)
        self.speed_y = coeff*self.speed_x
        l_enemy.append(self)

    def move_rect(self):
        self.rect = pg.Rect.move(self.rect, self.speed_x, self.speed_y)


asteroid = Asteroide()
