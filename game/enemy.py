# Module enemy du projet R-Type
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *


class Asteroide:
    """Definition de la classe qui va servir a creer les asteroides et gerer leurs comportements"""

    def __init__(self):
        """Initialisation"""
        speed = randint(6, 10)
        y = randint(0, play_height)
        self.size = asteroid_size
        self.rect = pg.Rect(width, y, self.size, self.size)
        #self.rect.center = (width+self.size/2, y+self.size/2)
        target = randint(0, play_height)
        coeff = (y-target)/width
        self.type = 'asteroide'
        self.speed_x = -(sqrt(1/(1+coeff**2))*speed)
        self.speed_y = coeff*self.speed_x
        l_enemy.append(self)

    def move(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)

    def shoot(self):
        """Un asteroide ne tire pas"""


class tir_enemy:
    def __init__(self, x, y):
        """Initialisation"""
        self.rect = pg.Rect(x, y, tir_size, tir_size)
        self.duree = duree_tir
        l_tir_enemy.append(self)

    def move(self):
        self.rect = self.rect.move(speed_tir_enemy, 0)

    def update_duree(self):
        self.duree -= 1
        if self.duree <= 0:
            l_tir_enemy.pop(0)


class Chromius_fighter():
    def __init__(self):
        self.size = scale_size
        # Apparition aléatoire à gauche de l'écran
        x = width
        y = randint(0, int((5/6)*height))
        self.type = 'chromius_fighter'
        self.cooldown = 0
        self.rect = pg.Rect(x, y, self.size, self.size)
        #self.rect.center = (x+self.size/2, y+self.size/2)
        l_enemy.append(self)

    def move(self):
        # Mouvement vers la droite uniquement horizontal
        self.rect = self.rect.move(-10, 0)

    def shoot(self):
        # creer un tir à la position du vaisseau ennemi
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.cooldown = delai_tir_enemy
            tir_enemy(self.rect.left+self.size/5, self.rect.top+self.size/3)


class missile_enemy:
    def __init__(self, x, y):
        """Initialisation"""
        self.rect = pg.Rect(x, y, tir_size, tir_size)
        self.duree = duree_tir
        l_missile_enemy.append(self)

    def move(self):
        # à changer pour que le missile suive le personnage
        self.rect = self.rect.move(speed_missile_enemy, 0)

    def update_duree(self):
        self.duree -= 1
        if self.duree <= 0:
            l_missile_enemy.pop(0)


class Chromius_warrior():
    def __init__(self):
        self.size = scale_size
        # Apparition aléatoire à gauche de l'écran
        x = width
        y = randint(0, int((5/6)*height))
        self.type = 'chromius_warrior'
        self.cooldown = 0
        self.rect = pg.Rect(x, y, self.size, self.size)
        #self.rect.center = (x+self.size/2, y+self.size/2)
        l_enemy.append(self)

    def move(self):
        # Mouvement vers la droite uniquement horizontal
        self.rect = self.rect.move(-10, 0)

    def shoot(self):
        # creer un tir à la position du vaisseau ennemi
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.cooldown = delai_tir_enemy
            missile_enemy(self.rect.left+self.size/5,
                          self.rect.top+self.size/3)


Chromius_warrior()


def spawn_chromius_fighter():
    # Fait apparaitre un chromius fighter toute les 120 frames
    global delai_spawn_enemy
    if delai_spawn_enemy > 0:
        delai_spawn_enemy -= 1
    else:
        Chromius_fighter()
        delai_spawn_enemy = 120


def destroy_old_enemy():
    to_delete = []
    for i in range(len(l_enemy)):
        if l_enemy[i].rect.right < 0:
            to_delete.append(i)
    for e in to_delete:
        l_enemy.pop(e)

# Initialisation d'un objet de la classe Asteroid + creation du mask des asteroid


# Cette ligne est a priori temporaire et devra etre retirer lorsque les asteroides seront vraiment implementes
asteroide = Asteroide()
