# Module sounds du projet R-Type
# -*- coding: utf-8 -*-
# Penser à modifier les imports une fois le code terminé
import pygame as pg
from pygame.locals import *

# Imports spécifiques
if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

# Création des objets liés au son
canal_musique = pg.mixer.Channel(0)
canal_musique.set_volume(volume_musique)
canal_son = pg.mixer.Channel(1)
canal_son.set_volume(volume_bruitage)


# Fonction pour charger les musiques
def chargement_musique(dico):
    """Fonction pour charger toutes les musiques d'un coup.
    Prend en entrée un dictionnaire avec le nom de chaque musique et sa position.
    Renvoie un dictionnaire avec le nom de chaque musique et la musique elle même.
    """
    for nom_musique in dico:
        dico[nom_musique] = pg.mixer.Sound(dico[nom_musique])
    return dico
