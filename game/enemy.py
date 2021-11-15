# Module enemy du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
from pygame import key


if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *


#IMPORTS A SUPPR-----------------A SUPPR--------------A SUPPR------------------------A SUPPR
window=pg.display.set_mode((1280,720))
pg.display.set_caption("yessir")
saitamos=pg.image.load('opm_head.png')
saitamos=pg.transform.scale(saitamos,(80,80))
#IMPORTS A SUPPR-----------------A SUPPR--------------A SUPPR------------------------A SUPPR

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

def test(v):
    x,y,vx,vy=apparition(v)
    aste=pg.Rect(x,y,10,10)
    clock=pg.time.Clock()
    run=True
    while run:
        clock.tick(fps)
        window.fill((255,255,255))
        print(aste.x,aste.y)
        window.blit(saitamos,(aste.x,aste.y))
        aste.x+=vx
        aste.y+=vy
        for truc in pg.event.get():
            if truc.type==pg.QUIT:
                run=False
        pg.display.update()
    pg.quit()
test(30)    


