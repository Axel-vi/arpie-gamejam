"Module graphics du projet R-Type"
# -*- coding: utf-8 -*-

from game.constant import pg, white, width, height, image, clock, fps, BLEND_RGBA_MULT, QUIT, \
    KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_z, K_q, K_d, K_s, K_SPACE, random, randint, \
    nb_star, starfield, black, titre_ecran_demarrage, press_start, rect_press_start, rect_titre, \
    rect_crochets, rect_game_over, rect_play_again, x_bord_bg, vitesse_decor, l_enemy, x_bord_decor, \
    vitesse_bg, vitesse_mg, spriteSheetExplosion, l_explosion, titre_game_over, play_again, crochets, \
    tower_height, tower_width, l_missile_enemy, l_tir_enemy, l_tir_tower, l_tir_vaisseau, tir_size, \
    asteroid_size, scale_size, width_fg, width_bg, ratio_bg, ratio_decor, l_aff_niveau, l_rect_niveau, titre_victory, rect_next_level, \
    rect_score, rect_victory, next_level, score, l_chromius_lord,\
    size_chromius_lord

# Création de la fenêtre
fenetre = pg.display.set_mode((width, height))
fenetre.fill(white)
rectFenetre = fenetre.get_rect()

# Réglage de la fenetre
pg.display.set_caption("ARPIE")
pg.display.set_icon(image["chromius_lord"])


def quitter():
    """Fonction qui ferme pygame et python."""
    pg.quit()
    quit()


def transition(fenetre, couleur=white):
    """Fonction pour faire une transition d'un état à un autre avec une pause d'une demi-seconde.
    Affiche un écran de la couleur choisie pour les transitions.
    """
    time_left = fps//2
    while clock.tick(fps) and time_left > 0:
        time_left -= 1
        fenetre.fill(couleur)
        pg.display.update()


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


# Etoiles pour l'écran de démarrage


