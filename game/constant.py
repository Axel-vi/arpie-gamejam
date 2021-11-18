# Module constant du projet R-Type
# -*- coding: utf-8 -*-
# Penser à modifier les imports une fois le code terminé
import pygame as pg
from pygame.locals import *
from pygame import key
from math import sqrt, sin, pi, atan, cos
from random import random, randint
from os import listdir
import matplotlib.pyplot as plt
from time import sleep

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
couleur_titre = (82, 116, 245)

# Liste d'ennemis
l_enemy = []

# Réglage du nombre de fps
clock = pg.time.Clock()
fps = 60

# Taille de la fenêtre
width = 1280
height = 720
play_height = 540

# Taille du vaisseau et des ennemis
scale_size = 75
asteroid_size = 90
tir_size = 35
speed_chromius_fighter = 10

# Volume des sons
volume_musique = 0.2
volume_bruitage = 0.5

# Tirs
l_tir_vaisseau = []
l_tir_enemy = []
l_missile_enemy = []
speed_tir = 30
delai_tir = 45
delai_spawn_enemy = 120
speed_tir_enemy = 20
speed_missile_enemy = -30
delai_tir_enemy = 60
duree_tir = fps*1  # équivaut à 1seconde


# Tour

tower_size = 300
speed_tir_tower = 12
l_tir_tower = []
# Liste pour stocker les explosions en cours
l_explosion = []

# Constante pour accélerer les calculs
sq = sqrt(2)


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
titre_game_over = police_titre.render("GAME OVER", True, red)
play_again = police_press_start.render("Play again?", True, red)
crochets = police_press_start.render("[           ]", True, red)
rect_game_over = titre_game_over.get_rect()
rect_game_over.center = (width/2, height/3)
rect_play_again = play_again.get_rect()
rect_play_again.center = (width/2, 2*height/3)
rect_crochets = crochets.get_rect()
rect_crochets.center = (width/2, 2*height/3)
rect_titre = titre_ecran_demarrage.get_rect()

rect_titre.center = (width//2, 150)
# Génération de la surface du press start
press_start = police_press_start.render(
    "Appuyez sur espace pour commencer la partie", True, couleur_titre)
rect_press_start = press_start.get_rect()
rect_press_start.center = (width//2, 500)

# Chargement des niveaux


def lire_niveau(id_niveau):
    fichier = open('./data/niveau_'+str(id_niveau)+'.txt', 'r')
    nom_niveau = fichier.readline()
    distance_totale = fichier.readline()
    liste_event = []
    for ligne in fichier:
        ligne = ligne.replace("\n", "")
        date, type, arg = ligne.split(";")
        date = float(date)
        if type == 'chromius_fighter' or type == 'chromius_warrior':
            hauteur, id_pattern = arg.split(":")
            hauteur = int(hauteur)
            id_pattern = int(id_pattern)
            arg = [hauteur, id_pattern]
            liste_event.append([date]+[type]+arg)
        else:
            liste_event.append([date]+[type])
    return [nom_niveau, distance_totale, liste_event]


niveau_0 = lire_niveau(0)
niveau_1 = lire_niveau(1)
# print(niveau_1)
liste_niveau = [niveau_0, niveau_1]
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
height_fg = 72
width_bg = 2048
height_bg = 360
pixels_decor = 7  # nombre de pixel en hauteur du bandeau du décor

# 'Zoom' sur l'image en décor pour la faire coincider en hauteur avec la fenetre
ratio_decor = height / height_fg
ratio_bg = height / height_bg

# Numero du pixel du décor au bord droit de la fenètre
bord_fenetre_decor = width / ratio_decor
bord_fenetre_bg = width / ratio_bg

# Abscisse de ce pixel
x_bord_fenetre = bord_fenetre_decor*ratio_decor
x_bord_bg = bord_fenetre_bg*ratio_bg

# Abscisse du pixel tout à droite du décor
x_bord_decor = (width_fg-bord_fenetre_decor)*ratio_decor
x_bord_bg = (width_bg-bord_fenetre_bg)*ratio_bg

# Déplacement à chaque avancée du décor (en unité d'abscisse pygame)
vitesse_decor = 5
vitesse_bg = 1
vitesse_mg = 3

# Nombre d'étoiles dans l'écran de démarrage
nb_star = 100
starfield = pg.Surface((width, height))

# Compteur de frame pour gérer la transparence dynamique de l'écran de démarrage
compt_trans = 0
state_trans = 0
end_trans = 0

# Chargement des frames de l'explosion
spriteSheetExplosion = pg.image.load("resources/images/explosion_ss.png")
