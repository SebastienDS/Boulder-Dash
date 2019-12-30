import upemtk
from variable import var, _touche
import editeur_personnage
import esthetique
from random import choice, randint
from time import time
from copy import deepcopy
import os


# on associe les lettres aux fonctions les dessinant
dico = {
    "G": esthetique.terre,
    "P": esthetique.pierre,
    "R": esthetique.rockford,
    "W": esthetique.mur,
    "D": esthetique.diamand,
    "E": esthetique.sortie,
    ".": lambda *args: None,
    "K": esthetique.pierre_eboulement,
    "C": esthetique.diamand_eboulement,
    "F": esthetique.mur,
    "L": esthetique.charbon,
}


def creer_map(nomdufichier):
    """
    Transforme un fichier texte contenant une map en une matrice

    :param str nomdufichier: nom de la map a lire
    :return: donnees extraites du fichier
    """
    with open(
        "map/" + nomdufichier, "r"
    ) as fichier:  # ouvre le fichier contenant la carte
        contenu = fichier.read()  # lis le fichier
        contenu = contenu.split(
            "\n"
        )  # Construit une matriche de la carte /chaque ligne = chaine de caractère
        ted = contenu.pop(0)  # Enlève le temps et nombre de diamands
        ted = ted.split()
        t = ted[0][:-1]
        d = ted[1][:-1]
        while contenu[-1] == "":
            contenu.pop()
        tempslumiere = contenu.pop()
        nommap = contenu.pop()
        score4 = (
            contenu.pop()
        )  # score actuelle ("00000000" de base puis autre quand partie sauvegardé)
        score3 = contenu.pop()
        score2 = contenu.pop()
        score1 = contenu.pop()
        for i in range(len(contenu)):
            contenu[i] = list(
                contenu[i]
            )  # transforme la chaine de caractère en une list('abc'=['a','b','c'])
    return contenu, t, d, score1, score2, score3, score4, nommap, time() - int(float(tempslumiere))


def save_map_en_cours(
    carte,
    nb_diamand,
    score,
    temps_restant,
    nommap,
    tempslumiere,
    nom_sauvegarde="map_sauvegarde",
    aleatoire=False
):
    """
    sauvegarde la map

    :param list carte: liste 2D contenant le jeu
    :param int nb_diamand: nombre de diamant a sauvegarder dans le fichier
    :param int temps_restant: temps restant de la partie
    :param str nommap: nom de la map en cours de jeu a sauvegarder (permet de savoir de quelle map on vient lors d'un futur retry)
    :param int tempslumiere: temps restant de lumiere
    :param str nom_sauvegarde: nom du fichier
    :param bool aleatoire: sauvegarde des scores par defaut si la map est aleatoire
    """
    with open("map/{}.txt".format(nom_sauvegarde), "w") as f:
        f.write("{}s {}d\n".format(temps_restant, nb_diamand))
        for j in range(len(carte)):
            for i in range(len(carte[0])):
                f.write(carte[j][i])
            f.write("\n")
        for i in range(1, 4):
            if not aleatoire:
                f.write("{}\n".format(var["score{}".format(i)]))
            else:
                f.write("personne = 00000000\n")
        f.write("{}\n".format(score))
        f.write("{}\n".format(nommap))
        f.write("{}\n".format(tempslumiere))


def timer(tempstotal, tempscommencement):
    """
    temps restant de la partie
    
    :param int tempstotal: temps deja ecoule dans la partie 
    :param int tempscommencement: temps depuis le debut de la partie
    :return: temps restant de la partie
    """
    return tempstotal - (int(time() - tempscommencement))


