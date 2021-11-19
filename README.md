# TEAM ARPIE GAMEJAM

<h1> Projet ARPIE: </h1>
<p>
Le but du projet est de créer un shooter spatial inspiré du jeu d'arcade R-Type.<br>
Les différentes étapes du projet sont disponibles dans le fichier TO_DO.txt </p>

<h2> Liste des membres de l'équipe: </h2>
<ul>
<li>Ivan ROBERT</li>
<li>Edy LAHOUD</li>
<li>Gauthier DEBUISSCHERT</li>
<li>Axel VISELTHIER</li>
<li>Robin GONDEAU</li>
<li>Paul CREUSY</li>
</ul>
<h2> Instructions pour lancer le jeu et jouer: </h2>
<h3>Prérequis :</h3>
<ul>
<li>Avoir installé le module pygame (Voir https://www.pygame.org/wiki/GettingStarted "Pygame Installation")</li>
<li>Disposer du dossier contenant le jeu (le dossier "team-arpie-gamejam")</li>
</ul>
<h3>Pour lancer le jeu:</h3>
<ul><li>Exécutez le script python r_type.py</li></ul>

<h3>Pour jouer:</h3>
<p>Un écran de démarrage apparait, pour jouer presser la barre espace.
<ul>
<li>Déplacer le vaisseau en utilisant les flèches directionnelles ( ↑, ↓, ← ou →) ou les touches "z,q,s,d".</li>
<li>Vous pouvez tirer en appuyant sur la barre espace.</li>
<li>Pour survivre : évitez les collisions avec les éléments du décor et les ennemis (autres vaisseaux,astéroides,tours) et évitez les tirs des ennemis. Vous pouvez détruire les vaisseaux ennemis avec vos tirs mais pas les astéroides et éléments du décor.</li>
<li>Si vous survivez assez longtemps vous passez au niveau suivant.</li>
<li>Pour gagner : Atteignez la fin du niveau 5 puis terrassez le Boss : Le Chromius Lord.</li>
<li>En cas de mort : un écran "game over" s'affiche, vous pouvez reprendre au début de votre niveau en appuyant sur la barre espace ou quitter en appuyant sur la touche "échap" (ou en fermant la fenêtre de jeu).</li>
</ul></p>

<h2> Structure du fichier:  </h2>
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
<li>Le fichier r_type.py est le fichier principal qui permet de lancer le jeu et de gérer les différents états (écran d'accueil,jeu,écran de fin).</li>
</ul>

<h2>Propriété intellectuelle</h2>
<p>
Tous les éléments de ce jeu, qu'il s'agisse du code, des graphismes ou de la musique ont été créés par les membres de l'équipe mentionnés plus haut à l'exception des éléments suivants:
</p>
<ul>
<li>La bibliothèque <a href='https://www.pygame.org/news'>pygame</a></li>
<li>Les modules os, random, math et matplotib</li>
<li>Les polices <a href='https://www.dafont.com/fr/open-24-display-st.font'>Open_24_Display</a> et <a href='https://www.dafont.com/fr/space-age.font'>Space Age</a></li>
<li>Les sons de tir, d'explosion, de game over et de victoire provenant du site <a href='https://www.sound-fishing.net/'>Sound Fishing</a></li>
</ul>
