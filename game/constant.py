# Module constant du projet R-Type
# -*- coding: utf-8 -*-
# Penser à modifier les imports une fois le code terminé
import pygame as pg
from pygame.locals import *
from math import sqrt
from random import random,randint
from os import listdir

# Démarrage de pygame
pg.init()

# Les couleurs basiques
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
gray = 100, 100, 100
couleur_titre = (95, 199, 227)

#Liste d'ennemis
l_enemy=[]

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

# Tirs
L_tir_vaisseau=[]
speed_tir=30
long_tir=50
larg_tir=25
duree_tir=fps*1   #équivaut à 1seconde


# Création du dictionnaire pour importer les images
dico_image = {}
for file in listdir("resources/images/"):
    dico_image[file[:-4]] = "resources/images/" + file

# Chargement de la police du titre
police_titre = pg.font.Font("resources/font/space_age.ttf", 150)
# Chargement de la police du press start
police_press_start = pg.font.Font("resources/font/Open_24_Display.ttf", 50)
# Génération de la surface du titre
titre_ecran_demarrage = police_titre.render("ARPIE", True, couleur_titre)
rect_titre = titre_ecran_demarrage.get_rect()
rect_titre.center = (width//2, 150)
# Génération de la surface du press start
press_start = police_press_start.render(
    "Appuyez sur espace pour commencer la partie", True, couleur_titre)
rect_press_start = press_start.get_rect()
rect_press_start.center = (width//2, 500)

# Initialise l'état du jeu
state = 0


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
image = chargement_image(dico_image)


# Taille générique des images utilisées:
width_img = 32
height_img = 32

# Dimension en pixels de l'image qui sert de décor
width_fg = 1024
height_fg = 36
pixels_decor = 7  # nombre de pixel en hauteur du bandeau du décor

# 'Zoom' sur l'image en décor pour la faire coincider en hauteur avec la fenetre
ratio_decor = height / height_fg

# Numero du pixel du décor au bord droit de la fenètre
bord_fenetre_decor = width / ratio_decor

# Abscisse de ce pixel
x_bord_fenetre = bord_fenetre_decor*ratio_decor

# Abscisse du pixel tout à droite du décor
x_bord_decor = (width_fg-bord_fenetre_decor)*ratio_decor

# Déplacement à chaque avancée du décor (en unité d'abscisse pygame)
vitesse_decor = 1


# chargement image du décor
image['long_foreground_simple'] = pg.transform.scale(
    image['long_foreground_simple'], (width_fg*ratio_decor, height))
