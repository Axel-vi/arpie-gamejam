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
        self.speed = 4
        self.size = 75
        self.state = "static"
        self.rect = pg.Rect(width//2, height//2, self.size, self.size)

    def move(self, direction):
        """Déplace le vaisseau dans la direction voulue et change l'état des propulseurs en fonction du déplacement.
        """
        # Variables utiles
        sq = sqrt(2)
        x = 0
        y = 0
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
            y -= self.speed
        if direction == "s":
            y += self.speed
        if direction == "w":
            x -= self.speed
        if direction == "e":
            x += self.speed
        if direction == "ne":
            y -= self.speed/sq
            x += self.speed/sq
        if direction == "nw":
            y -= self.speed/sq
            x -= self.speed/sq
        if direction == "se":
            y += self.speed/sq
            x += self.speed/sq
        if direction == "sw":
            y += self.speed/sq
            x -= self.speed/sq
        # Retour à la postion précédente en cas de sortie de la fenetre
        self.rect = self.rect.move(x, y)
        if self.rect.right > width:
            self.rect = self.rect.move(-x, 0)
        if self.rect.left < 0:
            self.rect = self.rect.move(-x, 0)
        if self.rect.bottom > height:
            self.rect = self.rect.move(0, -y)
        if self.rect.top < 0:
            self.rect = self.rect.move(0, -y)


ship = Vaisseau()