def affichage(carte, nbdiamand, diamand, tempslumiere):
    """
    Affiche la carte
    
    :param list carte: liste 2D contenant le jeu
    :param int nb_diamand: nombre de diamant deja recupere en jeu
    :param int diamand: nombre de diamant requis avant de pouvoir gagner
    :param int tempslumiere: temps restant de lumiere
    """
    esthetique.fond("black")
    if time() - tempslumiere < 0:
        esthetique.lumiere(0)
    else:
        esthetique.lumiere(time() - tempslumiere)
    if var["porte"] == 0:
        esthetique.lumiere_escalier()
    carte[2][0] = "F"

    for y in range(len(carte) - 1, -1, -1):  # y = ligne
        for x in range(len(carte[y]) - 1, -1, -1):  # x = colonne
            if carte[y][x] == "R" and var["personnage"]:
                if var["personnage"]:
                    for elem in var["forme_personnage"].values():
                        copy_elem = deepcopy(elem)
                        if elem[1] == "R":
                            copy_elem[2] += var["dimension_fenetre"] // 2
                            copy_elem[4] += var["dimension_fenetre"] // 2
                            copy_elem[3] += var["dimension_fenetre"] // 2
                            copy_elem[5] += var["dimension_fenetre"] // 2

                        elif elem[1] == "C":
                            copy_elem[2] += var["dimension_fenetre"] // 2
                            copy_elem[3] += var["dimension_fenetre"] // 2

                        elif copy_elem[1] == "P":
                            for i in range(len(copy_elem[2])):
                                copy_elem[2][i] = (
                                    copy_elem[2][i][0] + var["dimension_fenetre"] // 2,
                                    copy_elem[2][i][1] + var["dimension_fenetre"] // 2,
                                )
                        editeur_personnage.forme_possible[copy_elem[1]][1](
                            *copy_elem[2:]
                        )
            else:
                dico[carte[y][x]](
                    x + (var["nb_cases"] // 2 - var["pos_x"]),
                    y + (var["nb_cases"] // 2 - var["pos_y"]),
                    var["taille_case"],
                    nbdiamand,
                    diamand,
                    "goldenrod3",
                )  # centre le perso

    if not var["lumiere"]:
        if 400 + (time() - tempslumiere) * 5 < 350:
            esthetique.noir_lumiere(350)
        else:
            esthetique.noir_lumiere(400 + (time() - tempslumiere) * 5)


def fond_score_temps_diams(score, tempsrestant, nbdiamand, diamand):
    """
    Affiche une banderolle avec le score le temps et le nombre de diamand restant
    
    :param str score: score de la partie
    :param int tempsrestant: temps restant de la partie
    :param int nb_diamand: nombre de diamant deja recupere en jeu
    :param int diamand: nombre de diamant requis avant de pouvoir gagner
    """
    nbdiamandrestant = diamand - nbdiamand
    if nbdiamandrestant < 0:
        nbdiamandrestant = 0
    esthetique.fond_score_temps_diams(score, tempsrestant, nbdiamandrestant)


def tomber_de_pierre_ou_diamand(carte):
    """
    Fais tomber les pierres

    :param list carte: liste 2D contenant le jeu

    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "R", "K", "W"], 
    ...     ["W", "E", ".", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> tomber_de_pierre_ou_diamand(carte)
    >>> print(carte)
    [['W', 'W', 'W', 'W'], ['W', 'R', '.', 'W'], ['W', 'E', 'K', 'W'], ['W', 'W', 'W', 'W']]
    """
    for y in range(len(carte) - 2, -1, -1):
        for x in range(len(carte[0]) - 1, -1, -1):
            if carte[y][x] == "K" and carte[y + 1][x] == ".":
                carte[y][x], carte[y + 1][x] = ".", "K"
            if carte[y][x] == "C" and carte[y + 1][x] == ".":
                carte[y][x], carte[y + 1][x] = ".", "C"


def test_si_pierre_va_tomber(carte):
    """
    test si une pierre va tomber et la transforme en une pierre 
    qui tombe si oui (pareil pour diams)
    
    :param list carte: liste 2D contenant le jeu
    
    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "P", "D", "W"], 
    ...     ["W", ".", ".", "W"],
    ...     ["W", "E", "R", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> test_si_pierre_va_tomber(carte)
    >>> print(carte)
    [['W', 'W', 'W', 'W'], ['W', 'K', 'C', 'W'], ['W', '.', '.', 'W'], ['W', 'E', 'R', 'W'], ['W', 'W', 'W', 'W']]
    """
    for y in range(len(carte) - 2, -1, -1):
        for x in range(len(carte[0]) - 1, -1, -1):
            if carte[y][x] == "P" and carte[y + 1][x] == ".":
                carte[y][x] = "K"
            if carte[y][x] == "D" and carte[y + 1][x] == ".":
                carte[y][x] = "C"


def test_pierre_ou_diamand_eboulement(carte):
    """
    test si une pierre est toujours en train de tomber 
    et la transforme en pierre normal si non (pareil pour diams)
    
    :param list carte: liste 2D contenant le jeu
    
    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", ".", ".", "W"], 
    ...     ["W", "K", "C", "W"],
    ...     ["W", "E", "R", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> test_pierre_ou_diamand_eboulement(carte)
    >>> print(carte)
    [['W', 'W', 'W', 'W'], ['W', '.', '.', 'W'], ['W', 'P', 'C', 'W'], ['W', 'E', 'R', 'W'], ['W', 'W', 'W', 'W']]
    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "R", ".", "W"], 
    ...     ["W", "K", "C", "W"],
    ...     ["W", "E", "W", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> test_pierre_ou_diamand_eboulement(carte)
    >>> print(carte)
    [['W', 'W', 'W', 'W'], ['W', 'R', '.', 'W'], ['W', 'P', 'D', 'W'], ['W', 'E', 'W', 'W'], ['W', 'W', 'W', 'W']]
    """
    for y in range(len(carte) - 1):
        for x in range(len(carte[0])):
            if carte[y][x] == "K" and carte[y + 1][x] not in [".", "R"]:
                carte[y][x] = "P"
            if carte[y][x] == "C" and carte[y + 1][x] not in [".", "R"]:
                carte[y][x] = "D"


def test_deplacement(carte, direction, liste):
    """
    test si le deplacement est possible
    
    :param list carte: liste 2D contenant le jeu
    :param str direction: ["Up", "Down", "Left", "Right")
    :param list liste: contient les elements permettant le deplacement
    :return: bool

    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "R", ".", "W"], 
    ...     ["W", ".", ".", "W"],
    ...     ["W", "E", "W", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> var["pos_x"] = 1
    >>> var["pos_y"] = 1 
    >>> choix = ["Up", "Down", "Left", "Right"]
    >>> test_deplacement(carte, choix[3], {"G", ".", "D"})
    True
    >>> test_deplacement(carte, choix[0], {"G", ".", "D"})
    False
    """
    return (
        carte[var["pos_y"] + _touche[direction][1]][
            var["pos_x"] + _touche[direction][0]
        ]
        in liste
    )


def enleve_porte(carte, ev, nbdiamand, diamand):
    """
    test si la porte a été ouverte
    
    :param list carte: liste 2D contenant le jeu
    :param upemtk.Event ev: evenement recupere par upemtk.donne_evenement()
    :param int nb_diamand: nombre de diamant deja recupere en jeu
    :param int diamand: nombre de diamant requis avant de pouvoir gagner
    """
    type_ev = upemtk.type_evenement(ev)
    if type_ev == "Touche":
        t = upemtk.touche(ev)
        if t in _touche:
            if (
                carte[var["pos_y"] + _touche[t][1]][var["pos_x"] + _touche[t][0]]
                == carte[var["pos_sortie_y"]][var["pos_sortie_x"]]
                and nbdiamand >= diamand
            ):
                var["porte"] = 0


def deplace(carte, t):
    """
    se deplace dans la direction voulu et met a jour les positions du joueur

    :param list carte: liste 2D contenant le jeu
    :param str t: ("Up", "Down", "Left", "Right")

    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "R", ".", "W"], 
    ...     ["W", ".", ".", "W"],
    ...     ["W", "E", "W", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> var["pos_x"] = 1
    >>> var["pos_y"] = 1 
    >>> choix = ["Up", "Down", "Left", "Right"]
    >>> deplace(carte, choix[1])
    >>> print(carte)
    [['W', 'W', 'W', 'W'], ['W', '.', '.', 'W'], ['W', 'R', '.', 'W'], ['W', 'E', 'W', 'W'], ['W', 'W', 'W', 'W']]
    >>> var["pos_y"] == 2
    True
    """
    carte[var["pos_y"] + _touche[t][1]][var["pos_x"] + _touche[t][0]] = "R"
    carte[var["pos_y"]][var["pos_x"]] = "."
    var["pos_x"] += _touche[t][0]
    var["pos_y"] += _touche[t][1]


def deplacer_perso(carte, nbdiamand, ev, diamand, tempstotal, score, tempslumiere):
    """
    Test si le perso peut se deplacer, si oui, 
    deplace le perso sur la carte en fonction de la touche utilisé
    
    :param list carte: liste 2D contenant le jeu
    :param int nb_diamand: nombre de diamant deja recupere en jeu
    :param upemtk.Event ev: evenement recupere par upemtk.donne_evenement()
    :param int diamand: nombre de diamant requis avant de pouvoir gagner
    :param int tempstotal: temps restant de la partie
    :param str score: score de la partie
    :param int tempslumiere: restant de lumiere restant
    :return: nbdiamand, tempstotal, score, tempslumiere
    """
    type_ev = upemtk.type_evenement(ev)
    if type_ev == "Touche":
        t = upemtk.touche(ev)
        if t in _touche:
            if test_deplacement(carte, t, "D"):
                deplace(carte, t)
                return (
                    nbdiamand + 1,
                    int(tempstotal) + 10,
                    (8 - len((str(int(score) + 350)))) * "0" + (str(int(score) + 350)),
                    tempslumiere,
                )
            if test_deplacement(carte, t, "L"):
                deplace(carte, t)
                return nbdiamand, tempstotal, score, tempslumiere + 10
            elif test_deplacement(carte, t, {"G", ".", "F"}):
                deplace(carte, t)
                return nbdiamand, tempstotal, score, tempslumiere
            if (
                nbdiamand >= diamand
                and test_deplacement(carte, t, "E")
                and var["porte"] == 0
            ):
                deplace(carte, t)
                return nbdiamand, tempstotal, score, tempslumiere
    return nbdiamand, tempstotal, score, tempslumiere


def tomber_pierre_laterale(carte):
    """
    test si une pierre peut tomber sur les cotés et la bouge si oui

    :param list carte: liste 2D contenant le jeu
    :return: carte

    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "D", ".", "W"], 
    ...     ["W", "P", ".", "W"],
    ...     ["W", "E", "R", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> tomber_pierre_laterale(carte)
    [['W', 'W', 'W', 'W'], ['W', '.', 'D', 'W'], ['W', 'P', '.', 'W'], ['W', 'E', 'R', 'W'], ['W', 'W', 'W', 'W']]
    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "P", ".", "W"], 
    ...     ["W", "P", ".", "W"],
    ...     ["W", "E", "R", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> tomber_pierre_laterale(carte)
    [['W', 'W', 'W', 'W'], ['W', '.', 'P', 'W'], ['W', 'P', '.', 'W'], ['W', 'E', 'R', 'W'], ['W', 'W', 'W', 'W']]
    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "P", ".", "W"], 
    ...     ["W", "P", "P", "W"],
    ...     ["W", "E", "R", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> tomber_pierre_laterale(carte)
    [['W', 'W', 'W', 'W'], ['W', 'P', '.', 'W'], ['W', 'P', 'P', 'W'], ['W', 'E', 'R', 'W'], ['W', 'W', 'W', 'W']]
    >>> carte = [
    ...     ["W", "W", "W", "W"], 
    ...     ["W", "P", ".", "W"], 
    ...     ["W", "G", ".", "W"],
    ...     ["W", "E", "R", "W"], 
    ...     ["W", "W", "W", "W"]]
    >>> tomber_pierre_laterale(carte)
    [['W', 'W', 'W', 'W'], ['W', 'P', '.', 'W'], ['W', 'G', '.', 'W'], ['W', 'E', 'R', 'W'], ['W', 'W', 'W', 'W']]
    """
    for y in range(len(carte) - 2, 0, -1):
        for x in range(len(carte[0]) - 2, 0, -1):
            if (
                carte[y][x] in ["P", "D"]
                and carte[y][x + 1] == "."
                and carte[y + 1][x + 1] == "."
                and carte[y + 1][x] in ["P", "D", "W"]
            ):
                carte[y][x], carte[y][x + 1] = ".", carte[y][x]
            if (
                carte[y][x] in ["P", "D"]
                and carte[y][x - 1] == "."
                and carte[y + 1][x - 1] == "."
                and carte[y + 1][x] in ["P", "D", "W"]
            ):
                carte[y][x], carte[y][x - 1] = ".", carte[y][x]
    return carte


def test_pousser_pierre(carte, ev):
    """
    test si une pierre peut etre poussé et return true or false selon le résultat
    
    :param list carte: liste 2D contenant le jeu
    :param upemtk.Event ev: evenement recupere par upemtk.donne_evenement()
    :return: bool
    """
    type_ev = upemtk.type_evenement(ev)
    if type_ev == "Touche":
        t = upemtk.touche(ev)
        if (
            t == "Right"
            and carte[var["pos_y"]][var["pos_x"] + 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] + 2] == "."
        ):
            return True
        if (
            t == "Left"
            and carte[var["pos_y"]][var["pos_x"] - 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] - 2] == "."
        ):
            return True
    return False


