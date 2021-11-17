# Projet R-Type
# -*- coding: utf-8 -*-
from game.graphics import *
from game.ship import *
from game.sounds import *
from game.game import *
from game.enemy import *


while True:
    while state == 0:
        afficher_ecran_demarrage()
        new_state = detect_control_demarrage()
        compteur = 0
        id_niveau = 1
        if new_state == 1:
            state = 3
        pg.display.update()

    while state == 1:
        fenetre.fill(black)
        clock.tick(fps)
        compteur +=1
        gestion_event(niveau, compteur)
        direction, touche = detect_control_game()
        ship.move(direction)
        afficher_vaisseau(ship)
        ship.shoot(touche)
        abs_decor = defilement_decor()
        # spawn_chromius_fighter()
        afficher_et_update_enemy()
        afficher_et_update_tir()
        destroy_old_enemy()
        if detect_collision(ship, l_enemy, abs_decor):
            state = 2
        pg.display.update()

    while state == 2:
        afficher_ecran_fin()
        new_state = detect_control_demarrage()
        if new_state == 1:
            state = 3
        pg.display.update()
        
    if state == 3 :
        niveau = [el for el in liste_niveau[id_niveau][2]]
        compteur = 0
        niveau_1 = lire_niveau(id_niveau)
        initialiser_decor()
        ship = Vaisseau()
        while len(l_enemy) != 0:
            l_enemy.pop()
        while len(l_tir_enemy) != 0:
            l_tir_enemy.pop()
        while len(l_tir_vaisseau) != 0:
            l_tir_vaisseau.pop()
        state = 1
