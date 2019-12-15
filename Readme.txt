Projet Python de Quentin Boulet, Sébastien Dos Santos

Fonctionnalité:
    - jeu directement lancable sur une map si elle est mis en parametre au lancement du programme:
        - ex: python3 main.py -m "map_test.txt"
        - python3 main.py -h (pour plus d'infos (il n'y en a pas plus))

    - Menu principal permettant:
        - lancer une map
        - lancer la derniere sauvegarde
        - lancer lediteur de map
        - lancer lediteur de personnage en cours de conception
        - animation incroyable

    - selection map:
        - selecteur de map
        - apercu de la map selectionné
        - affichage des scores
        - map aléatoire
        - map perso (permet de lancer une map non disponible par défaut)

    - derniere sauvegarde:
        - lance la map sauvegardé

    - editeur de map:
        - choix de la taille de la map
        - bloc disponible cliquable + touche permettant de poser les elements de la map
        - suppression d'element avec le clique droit
        - touche "echap" permet la sauvegarde de la map:
            - nom de la map
            - temps limite
            - diamant requis
        - touche "espace" pour quitter

    - editeur de personnage:
        - permet de creer son propre personnage
        - outil disponible: Cercle, Rectangle, Polygone (touche: "c", "r", "p")
        - lorsque la forme est selectionné, des croix se pose au niveau des cliques
            - --> clique droit pour valider la figure
                - nom perso pour la figure
                - choix des couleurs, epaisseur, remplissage
                    - pour couleurs et remplissage: "+" permet d'ouvrir la palette des couleurs
        - touche "espace" pour quitter

        Bientot disponible: 
            - sauvegarde de l'historique pour reouvrir en jeu le personnage
            - suppressions d'une figure a partir de son nom
    
    - EN JEU:
        - deplacement: fleche directionnelle
        - mode debug: touche "d"
        - menu: touche "echap"
            - continuer
            - sauvegarder la partie en cours
            - recommencer le niveau
            - quitter le jeu (permet de retourner au menu)
        - porte accessible uniquement lorsque le nombre de diamant requis a été atteint (clé dans la main)
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
            - animation God Tier
        - torche dans la main permettant de voir (car nous sommes dans une grottes ce qui implique aucune lumière)
            - (possibilité d'allumer la lumière dans la grotte bientot disponible ? pour les tricheurs)

Graphisme:
    - Entièrement fait main par Léonard de Vinci souvent appelé Quentin

Choix technique:
    - la simplicité quand elle est possible
    - une Magie Noire souvent utilisé pour plus de beau jeu
