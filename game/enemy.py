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
        self.size = 90
        self.rect = pg.Rect(width, y, self.size, self.size)
        self.rect.center = (width+self.size/2, y+self.size/2)
        target = randint(0, play_height)
        self.coeff = (y-target)/width
        self.speed_x = -(sqrt(1/(1+self.coeff**2))*speed)
        self.speed_y = self.coeff*self.speed_x
        l_enemy.append(self)

    def move_rect(self):
        """Fonction qui met un asteroid en mouvement"""
        self.rect = pg.Rect.move(self.rect, self.speed_x, self.speed_y)


# Initialisation d'un objet de la classe Asteroid + creation du mask des asteroid

# Cette ligne est a priori temporaire et devra etre retirer lorsque les asteroides seront vraiment implementes
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
