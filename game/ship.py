# Module ship du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

x_vaisseau = width//2
y_vaisseau = height//2
speed = 3


def move_ship(direction):
    global x_vaisseau
    global y_vaisseau
    if direction == "n":
        y_vaisseau -= speed
    if direction == "s":
        y_vaisseau += speed
    if direction == "w":
        x_vaisseau -= speed
    if direction == "e":
        x_vaisseau += speed
    if direction == "ne":
        y_vaisseau -= speed/sqrt(2)
        x_vaisseau += speed/sqrt(2)
    if direction == "nw":
        y_vaisseau -= speed/sqrt(2)
        x_vaisseau -= speed/sqrt(2)
    if direction == "se":
        y_vaisseau += speed/sqrt(2)
        x_vaisseau += speed/sqrt(2)
    if direction == "sw":
        y_vaisseau += speed/sqrt(2)
        x_vaisseau -= speed/sqrt(2)
    return x_vaisseau, y_vaisseau
