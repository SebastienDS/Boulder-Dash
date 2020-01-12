Projet Python de Quentin Boulet, Sébastien Dos Santos

Fonctionnalité:
    - jeu directement lancable sur une map si elle est mis en parametre au lancement du programme:
           - ex: python3 main.py -m map_test.txt
    - jeu lancable avec un personnage personnalisé:
        - ex: python3 main.py -p test
    - jeu lancable sans restriction de lumiere:
        - ex: python3 main.py -l
    - ces arguments peuvent etre combiné:
        - ex: python3 main.py -m map_test.txt -p test -l 
    - python3 main.py -h (pour plus d'infos)

    - Menu principal permettant:
        - lancer une map
        - lancer la derniere sauvegarde
        - lancer l'editeur de map
        - lancer l'editeur de personnage 
        - animation afin de rendre le menu plus dynamique

    - selection map:
        - selecteur de map
        -nom map séléctionné
        - apercu de la map selectionné
        - affichage des scores
        - map aléatoire
        - recherche qui permet de lancer une map sans la chercher avec les flèches
        (nom des maps print dans la console)

    - derniere sauvegarde:
        - lance la map sauvegardé

    - editeur de map:
        - choix de la taille de la map
        - bloc disponible cliquable + touche permettant de poser les elements de la map
        - suppression d'element avec le clique droit
        - touche "s" ou bouton sauvegarder permet la sauvegarde de la map:
            - nom de la map
            - temps limite
            - diamant requis
        - touche "echap" ou bouton retour pour quitter

    - editeur de personnage:
        - permet de creer son propre personnage
        - outil disponible: Cercle, Rectangle, Polygone (touche: "c", "r", "p"), clé et torche
        - lorsque la forme est selectionné, des croix se pose au niveau des cliques
            - --> clique droit pour valider la figure
                - nom perso pour la figure
                - choix des couleurs, epaisseur, remplissage
                    - pour couleurs et remplissage: "+" permet d'ouvrir la palette des couleurs
        - touche "echap" pour quitter ou bouton quitter
        - sauvegarde de l'historique pour reouvrir en jeu le personnage avec la touche "s" ou bouton sauvegarder
        - suppressions d'une figure a partir de son nom avec la touche "enter" ou bouton supprimer
        - suppressions de la derniere figure avec la touche "retour (backspace)" ou bouton supprimer
    
    - EN JEU:
        - deplacement: fleche directionnelle
        - mode debug: touche "d"
        - mode pathfinding : touche "p"
        - menu: touche "echap"
            - continuer
            - sauvegarder la partie en cours
            - recommencer le niveau
            - quitter le jeu (permet de retourner au menu)
        - porte accessible uniquement lorsque le nombre de diamant requis a été atteint (clé dans la main) et ouverture de la porte
        si clé plus direction porte(change la porte en escalier)
        - perd si il n'y a plus de temps
        - lorsqu'on gagne:
            - affichage des scores
                - possibilité de rentrer son nom si il fait parti du top 3 des temps sur la map
            - menu de victoire:
                - score
                - bouton retry
                - bouton menu
        - lorsqu'on perd:
            - menu defaite
        - pierre et diamant peuvent tomber avec chute en cascade si les conditions sont réuni:
            - animation et effet de vitesse
        - torche dans la main permettant de voir (car nous sommes dans une grottes ce qui implique aucune lumière)
        - charbon pour augmenter porter de la lumière qui diminue au cours du temps

Graphisme:
    - Entièrement fait main sans importer d'image, seulement avec les fonctions graphique de upemtk.

Choix technique:
    -Nous avons décider de répartir le code en 6 modules afin de trouver les parties qui nous interesse,
    il ya le module main qui lance le menu et le jeu, le module fonction ou se trouve toute les parties techniques,
    le module esthetique qui comporte tout l'affichage du jeu et le module variable qui stock certaine variable
    importante dans un dictionnaire et les 2 modules d'éditeur.
    -Afin de ne pas copier coller de if, nous avons décider de changer les 4 if par un dictionnaire qui a
    pour chaque valeur de position possible, ce quel fait (exemple: "Left":(-1,0)). Cela permet de réduire considérablement
    le code.
    -Pour l'affichage, nous avons aussi utiliser un dictionnaire ou une lettre a pour valeur un nom de fonction('R' : Rockford) et
    l'écran bouge afin de laisser le personnage principale au milieu, on parcours la matrice et affichons les élément du bas vers le haut afin qu'une pierre ou 
    qu'un diamant ne tombe pas instantanément.
    -Pour changer de mode, nous avons des numéros qui sont ensuite mis dans un fichier texte memo afin de ne pas se perdre
    par exemple quitter le jeu = -1.
    -La map est créer à partir d'un fichier qui devient une matrice, on peut donc ajouter des maps externes si elles ont le bon format( même lettre et bonne position des
    différents éléments(temps+diamand puis map puis meilleurs scores puis score de commencement puis nom map puis temps lumière))
    -Pour sauvegarder, nous mettons la matrice carte dans un nouveau fichier texte qui a le meme format que cité précédemment sauf que score de commencement
    sera le score que le joueur avait avant de sauvegarder.
    -Pour tout ce qui est déplacement des pierre et diamants, une boucle parcours la map et si l'élément est une pierre ou un diamant, un if vérifie
    toutes les conditions et fais le déplacement.
    -Pour faire qu'un pierre ne tue pas instantanément Rockford, nous avons différencié une pierre qui tombe d'une pierre qui ne tombais pas(lettre
    et affichage différent).
    -Pour vérifier si un joueur à perdu ou a gagner, nous avons fait deux fonctions qui lance leur propre menu.
    -Pour choisir son pseudo, nous avons une fonction qui fonctionne comme un input mais graphique.
    -Pour sauvegarder les meilleurs scores, nous avons mis les meilleurs scores dans les fichiers des maps et nous regardons si le score de fin de partie
    bat l'un des 3 meilleurs scores et remplaçons en fonction duquel c'est.
    

 