def pousser_pierre(carte, t):
    """
    Test si une pierre est poussable, si oui, la pousse

    :param list carte: liste 2D contenant le jeu
    :param str t: ("Up", "Down", "Left", "Right")

    >>> carte = [
    ...     ["W", "W", "W", "W", "W", "W", "W"], 
    ...     ["W", ".", "P", "R", "P", ".", "W"], 
    ...     ["W", ".", "P", "E", "P", ".", "W"],
    ...     ["W", "W", "W", "W", "W", "W", "W"]]
    >>> var["pos_x"] = 3
    >>> var["pos_y"] = 1 
    >>> choix = ["Up", "Down", "Left", "Right"]
    >>> pousser_pierre(carte, choix[3])
    >>> carte[var["pos_y"]][var["pos_x"] + 1] == "."
    True
    >>> carte[var["pos_y"]][var["pos_x"] + 2] == "P"
    True
    """
    (
        carte[var["pos_y"]][var["pos_x"] + _touche[t][0]],
        carte[var["pos_y"]][var["pos_x"] + 2 * _touche[t][0]],
    ) = (".", "P")


def loose(carte, tempsrestant):
    """
    test si joueur s'est pris une pierre 
    si oui met l'image de défaite et retourne True
    
    :param list carte: liste 2D contenant le jeu
    :param int tempsrestant: temps restant de la partie en cours
    :return: bool
    """
    if carte[var["pos_y"] - 1][var["pos_x"]] in ["K", "C"] or tempsrestant <= 0:
        upemtk.efface_tout()
        esthetique.fond("black")
        esthetique.personnage_defaitiste()
        upemtk.texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 4,
            "DÉFAITE !",
            couleur="red",
            ancrage="center",
            taille=75,
        )
        return True
    return False


