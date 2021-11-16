# Projet R-Type
# -*- coding: utf-8 -*-
from pygame import mask
from game.graphics import *
from game.ship import *
from game.sounds import *
from game.game import *
from game.enemy import *


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

        asteroid.move_rect()
        afficher_asteroid(asteroid)

        abs_decor = defilement_decor()
        ship.shoot(touche)
        afficher_et_update_tir_vaisseau()
        # A l'heure actuelle la collision avec le décor ne marche pas car le masque ne prend pas en compte le deplacement de l'image
        if detect_collision(ship, l_enemy, maskShip, maskEnemy, maskForegrnd, abs_decor):
            state = 2
        pg.display.update()
    while state == 2:
        afficher_ecran_fin()
        # Attention il faut reset la game aussi !!
        new_state = detect_control_demarrage()
        if new_state == 1:
            state = 1
        pg.display.update()
