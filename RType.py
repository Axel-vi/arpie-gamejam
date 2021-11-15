# Projet R-Type
# -*- coding: utf-8 -*-
from game.graphics import *
from game.ship import *
from game.sounds import *


while True:
    while state == 0:
        afficher_ecran_demarrage()
        new_state = detect_control_demarrage()
        if new_state == 1:
            state = 1
        pg.display.update()
    while state == 1:
        fenetre.fill(black)
        clock.tick(fps)
        direction, touche = detect_control_game()
        ship.move(direction)
        afficher_vaisseau(ship)
        defilement_decor()
        ship.shoot(touche)
        afficher_et_update_tir_vaisseau()
        pg.display.update()
    while state == 2:
        afficher_ecran_fin()
        new_state = detect_control_demarrage()
        if new_state == 1:
            state = 1
        pg.display.update()
