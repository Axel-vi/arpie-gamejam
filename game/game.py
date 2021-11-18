# Module game du projet R-Type
# -*- coding: utf-8 -*-

from game.enemy import Asteroide, Chromius_fighter, Chromius_warrior, Chromius_tower
from game.graphics import *
from game.sounds import *


def detect_collision(ship, l_enemy, l_tir_enemy, l_tir_vaisseau, l_missile_enemy, abs_decor):
    """ Cette fonction detecte les collisions entre des objets. Elle prend en argument :
    - ship qui est un objet de la classe "Vaisseau" (doit avoir un attribut '.rect' !)
    - l_enemy qui est une liste d'ennemis : objets de la classe "Asteroide" ou "Chromius fighter" (doit avoir un attribut '.rect' !)
    - l_tir_enemy qui est une liste de tirs d'ennemis : objet de la classe "tir_enemy" (doit avoir un attribut '.rect' !)
    - abs_decor : l'entier relatif qui donne la position du bord de l'image de décor par rapport au bord de la fenetre visible (pour pouvoir gerer le defilement du decor)
    """
    index_enemy = []
    index_tir = []
    # Collisions ennemis-tir
    for i in range(len(l_tir_vaisseau)):
        for j in range(len(l_enemy)):
            # Calcul rapide de la collision avec des rectangles
            if l_tir_vaisseau[i].rect.colliderect(l_enemy[j].rect):
                # Calcul précis de la collision avec des masques
                if masks['tir_vaisseau'].overlap(masks[str(l_enemy[j].type)], (l_enemy[j].rect.left - l_tir_vaisseau[i].rect.left, l_enemy[j].rect.top - l_tir_vaisseau[i].rect.top)) != None:
                    if l_enemy[j].type != "asteroide" and l_enemy[j].type != "chromius_tower":
                        index_enemy.append(l_enemy[j])

                    index_tir.append(l_tir_vaisseau[i])
    # Suppression des ennemis touchés et création des explosions
    for j in index_enemy:
        Explosion(j.rect.left, j.rect.top)
        l_enemy.remove(j)
<<<<<<< HEAD
        explosion()
=======
    # Suppression des tirs ayant touché des ennemis
>>>>>>> ad62b13eb7d8f250c93e4754712bb729fbffa18b
    for j in index_tir:
        if j in l_tir_vaisseau:
            l_tir_vaisseau.remove(j)
    # Collisions vaisseau-ennemis
    for i in range(len(l_enemy)):
        if ship.rect.colliderect(l_enemy[i].rect):
            return masks['vaisseau'].overlap(masks[str(l_enemy[i].type)], (l_enemy[i].rect.left - ship.rect.left, l_enemy[i].rect.top - ship.rect.top)) != None
    # Collisions vaisseau-tir_ennemis
    for i in range(len(l_tir_enemy)):
        if ship.rect.colliderect(l_tir_enemy[i].rect):
            return masks['vaisseau'].overlap(masks['tir_enemy'], (l_tir_enemy[i].rect.left - ship.rect.left, l_tir_enemy[i].rect.top - ship.rect.top)) != None
    # Collisions vaisseau-missiles_ennemis
    for i in range(len(l_missile_enemy)):
        if ship.rect.colliderect(l_missile_enemy[i].rect):
            return masks['vaisseau'].overlap(masks['missile'], (l_missile_enemy[i].rect.left - ship.rect.left, l_missile_enemy[i].rect.top - ship.rect.top)) != None
    for i in range(len(l_tir_tower)):
        if ship.rect.colliderect(l_tir_tower[i].rect):
            return masks['vaisseau'].overlap(masks['tir_tower'], (l_tir_tower[i].rect.left - ship.rect.left, l_tir_tower[i].rect.top - ship.rect.top)) != None

    return masks['vaisseau'].overlap(masks['foregrnd'], (abs_decor - ship.rect.left, foregrnd.top - ship.rect.top)) != None


def gestion_event(niveau, compteur):
    """Fonction qui lance les apparitions d'ennemis programmées dans les fichiers niveau"""
    liste_event = niveau
    if len(liste_event) > 0:
        if compteur > 60*liste_event[0][0]:
            if liste_event[0][1] == 'asteroide':
                Asteroide()
                liste_event.pop(0)
            elif liste_event[0][1] == 'chromius_fighter':
                Chromius_fighter(liste_event[0][2], liste_event[0][3])
                liste_event.pop(0)
            else:
                Chromius_warrior(liste_event[0][2], liste_event[0][3])
                liste_event.pop(0)
    else:
        you_won = True
