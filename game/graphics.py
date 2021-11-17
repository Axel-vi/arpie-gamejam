# Module graphics du projet R-Type
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

# Création de la fenêtre
fenetre = pg.display.set_mode((width, height))
fenetre.fill(white)
rectFenetre = fenetre.get_rect()

# Réglage de la fenetre
pg.display.set_caption("R-Type")
# pg.display.set_icon(<icon>)


def quitter():
    """Fonction qui ferme pygame et python."""
    pg.quit()
    quit()


def detect_quitter():
    """Fonction qui détecte l'ordre de fermeture de la fenêtre et quitte.
    """
    for event in pg.event.get():
        if event.type == QUIT:
            quitter()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quitter()


def transition(fenetre, couleur=white):
    """Fonction pour faire une transition d'un état à un autre avec une pause d'une demi-seconde.
    Affiche un écran de la couleur choisie pour les transitions.
    """
    time_left = fps//2
    while clock.tick(fps) and time_left > 0:
        time_left -= 1
        fenetre.fill(couleur)
        pg.display.update()
    # print("transition")


def afficher_image(image, long, larg, x, y, anchor="ne"):
    """Fonction qui modifie la taille et affiche une image.
    Prend en entrée une image, la dimension à lui donner et la position à laquelle l'afficher.
    """
    img = pg.transform.scale(image, (long, larg))
    rectPos = img.get_rect()
    if anchor == "nw":
        rectPos.topright = (x, y)
    else:
        rectPos.topleft = (x, y)
    fenetre.blit(img, rectPos)


def transparent(img, valeur=150):
    """Fonction qui convertit une image en image transparente.
    Prend en entrée une image et valeur entre 0 et 255 (0  = transparent).
    Renvoie une nouvelle image transparente sans modifier l'originale.
    """
    res = img.copy()
    res = pg.Surface.convert_alpha(res)
    res.fill((255, 255, 255, valeur), special_flags=BLEND_RGBA_MULT)
    return res


def detect_control_game():
    """Fonction qui récupère les inputs de l'utilisateur et renvoie un tuple (direction, touche)
    """
    touche = False
    direction = False
    for event in pg.event.get():
        if event.type == QUIT:
            quitter()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quitter()
    key_pressed = pg.key.get_pressed()
    if key_pressed[K_UP] or key_pressed[K_z]:
        if key_pressed[K_LEFT] or key_pressed[K_q]:
            direction = "nw"
        elif key_pressed[K_RIGHT] or key_pressed[K_d]:
            direction = "ne"
        else:
            direction = "n"
    elif key_pressed[K_DOWN] or key_pressed[K_s]:
        if key_pressed[K_LEFT] or key_pressed[K_q]:
            direction = "sw"
        elif key_pressed[K_RIGHT] or key_pressed[K_d]:
            direction = "se"
        else:
            direction = "s"
    elif key_pressed[K_LEFT] or key_pressed[K_q]:
        direction = "w"
    elif key_pressed[K_RIGHT] or key_pressed[K_d]:
        direction = "e"
    if key_pressed[K_SPACE]:
        touche = True
    return direction, touche


def detect_control_demarrage():
    """ Fonction qui sert a gerer les controles de l'utilisateur sur les ecrans de demarrage/fin.
    Appuyer sur la touche ESPACE met dans l'etat "True"
    """
    for event in pg.event.get():
        if event.type == QUIT:
            quitter()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quitter()
            if event.key == K_SPACE:
                return 1


# Initialisation du décor
def initialiser_decor():
    """Cette foncion initialise le décor
    """
    global foregrnd
    global abs_decor
    global l_star
    abs_decor = 0
    l_star = []
    foregrnd = image["long_foreground_relief"].get_rect()
    for i in range(nb_star):
        l_star.append(Star())
# Objets pour l'écran de démarrage


