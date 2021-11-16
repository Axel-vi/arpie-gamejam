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
        size = 90
        self.rect = pg.Rect(width, y, size, size)
        self.rect.center = (width+size/2, y+size/2)
        target = randint(0, play_height)
        coeff = (y-target)/width
        self.type='asteroide'
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
            tir_enemy(self.rect.left+self.size/5, self.rect.top+self.size/3)
    
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
<<<<<<< game/enemy.py
# asteroid = Asteroide()
# maskAsteroid = pg.mask.from_surface(pg.transform.scale(image["asteroide"].convert_alpha(), (90, 90)))


def pattern(id_pattern, t, starting_height=0):
    if id_pattern == 1:
        return (width-6*t, starting_height)
    elif id_pattern == 2 or id_pattern == 3 or id_pattern == 4 or id_pattern == 5 or id_pattern == 6 or id_pattern == 7:
        if id_pattern == 2:
            amplitude = 100
        elif id_pattern == 3:
            amplitude = -100
        elif id_pattern == 4:
            amplitude = 200
        elif id_pattern == 5:
            amplitude = -200
        elif id_pattern == 6:
            amplitude = 400
        elif id_pattern == 7:
            amplitude = -400
        x = width-6*t/sq
        pow = 1 - int(x/320) % 2
        y_offset = (x/320-int(x/320))*amplitude*(-1)**pow + amplitude//2
        if pow == 0:
            y_offset = y_offset - amplitude
        return (x, starting_height + y_offset)
    elif id_pattern == 8 or id_pattern == 9 or id_pattern == 10 or id_pattern == 11:
        if id_pattern == 8:
            amplitude = 100
        elif id_pattern == 9:
            amplitude = -100
        elif id_pattern == 10:
            amplitude = 400
        elif id_pattern == 11:
            amplitude = -400
        x = width-6*t/sq
        return (x, starting_height + sin(x*2*pi/1280)*amplitude//2)
    elif id_pattern == 12 or id_pattern == 13:
        if id_pattern == 12:
            amplitude = 400
        elif id_pattern == 13:
            amplitude = -400
        x = width-6*t/sq
        pow = 1 - int(x/320) % 2
        y_offset = (x/320-int(x/320))*amplitude*(-1)**pow + amplitude//2
        if pow == 0:
            y_offset = y_offset - amplitude
        if y_offset > 0:
            y_offset = min(y_offset, 100)
        else:
            y_offset = max(y_offset, -100)
        return (x, starting_height + y_offset)
    else:
        raise NotImplementedError
=======
asteroid = Asteroide()
maskEnemy = pg.mask.from_surface(pg.transform.scale(
    image["asteroide"].convert_alpha(), (90, 90)))

>>>>>>> game/enemy.py
