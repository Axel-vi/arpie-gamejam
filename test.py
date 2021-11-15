from _typeshed import Self
import game
from game.ship import *

def move_test():
    speed = 4
    assert ship.move(Self, 'n') == Self.y + speed
    assert ship.move(Self, 's') == Self.y - speed
    assert ship.move(Self, 'e') == Self.x + speed
    assert ship.move(Self, 'w') == Self.x - speed

move_test()