def win(nbdiamand, diamand, tempsrestant, cartes, score, nommap):
    """
    Regarde si l'utilisateur gagne si oui, met l'image de victoire et retourne True
    
    :param int nb_diamand: nombre de diamant deja recupere en jeu
    :param int diamand: nombre de diamant requis avant de pouvoir gagner
    :param int tempsrestant: temps restant de la partie en cours
    :param cartes: 
    :param str score: score de la partie
    :param str nommap: nom de la map en cours de jeu
    :return: bool     
    """
    MS = 0
    if (
        var["pos_x"] == var["pos_sortie_x"]
        and var["pos_y"] == var["pos_sortie_y"]
        and nbdiamand >= diamand
    ):
        suivant = 0
        upemtk.efface_tout()
        while suivant == 0:
            suivant, score = esthetique.menu_score(
                nbdiamand, tempsrestant, suivant, score
            )
        upemtk.efface_tout()
        esthetique.fond("cyan")
        upemtk.texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 3,
            "Victoire !",
            couleur="black",
            ancrage="center",
            taille=75,
        )
        esthetique.personnage_victorieux()
        esthetique.coffre()
        esthetique.affiche_score_victoire(score)
        if MS == 0:
            test_meilleurscore(nommap, score)
            MS = 1
        if cartes == 6:
            del var["carte"]
        return True
    return False


