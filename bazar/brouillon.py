
import pygame as pg
from pygame.locals import *

def affiche(largeur,hauteur,e,color): #e=largeur de la bande présente en haut et en bas de la map , color=color des bodures en RGB
    pg.init()    
    fenetre = pg.display.set_mode((largeur,hauteur))
    fond=pg.image.load("bazar/etoiles.jpg")
    fenetre.blit(fond,(0,0))
    pg.draw.rect(fenetre,color, pg.Rect(0,0,largeur,e))
    pg.draw.rect(fenetre,color, pg.Rect(0,hauteur-e,largeur, e ))
    pg.display.flip()
    a=1
    while a:
        a=int(input())

affiche(640,480,40,(255,0,0))
