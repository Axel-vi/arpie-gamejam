# SECTION TEST_ENEMY

from game.enemy import *
from game.constant import *
# from tests.test_enemy import *

"""
def test_asteroid():
    asteroid = Asteroide()
    assert asteroid.x == width
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


def test_move_rect_asteroid():
    asteroid = Asteroide()
    x1 = asteroid.rect.left
    y1 = asteroid.rect.top

    asteroid.move_rect()
    assert asteroid.rect.left == x1 + int(asteroid.speed_x)
    assert asteroid.rect.top == y1 + int(asteroid.speed_y)


test_asteroid()  # Valide !
test_move_rect_asteroid()  # Valide !

"""
# SECTION TEST_SHIP

# SECTION TEST_AFFICHAGE


# Test des patterns
t = [i for i in range(301)]
y = [pattern(12, i, 0)[1] for i in range(301)]
plt.plot(t, y)
plt.show()