def initialiser_partie(carte):
    """
    Initialise les parametres par defaut de la partie

    :param list carte: liste 2D contenant le jeu

    >>> carte = [
    ...     ["W", "W", "W", "W", "W", "W", "W"], 
    ...     ["W", ".", "P", "R", "P", ".", "W"], 
    ...     ["W", ".", "P", "E", "P", ".", "W"],
    ...     ["W", "W", "W", "W", "W", "W", "W"]]
    >>> initialiser_partie(carte)
    >>> (var["pos_x"], var["pos_y"]) == (3, 1)
    True
    >>> (var["pos_sortie_x"], var["pos_sortie_y"]) == (3, 2)
    True
    """
    for y in range(len(carte)):
        for x in range(len(carte[y])):
            if carte[y][x] == "R":  # on recupere la position du perso
                var["pos_x"] = x
                var["pos_y"] = y
            elif carte[y][x] == "E":  # on recupere la position de l'arrivée
                var["pos_sortie_x"] = x
                var["pos_sortie_y"] = y
    var["porte"] = 1
    var["taille_case"] = var["dimension_fenetre"] // var["nb_cases"]


def debug(carte, nbdiamand, debug, tempstotal, score, tempslumiere):
    """
    Perso joue aléatoirement
    
    :param list carte: liste 2D contenant le jeu
    :param int nb_diamand: nombre de diamant deja recupere en jeu
    :param int debut: test si le mode debut est activé (1, -1)
    :param int tempstotal: temps restant de la partie
    :param str score: score de la partie
    ;param int tempslumiere: temps de lumiere restant
    :return: nbdiamand, debut, tempstotal, score, tempslumiere
    """
    choix = ["Up", "Down", "Left", "Right"]
    while True:
        x = choice(choix)
        if test_deplacement(carte, x, "D"):
            deplace(carte, x)
            return (
                nbdiamand + 1,
                debug,
                int(tempstotal) + 10,
                (8 - (len(str(int(score) + 350)))) * "0" + (str(int(score) + 350)),
                tempslumiere,
            )
        if test_deplacement(carte, x, "L"):
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score, tempslumiere + 10
        elif test_deplacement(carte, x, {"G", "."}):
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score, tempslumiere
        elif test_deplacement(carte, x, "E") and var["porte"] == 0:
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score, tempslumiere
        elif (
            x == "Right"
            and carte[var["pos_y"]][var["pos_x"] + 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] + 2] == "."
        ):
            pousser_pierre(carte, x)
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score, tempslumiere
        elif (
            x == "Left"
            and carte[var["pos_y"]][var["pos_x"] - 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] - 2] == "."
        ):
            pousser_pierre(carte, x)
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score, tempslumiere
        choix.remove(x)
        if choix == []:
            debug = -1
            return nbdiamand, debug, tempstotal, score, tempslumiere
    return nbdiamand, debug, tempstotal, score, tempslumiere


