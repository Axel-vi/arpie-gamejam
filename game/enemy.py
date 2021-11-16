# Module enemy du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
from pygame import key


if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

# Apparition des astéroides :


def apparition(v):
    # Renvoie un quadruplet (x,y,vx,vy) qui serviront à faire apparaître l'astéroide
    x = width
    y = randint(0, height)
    target = randint(0, height)
    coeff = (y-target)/width
    vx = -(sqrt(1/(1+coeff**2))*v)
    # vx_approx=int(vx)
    vy = coeff*vx
    # vy_approx=int(vy)
    return (x, y, vx, vy)


class Asteroide:
    def __init__(self):
        # Renvoie un quadruplet (x,y,vx,vy) qui serviront à faire apparaître l'astéroide
        v = randint(6, 10)
        x = width
        y = randint(0, height)
        size_x = 30  # A adapter---------------------------
        size_y = 30
        self.rect = pg.Rect(x, y, size_x, size_y)
        self.rect.center = (x+size_x/2, y+size_y/2)
        target = randint(0, height)
        coeff = (y-target)/width
        vx = -(sqrt(1/(1+coeff**2))*v)
        vy = coeff*vx
        # self.x=x
        # self.y=y
        self.speed_x = vx
        self.speed_y = vy
        l_enemy.append(self)

    def move_rect(self):
        self.rect = pg.Rect.move(self.rect, self.speed_x, self.speed_y)


class Chromius_fighter:
    def __init__(self, pattern, id, nb):
        self.pattern = pattern
        # self.id
        self.size = 75
        if pattern == 1:
            y = play_height/nb
            self.rect = pg.Rect(width, y, self.size, self.size)
