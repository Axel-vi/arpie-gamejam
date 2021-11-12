# Module constant du projet R-Type
# -*- coding: utf-8 -*-
# Penser à modifier les imports une fois le code terminé
import pygame as pg
from pygame.locals import *

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