def encadrement(
    msg, x, y, couleurTXT, couleurCadre, Taille, Epaisseur, Espacement, polise
):
    """ 
    Ecrit et encadre un texte puis donne les coordonnées du cadre (pour clic)
    
    :param str msg: message a encadrer
    :param int x: coordonnee x du msg a positionner
    :param int y: coordonnee y du msg a positionner
    :param str couleurTXT: couleur du msg
    :param str couleurCadre: couleur du cadre
    :param int Taille: taille du msg
    :param int Epaisseur: epaisseur du trait de lencadrement
    :param int Espacement: epaissement entre le msg et l'encadrement
    :return: [x_point_haut_gauche, y_point_haut_gauche, x_point_bas_droit, y_point_bas_droit]
    """
    upemtk.texte(10000000, y, msg, couleur=couleurTXT, police=polise, taille=Taille)
    upemtk.longueur_texte(msg)
    x2 = x + upemtk.longueur_texte(msg) // 2 + Espacement
    y2 = y + upemtk.hauteur_texte() + Espacement
    upemtk.texte(
        x - upemtk.longueur_texte(msg) // 2,
        y,
        msg,
        couleur=couleurTXT,
        police="Impact",
        taille=Taille,
    )
    upemtk.rectangle(
        x - Espacement - upemtk.longueur_texte(msg) // 2,
        y - Espacement,
        x2,
        y2,
        couleur=couleurCadre,
        epaisseur=Epaisseur,
    )
    return [x - upemtk.longueur_texte(msg) // 2 - Espacement, y - Espacement, x2, y2]


dico_texte = {
    "space": " ",
    "minus": "-",
    "plus": "+",
    "underscore": "_",
    "period": ".",
    "quotdbl": "#",
}


def _input(msg, reponse_defaut):
    """
    meme fonction que input mais cette fois si 
    s'affiche à l'écran et non sur la console
    :param str msg: message decrivant linput sur la fenetre
    :param str reponse_defaut: texte a afficher par defaut dans linput 
    :return: saisie de lutilisateur au clavier (str)
    """
    texte = reponse_defaut
    while True:
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)
        if type_ev == "Touche":
            x = upemtk.touche(ev)

            if x == "Return":
                return texte
            elif x == "BackSpace":
                texte = texte[:-1]

            elif len(x) == 1 and len(texte) <= 18:
                texte += x
            elif x in dico_texte:
                texte += dico_texte[x]

        elif type_ev == "ClicGauche":
            return texte

        upemtk.efface("texte_input")
        upemtk.texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 2,
            texte,
            couleur="white",
            ancrage="center",
            tag="texte_input",
        )
        upemtk.mise_a_jour()


def my_input(msg, type_retour, reponse_defaut=""):
    """
    affichage de l'input
    
    :param str msg: message decrivant linput sur la fenetre
    :param str type_retour: ("int", "str")
    :param str reponse_defaut: texte a afficher par defaut dans linput 
    :return: texte saisie par lutilisateur respectant le type voulu
    """
    upemtk.rectangle(
        var["dimension_fenetre"] // 2 - 180,
        var["dimension_fenetre"] // 2 - 100,
        var["dimension_fenetre"] // 2 + 180,
        var["dimension_fenetre"] // 2 + 100,
        couleur="gray28",
        remplissage="gray",
        epaisseur=5,
        tag="cadre",
    )

    while True:
        upemtk.texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 2 - 50,
            msg,
            couleur="white",
            ancrage="center",
            tag="msg",
        )
        _var = _input(msg, reponse_defaut)
        if type_retour == "int":
            if _var.isdigit():
                if int(_var) < 500 and int(_var) > 0:
                    upemtk.efface("msg")
                    upemtk.efface("msg_erreur")
                    upemtk.efface("texte_input")
                    upemtk.efface("cadre")
                    return int(_var)
                elif int(_var) == 0:
                    upemtk.efface("msg_erreur")
                    upemtk.texte(
                        var["dimension_fenetre"] // 2,
                        var["dimension_fenetre"] // 2 + 75,
                        "Valeur trop petite",
                        couleur="red",
                        ancrage="center",
                        police="impact",
                        tag="msg_erreur",
                    )
                else:
                    upemtk.efface("msg_erreur")
                    upemtk.texte(
                        var["dimension_fenetre"] // 2,
                        var["dimension_fenetre"] // 2 + 75,
                        "Valeur trop grande",
                        couleur="red",
                        ancrage="center",
                        police="impact",
                        tag="msg_erreur",
                    )
            else:
                upemtk.efface("msg_erreur")
                upemtk.texte(
                    var["dimension_fenetre"] // 2,
                    var["dimension_fenetre"] // 2 + 75,
                    "Valeur entiere requis",
                    couleur="red",
                    ancrage="center",
                    police="impact",
                    tag="msg_erreur",
                )
        else:
            upemtk.efface("msg")
            upemtk.efface("msg_erreur")
            upemtk.efface("texte_input")
            upemtk.efface("cadre")
            return _var


def creation_map_aleatoire(x=40, y=22):
    """
    renvoie une map aléatoire de taille(40 * 22) (x * y)
    
    :param int x: longueur de la map aleatoire
    :param int y: largeur de la map aleatoire
    """
    carte = [["W" for _ in range(x)] for _ in range(y)]
    nb_diam = 0

    for j in range(1, y - 1):
        for i in range(1, x - 1):
            nb_random = randint(0, 1025)
            if nb_random < 650:
                carte[j][i] = "G"
            elif nb_random < 750:
                carte[j][i] = "."
            elif nb_random < 850:
                carte[j][i] = "P"
            elif nb_random < 900:
                carte[j][i] = "D"
                nb_diam += 1
            elif nb_random <= 925:
                carte[j][i] = "L"

    coord_entree = (randint(1, x - 2), randint(1, y - 2))
    coord_sortie = (randint(1, x - 2), randint(1, y - 2))
    while coord_entree == coord_sortie:
        coord_sortie = (randint(1, x - 2), randint(1, y - 2))

    carte[coord_entree[1]][coord_entree[0]] = "R"
    carte[coord_sortie[1]][coord_sortie[0]] = "E"
    save_map_en_cours(
        carte,
        nb_diam - randint(3, 8),
        "00000000",
        100,
        "map_aleatoire.txt",
        0,
        "map_aleatoire",
        True,
    )


