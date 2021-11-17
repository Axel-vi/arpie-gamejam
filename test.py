import game
from game.ship import *
from game.graphics import *

def move_test(n):
    speed = 4
    ship.rect.left = 0
    ship.rect.top = 0
    if n/4 < width:
        for i in range(n):
            ship.move('n')
        assert ship.rect.top == speed*n
        ship.rect.left = 0
        ship.rect.top = 0
        for j in range(n):
            ship.move('e')
        assert ship.rect.left == speed*n
        ship.rect.left = 0
        ship.rect.top = 0
        for i in range(n):
            ship.move('w')
        assert ship.rect.left == -(speed*n)
        ship.rect.left = 0
        ship.rect.top = 0
        for j in range(n):
            ship.move('s')
        assert ship.rect.top == 0
        ship.rect.left = 0
        ship.rect.top = 0
        for i in range(n):

    else :
        assert ship.rect.top == 0
        assert ship.rect.left == 0
    
    
        

    
    


