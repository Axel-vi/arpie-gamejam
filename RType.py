# Projet R-Type
# -*- coding: utf-8 -*-
from game.graphics import *
from game.ship import *
from game.sounds import *

while True:
    fenetre.fill(black)
    clock.tick(fps)
    direction, touche = detect_control()
    x_vaisseau, y_vaisseau = move_ship(direction)
    afficher_image(dico_image["vaisseau"], 200,
                   200, x_vaisseau, y_vaisseau)
    defilement_decor()
    pg.display.update()
