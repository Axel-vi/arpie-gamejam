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
Prérequis :
- Avoir installé le module pygame (Voir https://www.pygame.org/wiki/GettingStarted "Pygame Installation")
- Disposer du dossier contenant le jeu (le dossier "team-arpie-gamejam")
        
        Pour lancer le jeu: -Exécutez le script python RType.py

        Pour jouer: - Un écran de démarrage apparait, pour jouer presser la barre espace.
                    - Déplacer le vaisseau en utilisant les flèches directionnelles ( ↑, ↓, ← ou →) ou les touches "z,q,s,d".
                    - Vous pouvez tirer en appuyant sur la barre espace.
                    - Pour survivre : évitez les collisions avec les éléments du décor et les ennemis (autres vaisseaux,astéroides,tours) et évitez les tirs des ennemis. Vous pouvez détruire les vaisseaux ennemis avec vos tirs mais pas les astéroides et éléments du décor.
                    - Si vous survivez assez longtemps vous passez au niveau suivant.
                    - Pour gagner : Atteignez la fin du niveau 5.
                    - En cas de mort : un écran "game over" s'affiche, vous pouvez reprendre au début de votre niveau en appuyant sur la barre espace ou quitter en appuyant sur la touche "échap" (ou en fermant la fenêtre de jeu).

<u> Structure du fichier:  <u>
<ul>
<li>Le dossier game contient les fichiers python essentiels au lancement du jeu.</li>
<li>Le fichier constant.py contient les listes/paramètres constants qui peuvent être appelés dans les autres fichier python.</li>
<li>Le fichier enemy.py contient les fonctions définissant les diférents ennemis.</li>
<li>Le fichier game.py contient les fonctions qui gèrent les interactions entre des éléments du jeu (collisions).</li>
<li>Le fichier graphics.py contient tout l'affichage.</li>
<li>Le fichier ship.py contient les fonctions liées au vaisseau du joueur.</li>
<li>Le fichier sound.py contient les fonctions de son et de bruitages.</li>
<li>Le dossier data contient les éléments qui sont amenés à être stockés par le joueur (comme des scores/highscores).</li>
<li>Le dossier ressources contient les éléments annexes nécéssaires au jeu (images,niveaux,sons).</li>
<li>Le fichier test.py contient les tests de différentes fonction du coverage.</li>
<li>Le fichier RType.py est le fichier principal qui permet de lancer le jeu et de gérer les différents états (écran d'accueil,jeu,écran de fin).</li>