class Star():
    """Classe pour gérer les étoiles du fond de l'écran de démarrage"""

    def __init__(self):
        """Initialisation"""
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
        """Met à jour la position des étoiles et réintialise celles en dehors de l'écran"""
        self.sx = (width//2)*(self.x/self.z)
        self.sy = (height//2)*(self.y/self.z)
        self.r = (self.max_radius)*(1-self.z/width)
        self.rect = pg.Rect(width//2 - self.sx*self.orient_x, height //
                            2 - self.sy*self.orient_y, self.r, self.r)
        self.z -= self.star_speed
        # Reset de la position des étoiles lointaines
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
        """Gère l'affichage des étoiles sur la surface starfield"""
        pg.draw.ellipse(starfield, white, self.rect)

# Initialisation du décor


def initialiser_decor():
    """Fonction qui initialise le décor"""
    global foregrnd
    global abs_decor
    global l_star
    global foregrnd
    global abs_decor
    global backgrnd
    abs_decor = 0
    foregrnd = image["long_foreground_relief"].get_rect()
    backgrnd = image["background"].get_rect()
    l_star = []
    foregrnd = image["long_foreground_relief"].get_rect()
    for i in range(nb_star):
        l_star.append(Star())


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
    # Transparence du press start
    etape = (1-2*((state_trans//255) % 2))
    alpha = ((state_trans) % 255) * etape
    if etape == -1:
        alpha = 255+alpha
    fenetre.blit(transparent(press_start, alpha), rect_press_start)


def defilement_decor_background():
    """Définition de la boucle qui va faire défiler le décor au premier plan.
    La vitesse de défilement est ajustable dans le fichier constant.py
    La fonction renvoie la valeur de abs_decor (l'entier relatif qui donne la position du bord de l'image de décor par rapport au bord de la fenetre visible)
    """
    global backgrnd
    global middlegrnd

    if -backgrnd.topleft[0] >= x_bord_bg:
        backgrnd = backgrnd.move(-backgrnd.topleft[0], 0)
    else:
        backgrnd = backgrnd.move(-vitesse_bg, 0)

    if -middlegrnd.topleft[0] >= x_bord_decor:
        middlegrnd = middlegrnd.move(-middlegrnd.topleft[0], 0)
    else:
        middlegrnd = middlegrnd.move(-vitesse_mg, 0)

    fenetre.blit(image["background"], backgrnd)
    fenetre.blit(image['long_middleground_relief'], middlegrnd)


def defilement_decor_foreground():
    global foregrnd
    global abs_decor
    global backgrnd
    if -foregrnd.topleft[0] >= x_bord_decor:
        foregrnd = foregrnd.move(-foregrnd.topleft[0], 0)
        abs_decor = 0
    else:
        foregrnd = foregrnd.move(-vitesse_decor, 0)
        abs_decor -= vitesse_decor
    fenetre.blit(image["long_foreground_relief"], foregrnd)
    return abs_decor
# Initialisation du décor


def initialiser_decor():
    """Cette foncion initialise le décor
    """
    global foregrnd
    global middlegrnd
    global backgrnd
    global abs_decor
    global backgrnd
    abs_decor = 0
    middlegrnd = image['long_middleground_relief'].get_rect()
    backgrnd = image['background'].get_rect()
    foregrnd = image["long_foreground_relief"].get_rect()
    backgrnd = image["background"].get_rect()


# initialisation du décor pour la premiere partie
initialiser_decor()


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


def afficher_ecran_fin(transparence):
    """Cette fonctin affiche l'ecran de fin de partie
    """
    fenetre.fill(black)
    fenetre.blit(titre_game_over, rect_game_over)
    fenetre.blit(transparent(play_again, transparence), rect_play_again)
    fenetre.blit(crochets, rect_crochets)


def afficher_et_update_enemy(ship):
    """La fonction bouge et affiche les ennemis"""
    for enemy in l_enemy:
        enemy.move()
        enemy.shoot(ship)
        if enemy.type == 'chromius_tower':
            afficher_image(image[enemy.type], tower_width,
                           tower_height, enemy.rect.left, enemy.rect.top)
        else:
            afficher_image(image[enemy.type], enemy.size,
                           enemy.size, enemy.rect.left, enemy.rect.top)


def afficher_et_update_tir():
    """La fonction bouge et affiche les tirs"""
    for l in l_tir_vaisseau:
        l.move()
        l.update_duree()
        afficher_image(image['tir_vaisseau'],
                       tir_size, tir_size, l.rect.left, l.rect.top)
    for l in l_tir_enemy:
        l.move()
        l.update_duree()
        afficher_image(image['tir_ennemi'],
                       tir_size, tir_size, l.rect.left, l.rect.top)
    for l in l_missile_enemy:
        l.move()
        l.update_duree()
        afficher_image(image["missile_ennemi"],
                       tir_size, tir_size, l.rect.left, l.rect.top)
    for l in l_tir_tower:
        l.move()
        l.update_duree()
        afficher_image(image["tir_tower"],
                       tir_size, tir_size, l.rect.left, l.rect.top)


def afficher_et_update_explosion():
    for e in l_explosion:
        e.update()
        e.show()


def afficher_et_update_chromius_lord(ship, l_tir_vaisseau):
    for chromius_lord in l_chromius_lord:
        chromius_lord.move()
        chromius_lord.shoot(ship)
        chromius_lord.detect_collision(l_tir_vaisseau, masks)
        if chromius_lord.hitstun % 2 == 1:
            afficher_image(image['chromius_lord_white'], chromius_lord.size,
                           chromius_lord.size, chromius_lord.rect.left, chromius_lord.rect.top)
        else:
            afficher_image(image['chromius_lord'], chromius_lord.size,
                           chromius_lord.size, chromius_lord.rect.left, chromius_lord.rect.top)


# Mise a jour de l'image de decor pour la rendre transparente
image['long_foreground_relief'] = pg.transform.scale(
    image['long_foreground_relief'].convert_alpha(), (width_fg*ratio_decor, height))
image['background'] = pg.transform.scale(
    image['background'].convert_alpha(), (width_bg*ratio_bg, height))
image['long_middleground_relief'] = pg.transform.scale(
    image['long_middleground_relief'].convert_alpha(), (width_fg*ratio_decor, height))

# Dictionnaire des masques pour gérer les collisions
# A CHANGER
maskAsteroid = pg.mask.from_surface(pg.transform.scale(
    image["asteroide"].convert_alpha(), (asteroid_size, asteroid_size)))
maskShip = pg.mask.from_surface(pg.transform.scale(
    image["vaisseau"].convert_alpha(), (scale_size, scale_size)))
maskForegrnd = pg.mask.from_surface(image['long_foreground_relief'])
maskChromiusFighter = pg.mask.from_surface(pg.transform.scale(
    image["chromius_fighter"].convert_alpha(), (scale_size, scale_size)))
maskTirEnemy = pg.mask.from_surface(pg.transform.scale(
    image["tir_ennemi"].convert_alpha(), (tir_size, tir_size)))
maskTirShip = pg.mask.from_surface(pg.transform.scale(
    image["tir_vaisseau"].convert_alpha(), (tir_size, tir_size)))
maskChromiusWarrior = pg.mask.from_surface(pg.transform.scale(
    image["chromius_warrior"].convert_alpha(), (scale_size, scale_size)))
maskMissile = pg.mask.from_surface(pg.transform.scale(
    image["missile_ennemi"].convert_alpha(), (tir_size, tir_size)))
maskChromiusTower = pg.mask.from_surface(pg.transform.scale(
    image["chromius_tower"].convert_alpha(), (tower_width, tower_height)))
maskTirTower = pg.mask.from_surface(pg.transform.scale(
    image["tir_tower"].convert_alpha(), (tir_size, tir_size)))
maskChromiusLord = pg.mask.from_surface(pg.transform.scale(
    image["chromius_lord"].convert_alpha(), (size_chromius_lord, size_chromius_lord)))
masks = {"asteroide": maskAsteroid,
         "vaisseau": maskShip,
         "foregrnd": maskForegrnd,
         "chromius_fighter": maskChromiusFighter,
         "tir_enemy": maskTirEnemy,
         'tir_vaisseau': maskTirShip,
         'tir_tower': maskTirTower,
         'chromius_warrior': maskChromiusWarrior,
         'chromius_tower': maskChromiusTower,
         'missile': maskMissile,
         'chromius_lord': maskChromiusLord}


def afficher_niveau_en_cours(id_niveau):
    fenetre.blit(l_aff_niveau[id_niveau-1], l_rect_niveau[id_niveau-1])


def afficher_ecran_victoire():
    fenetre.fill(black)
    fenetre.blit(titre_victory, rect_victory)
    fenetre.blit(next_level, rect_next_level)
    fenetre.blit(score, rect_score)


class Explosion(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x, y, 16, 16)
        self.num = 0
        self.delta_time = 0
        self.image = spriteSheetExplosion.subsurface(pg.Rect(0, 0, 16, 16))
        self.numeroImage = 0
        l_explosion.append(self)

    def update(self):
        self.delta_time += 1
        if self.delta_time >= 3:
            self.delta_time = 0
            n = self.numeroImage
            self.image = spriteSheetExplosion.subsurface(
                pg.Rect(n*16, 0, 16, 16))
            self.numeroImage = self.numeroImage+1
            if self.numeroImage > 8:
                l_explosion.remove(self)

    def show(self):
        afficher_image(self.image, scale_size, scale_size,
                       self.rect.left, self.rect.top)