def menu_or_retry(a, coordretry, coordmenu):
    """
    Regarde si l'utilisateur à décidé de quitté ou de recommencer
    et retourne donc sa réponse

    :param tuple a: coordonnee du clic de la souris
    :param list coordretry: coordonnees des points du bouton retry
    :param list coordmenu: coordonees des points du bouton menu
    :return: bool

    >>> menu_or_retry((10, 10), [0, 0, 20, 20], [100, 100, 200, 200])
    9
    >>> menu_or_retry((110, 110), [0, 0, 20, 20], [100, 100, 200, 200])
    7
    >>> menu_or_retry((50, 50), [0, 0, 20, 20], [100, 100, 200, 200])
    0
    """
    if (
        a[0] < coordretry[2]
        and a[0] > coordretry[0]
        and a[1] < coordretry[3]
        and a[1] > coordretry[1]
    ):
        return 9
    if (
        a[0] < coordmenu[2]
        and a[0] > coordmenu[0]
        and a[1] < coordmenu[3]
        and a[1] > coordmenu[1]
    ):
        return 7
    return 0


def test_clic(coordsclic, coordscarre):
    """
    test si l'utilisateur a cliqué dans le carré

    :param tuple coordsclic: coordonnee du clic de la souris
    :param list coordscarre: coordonnees des points du carre
    :return: bool 

    >>> test_clic((10, 10), [0, 0, 20, 20])
    True
    >>> test_clic((100, 100), [0, 0, 20, 20])
    False
    """
    if (
        coordsclic[0] < coordscarre[2]
        and coordsclic[0] > coordscarre[0]
        and coordsclic[1] < coordscarre[3]
        and coordsclic[1] > coordscarre[1]
    ):
        return True
    return False


def test_suivant_menu(coords, suivant):
    """
    test si l'utilisateur a cliqué sur la flèche qui
    donne la map suivante dans le menu

    :param tuple coords: coordonnee du clic de la souris
    :param list suivant: coordonnees des points de la fleche suivant
    :return: bool 
    
    >>> test_suivant_menu((575, 400), [(550, 250), (550, 300), (600, 275)])
    0
    >>> test_suivant_menu((575, 275), [(550, 250), (550, 300), (600, 275)])
    1
    """
    if (
        suivant[0][0] <= coords[0] <= suivant[2][0]
        and suivant[0][1] + (coords[0] - suivant[0][0]) * 0.5
        <= coords[1]
        <= suivant[1][1] - (coords[0] - suivant[0][0]) * 0.5
    ):
        return 1
    return 0


def test_precedent(coords, precedent):
    """
    test si l'utilisateur a cliqué sur la flèche 
    qui donne la map précédente dans le menu

    :param tuple coords: coordonnee du clic de la souris
    :param list precedent: coordonnees des points de la fleche precedent
    :return: bool 

    >>> test_precedent((25, 500), [(50, 250), (50, 300), (0, 275)])
    0
    >>> test_precedent((25, 275), [(50, 250), (50, 300), (0, 275)])
    1
    """
    if (
        precedent[0][0] >= coords[0] >= precedent[2][0]
        and precedent[0][1] + (precedent[0][0] - coords[0]) * 0.5
        <= coords[1]
        <= precedent[1][1] - (precedent[0][0] - coords[0]) * 0.5
    ):
        return 1
    return 0


