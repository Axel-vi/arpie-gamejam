# Module graphics du projet R-Type
# -*- coding: utf-8 -*-
# Penser à modifier les imports une fois le code terminé
import pygame as pg
from pygame.locals import *

# Imports spécifiques
if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

pg.init()

# Création de la fenêtre
fenetre = pg.display.set_mode((width, height))
fenetre.fill(white)
rectFenetre = fenetre.get_rect()

# Réglage de la fenetre
pg.display.set_caption("R-Type")
# pg.display.set_icon(<icon>)


def quitter():
    """Fonction qui ferme pygame et python."""
    pg.quit()
    quit()


def detect_quitter():
    """Fonction qui détecte l'ordre de fermeture de la fenêtre et quitte.
    """
    for event in pg.event.get():
        if event.type == QUIT:
            quitter()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quitter()


def transition(fenetre, couleur=white):
    """Fonction pour faire une transition d'un état à un autre avec une pause d'une demi-seconde.
    Affiche un écran de la couleur choisie pour les transitions.
    """
    time_left = fps//2
    while clock.tick(fps) and time_left > 0:
        time_left -= 1
        fenetre.fill(couleur)
        pg.display.update()
    # print("transition")


def chargement_image(dico):
    """Fonction pour charger toutes les images d'un coup.
    Prend en entrée un dictionnaire avec le nom de chaque image et sa position.
    Renvoie un dictionnaire avec le nom de chaque image et l'image elle même.
    """
    for nom_image in dico:
        dico[nom_image] = pg.image.load(dico[nom_image])
    return dico


def afficher_image(image, long, larg, x, y):
    """Fonction qui modifie la taille et affiche une image.
    Prend en entrée une image, la dimension à lui donner et la position à laquelle l'afficher.
    """
    img = pg.transform.scale(image, (long, larg))
    rectPos = img.get_rect()
    rectPos.topleft = (x, y)
    fenetre.blit(img, rectPos)


def transparent(img, valeur=150):
    """Fonction qui convertit une image en image transparente.
    Prend en entrée une image et valeur entre 0 et 255 (0  = transparent).
    Renvoie une nouvelle image transparente sans modifier l'originale.
    """
    res = img.copy()
    res = pg.Surface.convert_alpha(res)
    res.fill((255, 255, 255, valeur), special_flags=BLEND_RGBA_MULT)
    return res
