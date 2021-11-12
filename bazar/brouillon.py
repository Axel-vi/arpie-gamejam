
import pygame as pg
from pygame.locals import *
"""
def affiche(largeur,hauteur,e,color): #e=largeur de la bande présente en haut et en bas de la map , color=color des bodures en RGB
    pg.init()    
    fenetre = pg.display.set_mode((largeur,hauteur))
    fond=pg.image.load("bazar/etoiles.jpg").convert()
    fond=pg.transform.scale(fond,(largeur,hauteur))    
    fenetre.blit(fond,(0,0))
    ship=pg.image.load("bazar/ship_simple.png").convert()
    fenetre.blit(ship,(largeur/2,hauteur/2))
    pg.draw.rect(fenetre,color, pg.Rect(0,0,largeur,e))
    pg.draw.rect(fenetre,color, pg.Rect(0,hauteur-e,largeur,e))
    pg.display.flip()
    a=1
    while a:
        a=int(input())
"""
def affiche(largeur,hauteur,e,color): #e=largeur de la bande présente en bas de la map , color=color des bodures en RGB
    pg.init()    
    fenetre = pg.display.set_mode((largeur,hauteur))
    fond=pg.image.load("bazar/etoiles.jpg").convert()
    fond=pg.transform.scale(fond,(largeur,hauteur))    
    fenetre.blit(fond,(0,0))
    ship=pg.image.load("bazar/ship_simple.png").convert()
    fenetre.blit(ship,(largeur/2,hauteur/2))
    foreground=pg.image.load("bazar/foreground.png").convert()
    foreground=pg.transform.scale(foreground,(largeur,e))    
    fenetre.blit(foreground,(0,hauteur-e))
    pg.display.flip()
    a=1
    while a:
        a=int(input())

affiche(640,480,40,(255,0,0))
