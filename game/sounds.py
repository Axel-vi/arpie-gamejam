"Module sounds du projet R-Type"
# -*- coding: utf-8 -*-

from game.constant import pg, volume_bruitage, volume_musique, dico_musique, dico_bruitages

# Création des objets liés au son
canal_musique = pg.mixer.Channel(0)
canal_musique.set_volume(volume_musique)
canal_son = pg.mixer.Channel(1)
canal_son.set_volume(volume_bruitage)


def son_game_over():
    canal_musique.stop()
    canal_musique.play(dico_musique['son_game_over'])


def musique_victoire():
    canal_musique.play(dico_musique['musique_victoire'])


def tir_laser():
    canal_son.play(dico_bruitages['tir_laser'])


def explosion():
    canal_son.play(dico_bruitages['explosion'])


def musique_jeu():
    canal_musique.play(dico_musique['musique_jeu'], 1)
