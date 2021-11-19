"Module enemy du projet R-Type"
# -*- coding: utf-8 -*-

from game.constant import l_tir_tower, l_enemy, l_missile_enemy, randint, play_height, asteroid_size,  \
    width, height, pg, sqrt, tir_size, duree_tir, l_tir_enemy, speed_missile_enemy, speed_tir_enemy, \
    speed_tir_tower, sq, sin, pi, scale_size, delai_tir_enemy, cos, atan, vitesse_decor, tower_height, tower_width,\
    size_chromius_lord, l_chromius_lord


class Asteroide:
    """Definition de la classe qui va servir a creer les asteroides et gerer leurs comportements"""

    def __init__(self):
        """Initialisation"""
        self.speed = randint(6, 10)
        self.y = randint(0, play_height)
        self.size = asteroid_size
        self.rect = pg.Rect(width, self.y, self.size, self.size)
        self.coeff = (self.y-randint(0, play_height))/width
        self.type = 'asteroide'
        self.speed_x = -(sqrt(1/(1+self.coeff**2))*self.speed)
        self.speed_y = self.coeff*self.speed_x
        l_enemy.append(self)

    def move(self):
        """Déplace l'astéroide selon sa vitesse horizontale et verticale"""
        self.rect = self.rect.move(self.speed_x, self.speed_y)

    def shoot(self, ship):
        """Un asteroide ne tire pas"""


class tir_enemy:
    """La classe pour les tirs des chromius fighter"""

    def __init__(self, x, y):
        """Initialisation"""
        self.rect = pg.Rect(x, y, tir_size, tir_size)
        self.duree = duree_tir
        """
        self.angle = atan((ship.rect.centery-y)/(ship.rect.centerx-x))
        if ship.rect.centerx-x < 0:
            self.speed = -speed_tir_enemy
        else:
            self.speed = speed_tir_enemy
        """
        l_tir_enemy.append(self)

    def move(self):
        """Déplace le tir vers la gauche à vitesse constante"""
        self.rect = self.rect.move(-speed_tir_enemy, 0)

    def update_duree(self):
        """Décrèmente un compteur, quand celui-ci atteint 0, le tir est supprimé"""
        self.duree -= 1
        if self.duree <= 0:
            l_tir_enemy.pop(0)


def pattern(id_pattern, t, starting_height=0):
    """Fonction pour gérer les patterns des ennemis.
    Prend en entrée l'id du pattern, le temps que l'ennemi' a passé à l'écran et sa hauteur d'entrée à l'écran.
    Renvoie un tuple représentant les coordonnées de l'ennemi."""
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


class Chromius_fighter():
    """Classe pour gérer les chromius fighter"""

    def __init__(self, hauteur, id_pattern):
        """Initialisation"""
        self.size = scale_size
        x = width
        y = hauteur
        self.type = 'chromius_fighter'
        self.cooldown = 0
        self.id_pattern = id_pattern
        self.hauteur = hauteur
        self.t = 0
        self.rect = pg.Rect(x, y, self.size, self.size)
        l_enemy.append(self)

    def move(self):
        """Déplace le chromius fighter selon son pattern"""
        self.t += 1
        x, y = pattern(self.id_pattern, self.t, self.hauteur)
        self.rect = pg.Rect(x, y, self.size, self.size)

    def shoot(self, ship):
        """Gère la création des tirs des chromius fighter et le cooldown entre chaque tir."""
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.cooldown = delai_tir_enemy
            tir_enemy(self.rect.left+self.size/5, self.rect.top+self.size/3)


class missile_enemy:
    """Classe pour gérer les missiles tirés par les chromius warrior."""

    def __init__(self, x, y):
        """Initialisation"""
        self.rect = pg.Rect(x, y, tir_size, tir_size)
        self.duree = duree_tir
        l_missile_enemy.append(self)

    def move(self):
        """Déplace le missile vers la gauche"""
        self.rect = self.rect.move(speed_missile_enemy, 0)

    def update_duree(self):
        """Décrèmente un compteur, quand celui-ci atteint 0, le missile est supprimé"""
        self.duree -= 1
        if self.duree <= 0:
            l_missile_enemy.pop(0)


class Chromius_warrior():
    """Classe pour gérer les chromius fighter"""

    def __init__(self, hauteur, id_pattern):
        """Initialisation"""
        self.size = scale_size
        x = width
        y = hauteur
        self.type = 'chromius_warrior'
        self.cooldown = 0
        self.t = 0
        self.hauteur = hauteur
        self.id_pattern = id_pattern
        self.rect = pg.Rect(x, y, self.size, self.size)
        l_enemy.append(self)

    def move(self):
        """Déplace le chromius warrior selon son pattern"""
        self.t += 1
        x, y = pattern(self.id_pattern, self.t, self.hauteur)
        self.rect = pg.Rect(x, y, self.size, self.size)

    def shoot(self, ship):
        """Gère la création des missiles des chromius warrior et le cooldown entre chaque tir."""
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.cooldown = 2*delai_tir_enemy
            missile_enemy(self.rect.left+self.size/5,
                          self.rect.top+self.size/3)