class Star():
    def __init__(self):
        self.x = random()*width//2
        self.y = random()*height//2
        self.sx = self.x
        self.sy = self.y
        self.star_speed = 0.2
        self.max_radius = 10
        self.rect = pg.Rect(self.x, self.y, self.max_radius, self.max_radius)
        self.orient_x = 1 - 2*randint(0, 1)
        self.orient_y = 1 - 2*randint(0, 1)
        self.z = 2 + random()*width

    def update(self):
        self.sx = (width//2)*(self.x/self.z)
        self.sy = (height//2)*(self.y/self.z)
        self.r = (self.max_radius)*(1-self.z/width)
        self.rect = pg.Rect(width//2 - self.sx*self.orient_x, height //
                            2 - self.sy*self.orient_y, self.r, self.r)
        self.z -= self.star_speed
        if self.z < 2:
            self.x = random()*width//2
            self.y = random()*height//2
            self.sx = self.x
            self.sy = self.y
            self.rect.move_ip(self.sx, self.sy)
            self.orient_x = 1 - 2*randint(0, 1)
            self.orient_y = 1 - 2*randint(0, 1)
            self.z = 2 + random()*width

    def show(self):
        pg.draw.ellipse(starfield, white, self.rect)


# initialisation du décor pour la premiere partie
initialiser_decor()


def afficher_ecran_demarrage(state_trans):
    """Cette fonction affiche l'ecran de demarrage
    """
    starfield.fill(black)
    star = l_star[0]
    for star in l_star:
        star.update()
        star.show()
    fenetre.blit(starfield, (0, 0))
    fenetre.blit(titre_ecran_demarrage, rect_titre)
    etape = (1-2*((state_trans//255) % 2))
    alpha = ((state_trans) % 255) * etape
    if etape == -1:
        alpha = 255+alpha
    fenetre.blit(transparent(press_start, alpha), rect_press_start)


def defilement_decor():
    """Définition de la boucle qui va faire défiler le décor au premier plan.
    La vitesse de défilement est ajustable dans le fichier constant.py
    La fonction renvoie la valeur de abs_decor (l'entier relatif qui donne la position du bord de l'image de décor par rapport au bord de la fenetre visible)
    """
    global foregrnd
    global abs_decor

    if -foregrnd.topleft[0] >= x_bord_decor:
        foregrnd = foregrnd.move(-foregrnd.topleft[0], 0)
        abs_decor = 0
    else:
        foregrnd = foregrnd.move(-vitesse_decor, 0)
        abs_decor -= vitesse_decor
    fenetre.blit(image["long_foreground_relief"], foregrnd)
    return abs_decor


def afficher_vaisseau(ship):
    """ Cette fonction gere l'affichage du vaisseau sur l'ecran.
    Elle prend en argument ship qui est un objet de la classe 'Vaisseau'
    Elle ajuste aussi la taille de la flamme en fonction du deplacement relatif du vaisseau par rapport au decor
    """
    afficher_image(image["vaisseau"], ship.size,
                   ship.size, ship.rect.left, ship.rect.top)
    if ship.state == "accelerate":
        afficher_image(image["flamme"], ship.size,
                       ship.size, ship.rect.left, ship.rect.top, anchor="nw")
    elif ship.state == "static":
        afficher_image(image["flamme_faible"], ship.size,
                       ship.size, ship.rect.left, ship.rect.top, anchor="nw")


def afficher_ecran_fin():
    """Cette fonctin affiche l'ecran de fin de partie
    """
    fenetre.fill(black)
    fenetre.blit(titre_game_over, rect_game_over)
    fenetre.blit(play_again, rect_play_again)
    fenetre.blit(crochets, rect_crochets)


def afficher_et_update_enemy():
    """La fonction bouge et affiche les ennemis"""
    for enemy in l_enemy:
        enemy.move()
        enemy.shoot()
        afficher_image(image[enemy.type], enemy.size, enemy.size,
                       enemy.rect.left, enemy.rect.top)


def afficher_et_update_tir():
    """La fonction bouge et affiche les tirs"""
    for l in l_tir_vaisseau:
        l.move()
        l.update_duree()
        afficher_image(dico_image['tir_vaisseau'],
                       tir_size, tir_size, l.rect.left, l.rect.top)
    for l in l_tir_enemy:
        l.move()
        l.update_duree()
        afficher_image(dico_image['tir_ennemi'],
                       tir_size, tir_size, l.rect.left, l.rect.top)
    for l in l_missile_enemy:
        l.move()
        l.update_duree()
        afficher_image(dico_image["missile_ennemi"],
                       tir_size, tir_size, l.rect.left, l.rect.top)


# Mise a jour de l'image de decor pour la rendre transparente
image['long_foreground_relief'] = pg.transform.scale(
    image['long_foreground_relief'].convert_alpha(), (width_fg*ratio_decor, height))

# Dictionnaire des masques pour gérer les collisions
maskAsteroid = pg.mask.from_surface(pg.transform.scale(
    image["asteroide"].convert_alpha(), (asteroid_size, asteroid_size)))
maskShip = pg.mask.from_surface(pg.transform.scale(
    image["vaisseau"].convert_alpha(), (scale_size, scale_size)))
maskForegrnd = pg.mask.from_surface(image['long_foreground_relief'])
masks = {"asteroide": maskAsteroid,
         "vaisseau": maskShip, "foregrnd": maskForegrnd}
