# Projet R-Type
# -*- coding: utf-8 -*-
from game.graphics import *
from game.ship import *
from game.sounds import *
from game.game import *
from game.enemy import *

k=0
while True:
    while state == 0:
        # Ecran de demarrage qui affiche le titre et le bouton play (Appuyer sur espace)
        afficher_ecran_demarrage(state_trans)
        new_state = detect_control_demarrage()
        compteur = 0
        id_niveau = 1
        if new_state == 1:
            state = 3
        pg.display.update()
        if compt_trans % 2 == 0:
            state_trans += 1
        compt_trans += 1

    while state == 1:
        # Etat de jeu durant lequel l'utilisateur parcoure le niveau
        fenetre.fill(black)
        clock.tick(fps)
        compteur += 1
        gestion_event(niveau, compteur)
        defilement_decor_background()
        direction, touche = detect_control_game()
        ship.move(direction)
        afficher_vaisseau(ship)
        ship.shoot(touche)
        afficher_et_update_enemy(ship)
        afficher_et_update_tir()
        afficher_et_update_explosion()
        destroy_old_enemy()
        k+=1
        if k>300:
            Chromius_tower()
            k=0
        abs_decor = defilement_decor_foreground()
        if detect_collision(ship, l_enemy, l_tir_enemy, l_tir_vaisseau, l_missile_enemy, abs_decor):
            state = 2
        pg.display.update()

    while state == 2:
        # Etat de Game over
        end_trans += 1
        afficher_ecran_fin(int((1+cos(end_trans/150))/2*255))
        new_state = detect_control_demarrage()
        if new_state == 1:
            end_trans = 1
            state = 3
        pg.display.update()

    if state == 3:
        # Initialisation du niveau
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
        while len(l_missile_enemy) != 0:
            l_missile_enemy.pop()
        state = 1