class tir_tower:
    def __init__(self, x, y, ship):
        """Initialisation"""
        self.rect = pg.Rect(x, y, tir_size, tir_size)
        self.duree = 3*duree_tir
        diff_x = ship.rect.centerx-x
        if diff_x == 0:
            diff_x = 1
        self.angle = atan((ship.rect.centery-y) /
                          (diff_x))
        if ship.rect.centerx-x < 0:
            self.speed = -speed_tir_tower
        else:
            self.speed = speed_tir_tower
        l_tir_tower.append(self)

    def move(self):
        """Déplace le tir selon l'angle précisé"""
        self.rect = self.rect.move(
            self.speed*cos(self.angle), self.speed*sin(self.angle))

    def update_duree(self):
        """Décrèmente un compteur, quand celui-ci atteint 0, le tir est supprimé"""
        self.duree -= 1
        if self.duree <= 0:
            l_tir_tower.pop(0)


class Chromius_tower:
    """Classe pour gérer les chromius tower"""

    def __init__(self):
        """Initialisation"""
        self.type = 'chromius_tower'
        self.cooldown = 60
        self.t = 0
        self.rect = pg.Rect(width, height-tower_height,
                            tower_width, tower_height)
        l_enemy.append(self)
        self.xsize = tower_width
        self.ysize = tower_height

    def move(self):
        """Déplace le chromius warrior selon son pattern"""
        self.rect = self.rect.move(-vitesse_decor, 0)

    def shoot(self, ship):
        """Gère la création des missiles des chromius warrior et le cooldown entre chaque tir."""
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.cooldown = 60
            tir_tower(self.rect.left+tower_width/5, self.rect.top, ship)


def destroy_old_enemy():
    """Fonction qui supprime les ennemis en dehors de l'écran"""
    to_delete = []
    for i in range(len(l_enemy)):
        if l_enemy[i].rect.right < 0:
            to_delete.append(l_enemy[i])
    for e in to_delete:
        if e in l_enemy:
            l_enemy.remove(e)


class Chromius_lord:
    def __init__(self):
        self.size = size_chromius_lord
        self.rect = pg.Rect(width, height//2 - self.size, self.size, self.size)
        self.type = "chromius_lord"
        self.l_cooldown = [0, 20, 40, 60]
        self.t = 0
        self.speed_x = 2
        self.amplitude = 200
        self.pv = 100
        self.hitstun = 0
        self.offsetx1 = self.size/5
        self.offsetx2 = 0
        self.offsety1 = self.size/4
        self.offsety2 = self.size/8
        self.l_pos = [(self.rect.centerx - self.offsetx1, self.rect.centery - self.offsety1),
                      (self.rect.centerx - self.offsetx2,
                       self.rect.centery - self.offsety2),
                      (self.rect.centerx - self.offsetx1,
                       self.rect.centery + self.offsety1),
                      (self.rect.centerx - self.offsetx2, self.rect.centery + self.offsety2)]
        l_chromius_lord.append(self)

    def move(self):
        self.t += 1
        if self.hitstun > 0:
            self.hitstun -= 1
        x = width - 2*self.t
        if x < width//2:
            x = width // 2
        self.rect = pg.Rect(x, height//2 - self.size//2 +
                            cos(self.t/60)*self.amplitude, self.size, self.size)
        self.l_pos = [(self.rect.centerx - self.offsetx1, self.rect.centery - self.offsety1),
                      (self.rect.centerx - self.offsetx2,
                       self.rect.centery - self.offsety2),
                      (self.rect.centerx - self.offsetx1,
                       self.rect.centery + self.offsety1),
                      (self.rect.centerx - self.offsetx2, self.rect.centery + self.offsety2)]

    def shoot(self, ship):
        for i in range(len(self.l_cooldown)):
            self.l_cooldown[i] -= 1
            if self.l_cooldown[i] < 1:
                self.l_cooldown[i] = randint(100, 140)
                tir_tower(self.l_pos[i][0], self.l_pos[i][1], ship)

    def detect_collision(self, l_tir_vaisseau, masks):
        to_remove = []
        for tir in l_tir_vaisseau:
            if masks["tir_vaisseau"].overlap(masks["chromius_lord"], (self.rect.left - tir.rect.left, self.rect.top - tir.rect.top)) != None:
                self.pv -= 1
                self.hitstun = 6
                to_remove.append(tir)
        for tir in to_remove:
            l_tir_vaisseau.remove(tir)
        if self.pv < 1:
            l_chromius_lord.remove(self)
