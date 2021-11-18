# TEAM ARPIE GAMEJAM

<u> Projet R-Type: <u> <br>
Le but du projet est de créer un shooter spatial inspiré du jeu d'arcade R-Type. <br>
<br>
Les différentes étapes du projet sont disponibles dans le fichier TO_DO.txt <br>

<u> Liste des membres de l'équipe: <u>
- Ivan ROBERT
- Edy LAHOUD
- Gauthier DEBUISSCHERT
- Axel VISELTHIER
- Robin GONDEAU
- Paul CREUSY


<u> Instructions pour lancer le jeu et jouer: <u>
        Prérequis : - Avoir installé le module pygame (Voir https://www.pygame.org/wiki/GettingStarted "Pygame Installation")
                    - Disposer du fichier du jeu (le fichier "team-arpie-gamejam")
        
        Pour lancer le jeu: -Exécutez le script python RType.py

        Pour jouer: - Un écran de démarrage apparait, pour jouer pressez la barre espace.
                    - Déplacez le vaisseau en utilisant les flèches directionnelles ( ↑, ↓, ← ou →) ou les touches "z,q,s,d".
                    - Vous pouvez tirer en appuyant sur la barre espace.
                    - Pour survivre : évitez les collisions avec les éléments du décor et les ennemis (autres vaisseaux,astéroides,tours) et évitez les tirs des ennemis. Vous pouvez détruire les vaisseaux ennemis avec vos tirs mais pas les astéroides et éléments du décor.
                    - Si vous survivez assez longtemps vous passez au niveau suivant.
                    - Pour gagner : Atteignez la fin du niveau 5, dans ce cas le jeu est gagné et un écran de victoire apparait.
                    - En cas de mort : un écran "game over" s'affiche, vous pouvez reprendre au début de votre niveau en appuyant sur la barre espace ou quitter en appuyant sur la touche "échap" (ou en fermant la fenêtre de jeu).


<u> Structure du fichier:  <u>
-Le dossier game contient les fichiers python essentiels au lancement du jeu.
    -Le fichier constant.py contient les listes/paramètres constants qui peuvent être appelés dans les autres fichier python.
    -Le fichier enemy.py contient les fonctions définissant les diférents ennemis.
    -Le fichier game.py contient les fonctions qui gèrent les interactions entre des éléments du jeu (collisions) 
    -Le fichier graphics.py contient tout l'affichage.
    -Le fichier ship.py contient les fonctions liées au vaisseau du joueur.
    -Le fichier sound.py contient les fonctions de son et de bruitages.
-Le dossier data contient les éléments qui sont amenés à être stockés par le joueur (comme des scores/highscores).
-Le dossier ressources contient les éléments annexes nécéssaires au jeu (images,niveaux,sons).
-Le fichier test.py contient les tests de différentes fonction du coverage.
-Le fichier RType.py est le fichier principal qui permet de lancer le jeu et de gérer les différents états (écran d'accueil,jeu,écran de fin).
