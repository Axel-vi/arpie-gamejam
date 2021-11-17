# SECTION TEST_ENEMY

from pygame.transform import scale
from game.enemy import *
from game.constant import *
from game.game import *
from game.ship import *
# from tests.test_enemy import *


def test_asteroid():
    asteroid = Asteroide()
    assert asteroid.speed >= 6
    assert asteroid.speed <= 10
    assert asteroid.y >= 0
    assert asteroid.y <= height
    assert asteroid.size == 90
    assert asteroid.rect == pg.Rect(width, asteroid.y, 90, 90)
    assert asteroid.target >= 0
    assert asteroid.target <= height
    assert asteroid.coeff == (asteroid.y-asteroid.target)/width
    assert asteroid.speed_x == -(sqrt(1/(1+asteroid.coeff**2))*asteroid.speed)
    assert asteroid.speed_y == asteroid.coeff*asteroid.speed_x
    assert asteroid in l_enemy
    assert asteroid.type == 'asteroide'


def test_move_asteroid():
    asteroid = Asteroide()
    x1 = asteroid.rect.left
    y1 = asteroid.rect.top

    asteroid.move()
    assert asteroid.rect.left == x1 + int(asteroid.speed_x)
    assert asteroid.rect.top == y1 + int(asteroid.speed_y)


def test_shoot_asteroid():
    asteroid = Asteroide()
    assert asteroid.shoot() == None


def test_tir_enemy():
    tir = tir_enemy(5, 5)
    assert tir.rect.left == 5
    assert tir.rect.top == 5
    assert tir.rect.size == (tir_size, tir_size)
    assert tir.duree == duree_tir
    assert tir in l_tir_enemy
    assert tir.angle == atan((ship.rect.centery-5) /
                             (ship.rect.centerx-5))
    assert tir.speed in [-speed_tir_enemy, speed_tir_enemy]


def test_move_tir_enemy():
    tir = tir_enemy(5, 5)
    tir.move()
    assert tir.rect.left == 5 - speed_tir_enemy
    assert tir.rect.top == 5


def test_update_duree_tir_enemy():
    tir = tir_enemy(5, 5)
    d = tir.duree
    tir.update_duree()
    assert tir.duree == d-1
    for k in range(len(l_tir_enemy)):
        l_tir_enemy[k] = '0'
    K = l_tir_enemy.copy()
    for k in range(d-1):
        tir.update_duree()
    assert l_tir_enemy == K[1:]


def test_chromius_fighter():
    c = Chromius_fighter(5, 1)
    assert c.size == scale_size
    assert c.type == 'chromius_fighter'
    assert c.cooldown == 0
    assert c.id_pattern == 1
    assert c.hauteur == 5
    assert c.t == 0
    assert c.rect.left == width
    assert c.rect.top == 5
    assert c.rect.size == (scale_size, scale_size)
    assert c in l_enemy


def test_move_chromius_fighter():
    c = Chromius_fighter(5, 1)
    T = c.t
    c.move()
    assert c.t == T+1
    x, y = pattern(c.id_pattern, c.t, c.hauteur)
    assert c.rect == pg.Rect(x, y, c.size, c.size)


def test_shoot_chromius_fighter():
    c = Chromius_fighter(5, 1)
    c.shoot()
    assert c.cooldown == delai_tir_enemy
    assert tir_enemy(c.rect.left+c.size/5, c.rect.top+c.size/3) in l_tir_enemy
    c.shoot()
    assert c.cooldown == delai_tir_enemy-1


def test_missile_enemy():
    m = missile_enemy(5, 4)
    assert m.rect == pg.Rect(5, 4, tir_size, tir_size)
    assert m.duree == duree_tir
    assert m in l_missile_enemy


def test_move_missile_enemy():
    m = missile_enemy(5, 4)
    R = m.rect.move(speed_missile_enemy, 0)
    m.move()
    assert m.rect == R


def test_update_duree_missile_enemy():
    m = missile_enemy(5, 4)
    d = m.duree
    m.update_duree()
    assert m.duree == d
    for k in range(len(l_missile_enemy)):
        l_missile_enemy[k] = '0'
    K = l_missile_enemy.copy()

    for k in range(d-1):
        m.update_duree()
    assert l_missile_enemy == K[1:]
    # assert
    # if self.duree <= 0:
    #     l_missile_enemy.pop(0)


test_asteroid()  # Valide !
test_move_asteroid()  # Valide !
test_shoot_asteroid()  # Valide !

test_tir_enemy()  # Valide !
test_move_tir_enemy()  # Valide !
test_update_duree_tir_enemy()  # Valide!

test_chromius_fighter()  # Valide !
test_move_chromius_fighter()  # Valide !
test_shoot_chromius_fighter()  # Valide !

test_missile_enemy()  # Valide !
test_move_missile_enemy()  # Valide !

# SECTION TEST_SHIP


def test_detect_collision():  # A upgrade un peu peut etre?
    ship = Vaisseau()
    ship.rect = ship.rect.move((-ship.rect.left, -ship.rect.top))
    asteroid = Asteroide()
    tir = tir_enemy(5, 5)
    asteroid.rect = asteroid.rect.move(
        (-asteroid.rect.left+500, -asteroid.rect.top+500))
    tir.rect = tir.rect.move(
        (-tir.rect.left+500, -tir.rect.top+500))

    assert detect_collision(
        ship, [asteroid], [], abs_decor) == False
    assert detect_collision(
        ship, [], [tir], abs_decor) == False

    ship.rect = ship.rect.move((-ship.rect.left+640, -ship.rect.top+335))
    asteroid.rect = asteroid.rect.move(
        (-asteroid.rect.left+1280, -asteroid.rect.top+539))
    tir.rect = tir.rect.move(
        (-tir.rect.left+1280, -tir.rect.top+539))

    assert detect_collision(
        ship, [asteroid], [], abs_decor) == False
    assert detect_collision(
        ship, [], [tir], abs_decor) == False

    ship.rect = ship.rect.move((-ship.rect.left, -ship.rect.top))
    asteroid.rect = asteroid.rect.move(
        (-asteroid.rect.left, -asteroid.rect.top))
    tir.rect = tir.rect.move(
        (-tir.rect.left, -tir.rect.top))

    assert detect_collision(
        ship, [], [tir], abs_decor) == True
    detect_collision(
        ship, [asteroid], [], abs_decor) == True


# test_detect_collision()  # Valide !

# SECTION TEST_AFFICHAGE


# Test des patterns
# t = [i for i in range(301)]
# y = [pattern(12, i, 0)[1] for i in range(301)]
# plt.plot(t, y)
# plt.show()
