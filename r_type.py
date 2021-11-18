"Projet R-Type"
# -*- coding: utf-8 -*-
from game.ship import Vaisseau, l_tir_vaisseau
from game.game import gestion_event, detect_collision
from game.graphics import afficher_ecran_demarrage, afficher_ecran_victoire, afficher_niveau_en_cours, detect_control_demarrage, fenetre,\
    defilement_decor_background, detect_control_game, afficher_vaisseau, \
    afficher_et_update_enemy, afficher_et_update_tir, afficher_et_update_explosion, \
    defilement_decor_foreground, afficher_ecran_fin, initialiser_decor, l_explosion
from game.sounds import musique_jeu, son_game_over
from game.enemy import destroy_old_enemy, l_enemy, l_missile_enemy, \
    l_tir_enemy, l_tir_tower
from game.constant import state_trans, compt_trans, pg, black, clock, fps, cos, \
    lire_niveau, liste_niveau, STATE, end_trans
#from carbonai import PowerMeter
#power_meter = PowerMeter(project_name="ARPIE")

# with power_meter(
#    package="ARPIE",
#    algorithm="RType",
#    data_type="tabular",
#    comments="Un RType"
# ):
while True:
    while STATE == 0:
        # Ecran de demarrage qui affiche le titre et le bouton play (Appuyer sur espace)
        afficher_ecran_demarrage(state_trans)
        NEW_STATE = detect_control_demarrage()
        COMPTEUR = 0
        id_niveau = 1
        if NEW_STATE == 1:
            STATE = 3
            musique_jeu()
        pg.display.update()
        if compt_trans % 2 == 0:
            state_trans += 1
        compt_trans += 1

    while STATE == 1:
        # Etat de jeu durant lequel l'utilisateur parcourt le niveau
        fenetre.fill(black)
        clock.tick(fps)
        COMPTEUR += 1
        gestion_event(niveau, COMPTEUR)
        defilement_decor_background()
        direction, touche = detect_control_game()
        SHIP.move(direction)
        afficher_vaisseau(SHIP)
        SHIP.shoot(touche)
        afficher_et_update_enemy(SHIP)
        afficher_et_update_tir()
        afficher_et_update_explosion()
        destroy_old_enemy()
        abs_decor = defilement_decor_foreground()
        if detect_collision(SHIP, l_enemy, l_tir_enemy,
                            l_tir_vaisseau, l_missile_enemy, l_tir_tower, abs_decor):
            son_game_over()
            STATE = 2
        pg.display.update()
            if COMPTEUR > 60*liste_niveau[id_niveau-1][1] :
                STATE = 4
            pg.display.update()

    while STATE == 2:
        # Etat de Game over
        end_trans += 1
        afficher_ecran_fin(int((1+cos(end_trans/150))/2*255))
        NEW_STATE = detect_control_demarrage()
        if NEW_STATE == 1:
            end_trans = 1
            STATE = 3
        pg.display.update()

    if STATE == 3:
            # Initialisation du niveau
            niveau = [el for el in liste_niveau[id_niveau-1][2]]
            COMPTEUR = 0
            niveau_1 = lire_niveau(id_niveau)
            initialiser_decor()
            SHIP = Vaisseau()
            while len(l_enemy) != 0:
                l_enemy.pop()
            while len(l_tir_enemy) != 0:
                l_tir_enemy.pop()
            while len(l_tir_vaisseau) != 0:
                l_tir_vaisseau.pop()
            while len(l_missile_enemy) != 0:
                l_missile_enemy.pop()
            while len(l_explosion) != 0:
                l_explosion.pop()
            while len(l_tir_tower) != 0:
                l_tir_tower.pop()
            STATE = 1
            musique_jeu()
    
    while STATE == 4 :
        afficher_ecran_victoire() 
        new_state = detect_control_demarrage()
        if new_state == 1 :
            id_niveau+=1
            STATE = 3
        pg.display.update()

