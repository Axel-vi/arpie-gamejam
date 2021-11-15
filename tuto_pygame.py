import pygame
import time
window=pygame.display.set_mode((1280,720))
pygame.display.set_caption("yessir")

vitesse_tir=10
FPS=60
saitamos=pygame.image.load('opm_head.png')
saitamos=pygame.transform.scale(saitamos,(80,80))

def dessin():
    global sait
    window.fill((255,255,255))
    window.blit(saitamos,(sait.x,sait.y))

def deplacer():
    touches=pygame.key.get_pressed()
    if touches[pygame.K_RIGHT]:
        sait.x+=5
    if touches[pygame.K_DOWN]:
        sait.y+=5
    if touches[pygame.K_UP]:
        sait.y-=5
    if touches[pygame.K_LEFT]:
        sait.x-=5

def main(saitamos):
    global sait
    sait=pygame.Rect(200,200,10,10)
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        dessin()
        for truc in pygame.event.get():
            if truc.type==pygame.QUIT:
                run=False
        pygame.display.update()
        deplacer()
    pygame.quit()
main(saitamos)




