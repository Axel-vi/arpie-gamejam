# Module constant du projet R-Type
# -*- coding: utf-8 -*-
# Penser à modifier les imports une fois le code terminé
import pygame as pg
from pygame.locals import *
from math import sqrt

# Les couleurs basiques
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
gray = 100, 100, 100

# Les tailles de police standards
SMALL = 12
MEDIUM = 16
LARGE = 34
TITLE = 50

# Réglage du nombre de fps
clock = pg.time.Clock()
fps = 60

# Taille de la fenêtre
width = 1280
height = 720

# Volume des sons
volume_musique = 0.2
volume_bruitage = 0.5

# Création du dictionnaire pour importer les images
dico_image = {"vaisseau": "resources/images/vaisseau.png"}


def chargement_image(dico):
    """Fonction pour charger toutes les images d'un coup.
    Prend en entrée un dictionnaire avec le nom de chaque image et sa position.
    Renvoie un dictionnaire avec le nom de chaque image et l'image elle même.
    """
    for nom_image in dico:
        dico[nom_image] = pg.image.load(dico[nom_image])
    return dico


def chargement_musique(dico):
    """Fonction pour charger toutes les musiques d'un coup.
    Prend en entrée un dictionnaire avec le nom de chaque musique et sa position.
    Renvoie un dictionnaire avec le nom de chaque musique et la musique elle même.
    """
    for nom_musique in dico:
        dico[nom_musique] = pg.mixer.Sound(dico[nom_musique])
    return dico


# Chargement des images
dico_image = chargement_image(dico_image)
