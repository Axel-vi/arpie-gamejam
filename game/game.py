# Module game du projet R-Type
# -*- coding: utf-8 -*-

from game.enemy import Asteroide, Chromius_fighter, Chromius_warrior
from game.graphics import *


def detect_collision(ship, l_enemy, l_tir_enemy, l_tir_vaisseau, l_missile_enemy, abs_decor):
    """ Cette fonction detecte les collisions entre des objets. Elle prend en argument :
    - ship qui est un objet de la classe "Vaisseau" (doit avoir un attribut '.rect' !)
    - l_enemy qui est une liste d'ennemis : objets de la classe "Asteroide" ou "Chromius fighter" (doit avoir un attribut '.rect' !)
    - l_tir_enemy qui est une liste de tirs d'ennemis : objet de la classe "tir_enemy" (doit avoir un attribut '.rect' !)
    - abs_decor : l'entier relatif qui donne la position du bord de l'image de décor par rapport au bord de la fenetre visible (pour pouvoir gerer le defilement du decor)
    """
    index_enemy = []
    index_tir = []
    for i in range(len(l_tir_vaisseau)):
        for j in range(len(l_enemy)):
            if l_tir_vaisseau[i].rect.colliderect(l_enemy[j].rect):
                if masks['tir_vaisseau'].overlap(masks[str(l_enemy[j].type)], (l_enemy[j].rect.left - l_tir_vaisseau[i].rect.left, l_enemy[j].rect.top - l_tir_vaisseau[i].rect.top)) != None:
                    index_enemy.append(l_enemy[j])
                    index_tir.append(l_tir_vaisseau[i])

    for j in index_enemy:
        l_enemy.remove(j)
    for j in index_tir:
        l_tir_vaisseau.remove(j)
    #                 l_enemy[j] = None
    # while None in l_enemy:
    #     l_enemy.remove(None)

    for i in range(len(l_enemy)):
        if ship.rect.colliderect(l_enemy[i].rect):
            return masks['vaisseau'].overlap(masks[str(l_enemy[i].type)], (l_enemy[i].rect.left - ship.rect.left, l_enemy[i].rect.top - ship.rect.top)) != None
    for i in range(len(l_tir_enemy)):
        if ship.rect.colliderect(l_tir_enemy[i].rect):
            return masks['vaisseau'].overlap(masks[str(l_tir_enemy[i].type)], (l_tir_enemy[i].rect.left - ship.rect.left, l_tir_enemy[i].rect.top - ship.rect.top)) != None
    for i in range(len(l_missile_enemy)):
        if ship.rect.colliderect(l_missile_enemy[i].rect):
            return masks['vaisseau'].overlap(masks['missile'], (l_missile_enemy[i].rect.left - ship.rect.left, l_missile_enemy[i].rect.top - ship.rect.top)) != None

    return masks['vaisseau'].overlap(masks['foregrnd'], (abs_decor - ship.rect.left, foregrnd.top - ship.rect.top)) != None


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


def gestion_event(niveau, compteur):
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
