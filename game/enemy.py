# Module enemy du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
from pygame import key


if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

# Apparition des astéroides :

def apparition(v):
    #Renvoie un quadruplet (x,y,vx,vy) qui serviront à faire apparaître l'astéroide
    x=width
    y=randint(0,height)
    target=randint(0,height)
    coeff=(y-target)/width
    vx=-(sqrt(1/(1+coeff**2))*v)
    # vx_approx=int(vx)
    vy=coeff*vx
    # vy_approx=int(vy)
    return (x,y,vx,vy)