def affichageV2(carte, nbdiamand, diamand, taille, x_, y_, nbrcase):
    """
    Affiche la carte dans le menu des map
    
    :param list carte: liste 2D contenant le jeu
    :param int nb_diamand: 
    :param int diamand: 
    :param int taille: taille des cases
    :param int x_: position de l'apercu de la map
    :param int y_ position de l'apercu de la map
    :param int nbrcase: nombre de case a afficher sur l'apercu
    """
    esthetique.fond("black")
    for y in range(len(carte) - 1, -1, -1):  # y = ligne
        for x in range(len(carte[y]) - 1, -1, -1):  # x = colonne
            dico[carte[y][x]](
                (x + (var["nb_cases"] // 2 - var["pos_x"])) + x_,
                (y + (var["nb_cases"] // 2 - var["pos_y"])) + y_,
                taille,
                nbdiamand,
                diamand,
                "goldenrod3",
            )  # centre le perso
    upemtk.rectangle(
        x_ * taille + nbrcase * taille + 2 * taille,
        y_ * taille,
        var["dimension_fenetre"],
        var["dimension_fenetre"] + 100,
        remplissage="black",
    )
    upemtk.rectangle(
        x_ * taille,
        y_ * taille + nbrcase * taille + 2 * taille,
        var["dimension_fenetre"],
        var["dimension_fenetre"] + 100,
        remplissage="black",
    )
    upemtk.rectangle(
        x_ * taille + 2 * taille,
        y_ * taille + 3 * taille,
        x_ * taille + nbrcase * taille + 2 * taille + 5,
        y_ * taille + nbrcase * taille + 2 * taille + 5,
        couleur="gold",
        epaisseur=10,
    )


def menu_echap(temps, tempslumiere):
    """
    affiche un menu si jamais l'utilisateur à appuyer sur echap et 
    renvoie un des différents choix disponible
        (retry, continue, sauvegarder, quitter le jeu)
    
    :param int temps: temps du jeu en debut de menu afin de le conserver
    :param int tempslumiere: temps de lumiere restant
    :return: code de retour, duree de la partie, temps de lumiere
    """
    d = time()
    while True:
        esthetique.fond("black")
        encadrement(
            "MENU",
            var["dimension_fenetre"] // 2,
            30,
            "White",
            "black",
            50,
            1,
            1,
            "Impact",
        )

        continuer = encadrement(
            "CONTINUER",
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 5,
            "White",
            "white",
            36,
            1,
            5,
            "Impact",
        )
        sauvegarder = encadrement(
            "SAUVEGARDER",
            var["dimension_fenetre"] // 2,
            2 * var["dimension_fenetre"] // 5,
            "White",
            "white",
            36,
            1,
            5,
            "Impact",
        )
        recommencer = encadrement(
            "RECOMMENCER",
            var["dimension_fenetre"] // 2,
            3 * var["dimension_fenetre"] // 5,
            "White",
            "white",
            36,
            1,
            5,
            "Impact",
        )
        quitter = encadrement(
            "RETOURNER AU MENU",
            var["dimension_fenetre"] // 2,
            4 * var["dimension_fenetre"] // 5,
            "White",
            "white",
            36,
            1,
            5,
            "Impact",
        )

        upemtk.mise_a_jour()
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)
        if type_ev == "Quitte":
            return -1, temps + time() - d, tempslumiere + time() - d

        if type_ev == "Touche":
            t = upemtk.touche(ev)
            if t == "Escape":
                return 5, temps + time() - d, tempslumiere + time() - d
        if type_ev == "ClicGauche":
            coords = [upemtk.clic_x(ev), upemtk.clic_y(ev)]
            if test_clic(coords, continuer):
                return 5, temps + time() - d, tempslumiere + time() - d
            if test_clic(coords, sauvegarder):
                return 6, temps + time() - d, tempslumiere + time() - d
            if test_clic(coords, recommencer):
                return 9, temps + time() - d, tempslumiere + time() - d
            if test_clic(coords, quitter):
                return 7, temps + time() - d, tempslumiere + time() - d


def test_meilleurscore(nommap, score):
    """
    test si le score de fin est l'un de ses meilleurs scores
    
    :param str nommap: nom de la map afin de changer son score
    :param str score: score de la partie
    """
    pseudo = ""
    with open("map/" + nommap, "r") as f1:
        contenu = f1.read()
    contenu = contenu.split("\n")
    while contenu[-1] == "":
        contenu.pop()
    ted = contenu.pop(0)
    lumiere = contenu.pop()
    nommap = contenu.pop()
    inutile = contenu.pop()  # score de début de partie("00000000")
    score3 = contenu.pop() + "\n"
    score2 = contenu.pop() + "\n"
    score1 = contenu.pop() + "\n"
    score4 = str(int(score)) + "\n"
    score4 = "0" * (8 - len(score4[:-1])) + score4

    if int(score3[-10:-1]) < int(score4):
        while pseudo == "":
            pseudo = my_input("Quel est votre pseudo", "str", reponse_defaut="pseudo")
        score3 = pseudo + "  =  " + score4
        if int(score2[-10:-1]) < int(score3[-10:-1]):
            score2, score3 = score3, score2
            if int(score1[-10:-1]) < int(score2[-10:-1]):
                score1, score2 = score2, score1

    with open("map/" + nommap, "w") as f1:
        f1.write(ted)
        f1.write("\n")
        f1.write("\n".join(contenu))
        f1.write("\n")
        f1.write(score1)
        f1.write(score2)
        f1.write(score3)
        f1.write("00000000\n")
        f1.write(nommap+"\n")
        f1.write("0")


def test_ouverture_custom_map():
    """
    test si louverture de la map custom est valide
    return le nom si oui sinon return None
    """
    nom = my_input("Custom map:", "str")
    if not os.path.isfile("map/{}.txt".format(nom)):
        my_input("La map n'existe pas", "str")
        return
    return nom + ".txt"


if __name__ == "__main__":
    print("Programme principal: main.py")
