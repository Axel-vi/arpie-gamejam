# Projet R-Type
# -*- coding: utf-8 -*-
from game.graphics import *
from game.ship import *
from game.sounds import *

while True:
    clock.tick(fps)
    direction, touche = detect_control()
    x_vaisseau, y_vaisseau = move_ship(direction)
    afficher_image(dico_image["vaisseau"], 200,
                   200, x_vaisseau, y_vaisseau)
    pg.display.update()
