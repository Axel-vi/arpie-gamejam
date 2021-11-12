# Module graphics du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
from pygame import key


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


def detect_control():
    touche = False
    direction = False
    for event in pg.event.get():
        if event.type == QUIT:
            quitter()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quitter()
    key_pressed = pg.key.get_pressed()
    if key_pressed[K_UP] or key_pressed[K_z]:
        if key_pressed[K_LEFT] or key_pressed[K_q]:
            direction = "nw"
        elif key_pressed[K_RIGHT] or key_pressed[K_d]:
            direction = "ne"
        else:
            direction = "n"
    elif key_pressed[K_DOWN] or key_pressed[K_s]:
        if key_pressed[K_LEFT] or key_pressed[K_q]:
            direction = "sw"
        elif key_pressed[K_RIGHT] or key_pressed[K_d]:
            direction = "se"
        else:
            direction = "s"
    elif key_pressed[K_LEFT] or key_pressed[K_q]:
        direction = "w"
    elif key_pressed[K_RIGHT] or key_pressed[K_d]:
        direction = "e"
    if key_pressed[K_SPACE]:
        touche = True
    return direction, touche
