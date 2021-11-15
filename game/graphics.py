# Module graphics du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
from os import stat
from pygame import key


if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

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


def afficher_image(image, long, larg, x, y, anchor="ne"):
    """Fonction qui modifie la taille et affiche une image.
    Prend en entrée une image, la dimension à lui donner et la position à laquelle l'afficher.
    """
    img = pg.transform.scale(image, (long, larg))
    rectPos = img.get_rect()
    if anchor == "nw":
        rectPos.topright = (x, y)
    else:
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


def detect_control_game():
    """Fonction qui récupère les inputs de l'utilisateur et renvoie un tuple (direction, touche)
    """
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


def detect_control_demarrage():
    for event in pg.event.get():
        if event.type == QUIT:
            quitter()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quitter()
            if event.key == K_SPACE:
                return 1


def defilement_decor():
    """Définition de la boucle qui va faire défiler le décor au premier plan.
    \nLa vitesse de défilement est ajustable dans le fichier constant.py
    """
    global foregrnd
    if -foregrnd.topleft[0] >= x_bord_decor:
        foregrnd = foregrnd.move(-foregrnd.topleft[0], 0)
    else:
        foregrnd = foregrnd.move(-vitesse_decor, 0)
    fenetre.blit(image["long_foreground_simple"], foregrnd)

    # Initialisation du décor
global foregrnd
foregrnd = image["long_foreground_simple"].get_rect()


def afficher_vaisseau(ship):
    afficher_image(image["vaisseau"], ship.size,
                   ship.size, ship.rect.left, ship.rect.top)
    if ship.state == "accelerate":
        afficher_image(image["flamme"], ship.size,
                       ship.size, ship.rect.left, ship.rect.top, anchor="nw")
    elif ship.state == "static":
        afficher_image(image["flamme_faible"], ship.size,
                       ship.size, ship.rect.left, ship.rect.top, anchor="nw")


def afficher_ecran_demarrage():
    fenetre.fill(black)
    fenetre.blit(titre_ecran_demarrage, rect_titre)
    fenetre.blit(press_start, rect_press_start)

def afficher_ecran_fin():
    fenetre.fill(black)
    fenetre.blit(titre_game_over,rect_game_over)
    fenetre.blit(play_again,rect_play_again)
    fenetre.blit(crochets,rect_crochets)


