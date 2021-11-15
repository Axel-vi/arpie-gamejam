# Module sounds du projet R-Type
# -*- coding: utf-8 -*-

# Imports spécifiques
if __name__ == "__main__":
    from constant import *
else:
    from game.constant import *

# Création des objets liés au son
canal_musique = pg.mixer.Channel(0)
canal_musique.set_volume(volume_musique)
canal_son = pg.mixer.Channel(1)
canal_son.set_volume(volume_bruitage)
