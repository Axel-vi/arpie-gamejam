# SECTION TEST_ENEMY

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
    assert asteroid.rect.center == (width + 90/2, asteroid.y + 90/2)
    assert asteroid.target >= 0
    assert asteroid.target <= height
    assert asteroid.speed_x == -(sqrt(1/(1+asteroid.coeff**2))*asteroid.speed)
    assert asteroid.speed_y == asteroid.coeff*asteroid.speed_x
    assert asteroid in l_enemy


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
    assert tir.rect.size == (larg_tir, long_tir)
    assert tir.duree == duree_tir
    assert tir in l_tir_enemy


def test_move_tir_enemy():
    tir = tir_enemy(5, 5)
    tir.move()
    assert tir.rect.left == 5 + speed_tir_enemy
    assert tir.rect.top == 5


test_asteroid()  # Valide !
test_move_asteroid()  # Valide !
test_shoot_asteroid()  # Valide !

test_tir_enemy()  # Valide !
test_move_tir_enemy()  # Valide!

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


test_detect_collision()  # Valide !

# SECTION TEST_AFFICHAGE


# Test des patterns
t = [i for i in range(301)]
y = [pattern(12, i, 0)[1] for i in range(301)]
plt.plot(t, y)
plt.show()
