# Projet R-Type
# -*- coding: utf-8 -*-
from game.graphics import *
from game.ship import *
from game.sounds import *

while True:
    fenetre.fill(white)
    clock.tick(fps)
    direction, touche = detect_control()
    ship.move(direction)
    afficher_vaisseau(ship)
    defilement_decor()
    pg.display.update()
