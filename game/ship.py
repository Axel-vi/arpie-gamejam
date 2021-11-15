# Module ship du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *


class Vaisseau:
    """Classe utilisée pour gérer le vaisseau contrôlé par le joueur.
    """

    def __init__(self):
        self.x = width//2
        self.y = height//2
        self.speed = 4
        self.size = 75
        self.state = "static"

    def move(self, direction):
        """Déplace le vaisseau dans la direction voulue et change l'état des propulseurs en fonction du déplacement.
        """
        # Variables utiles
        sq = sqrt(2)
        old_x = self.x
        old_y = self.y
        # Changement d'état des propulseurs
        if direction == False:
            self.state = "static"
        elif "e" in direction:
            self.state = "accelerate"
        elif "w" in direction:
            self.state = "decelerate"
        else:
            self.state = "static"
        # Application du déplacement
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
        # Retour à la postion précédente en cas de sortie de la fenetre


ship = Vaisseau()
