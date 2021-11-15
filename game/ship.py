# Module ship du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *


class Vaisseau:
    def __init__(self):
        self.x = width//2
        self.y = height//2
        self.speed = 4
        self.size = 75
        self.state = "static"

    def move(self, direction):
        sq = sqrt(2)
        if direction == "n":
            self.y -= self.speed
        if direction == "s":
            self.y += self.speed
        if direction == "w":
            self.x -= self.speed
        if direction == "e":
            self.x += self.speed
        if direction == "ne":
            self.y -= self.speed/sq
            self.x += self.speed/sq
        if direction == "nw":
            self.y -= self.speed/sq
            self.x -= self.speed/sq
        if direction == "se":
            self.y += self.speed/sq
            self.x += self.speed/sq
        if direction == "sw":
            self.y += self.speed/sq
            self.x -= self.speed/sq


ship = Vaisseau()
