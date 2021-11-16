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
        speed = randint(6, 10)
        x = width
        y = randint(0, height)
        size = 90
        self.type='asteroide'
        self.rect = pg.Rect(x, y, size, size)
        self.rect.center = (x+size/2, y+size/2)
        target = randint(0, height)
        coeff = (y-target)/width
        self.speed_x = -(sqrt(1/(1+coeff**2))*speed)
        self.speed_y = coeff*self.speed_x
        l_enemy.append(self)

    def move(self):
        self.rect = pg.Rect.move(self.rect, self.speed_x, self.speed_y)

class tir_enemy:
    def __init__(self, x, y):

        self.rect = pg.Rect(x, y,larg_tir, long_tir)
        self.duree = duree_tir
        l_tir_enemy.append(self)

    def move(self):
        self.rect = pg.Rect.move(self.rect,speed_tir_enemy,0)

    def update_duree(self):
        self.duree -= 1
        if self.duree <= 0:
            l_tir_enemy.pop(0)



class Chromius_fighter():
    def __init__(self):
        self.size=90
        #Apparition aléatoire à gauche de l'écran
        x=width
        y=randint(0,int((5/6)*height))

        self.type='chromius fighter'
        self.cooldown=0
        self.rect = pg.Rect(x,y, self.size, self.size)
        self.rect.center = (x+self.size/2,y+self.size/2)
        print('ok')
        l_enemy.append(self)
    def move(self):
        #Mouvement vers la droite uniquement horizontal
        self.rect = pg.Rect.move(self.rect,-10,0)
    def creer_tir_enemy(self):
        #creer un tir à la position du vaisseau ennemi
        if self.cooldown>0:
            self.cooldown-=1
        else:
            self.cooldown=delai_tir_enemy
            tir_enemy(self.rect.left-self.size/2, self.rect.top+self.size/2)
    
def spawn_chromius_fighter():
    #Fait apparaitre un chromius fighter toute les 120 frames
    global delai_spawn_enemy
    if delai_spawn_enemy>0:
        delai_spawn_enemy-=1
    else:
        Chromius_fighter()
        delai_spawn_enemy=120

# Initialisation d'un objet de la classe Asteroid + creation du mask des asteroid

# Cette ligne est a priori temporaire et devra etre retirer lorsque les asteroides seront vraiment implementes
asteroid = Asteroide()
maskEnemy = pg.mask.from_surface(pg.transform.scale(
    image["asteroide"].convert_alpha(), (90, 90)))

