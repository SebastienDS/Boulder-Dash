from upemtk import *
from variable import var, _touche
from random import choice
from time import time
import esthetique


def creer_map(nomdufichier):
    """Transforme un fichier texte contenant une map en une matriche"""
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
        for i in range(len(contenu)):
            contenu[i] = list(
                contenu[i]
            )  # transforme la chaine de caractère en une list('abc'=['a','b','c'])
    return contenu, t, d


def rien(x, y, *args):
    """Ne fait rien(cas = ".")"""
    pass


# on associe les lettres aux fonctions les dessinant
dico = {
    "G": esthetique.terre,
    "P": esthetique.pierre,
    "R": esthetique.rockford,
    "W": esthetique.mur,
    "D": esthetique.diamand,
    "E": esthetique.sortie,
    ".": rien,
    "P1": esthetique.pierre_eboulement,
    "D1": esthetique.diamand_eboulement,
    "F": esthetique.mur,
}


def timer(tempstotal, tempscommencement):
    return int(tempstotal) - (int(time() - tempscommencement))


def affichage(carte, nbdiamand, diamand):
    """Affiche la carte"""
    esthetique.fond("black")
    if var["porte"] == 0:
        esthetique.lumiere_escalier()
    esthetique.lumiere()
    carte[2][0] = "F"
    for y in range(len(carte) - 1, -1, -1):  # y = ligne
        for x in range(len(carte[y]) - 1, -1, -1):  # x = colonne
            dico[carte[y][x]](
                x + (var["nb_cases"] // 2 - var["pos_x"]),
                y + (var["nb_cases"] // 2 - var["pos_y"]),
                var["taille_case"],
                nbdiamand,
                diamand,
            )  # centre le perso


def fond_score_temps_diams(score, tempsrestant, nbdiamand, diamand):
    """Affiche une banderolle avec le score et le bouton exitgame et retry"""
    nbdiamandrestant = diamand - nbdiamand
    if nbdiamandrestant < 0:
        nbdiamandrestant = 0
    esthetique.fond_score_temps_diams(score, tempsrestant, nbdiamandrestant)


def tomber_de_pierre_ou_diamand(carte):
    """Fais tomber les pierres"""
    for y in range(len(carte) - 2, -1, -1):
        for x in range(len(carte[0]) - 1, -1, -1):
            if carte[y][x] == "P1" and carte[y + 1][x] == ".":
                carte[y][x], carte[y + 1][x] = ".", "P1"
            if carte[y][x] == "D1" and carte[y + 1][x] == ".":
                carte[y][x], carte[y + 1][x] = ".", "D1"


def test_si_pierre_va_tomber(carte):
    for y in range(len(carte) - 2, -1, -1):
        for x in range(len(carte[0]) -1, -1, -1):
            if carte[y][x] in {"P", "D"} and carte[y + 1][x] == ".":
                carte[y][x] = carte[y][x] + "1"


def test_pierre_ou_diamand_eboulement(carte):
    for y in range(len(carte) - 1):
        for x in range(len(carte[0])):
            if carte[y][x] == "P1" and carte[y + 1][x] not in [".", "R"]:
                carte[y][x] = "P"
            if carte[y][x] == "D1" and carte[y + 1][x] not in [".", "R"]:
                carte[y][x] = "D"


def test_deplacement(carte, direction, liste):
    """test si le deplacement est possible"""
    return (
        carte[var["pos_y"] + _touche[direction][1]][
            var["pos_x"] + _touche[direction][0]
        ]
        in liste
    )


def enleve_porte(carte, ev, nbdiamand, diamand):
    type_ev = type_evenement(ev)
    if type_ev == "Touche":
        t = touche(ev)
        if t in _touche:
            if (
                carte[var["pos_y"] + _touche[t][1]][var["pos_x"] + _touche[t][0]]
                == carte[var["pos_sortie_y"]][var["pos_sortie_x"]]
                and nbdiamand >= diamand
            ):
                var["porte"] = 0


def deplace(carte, t):
    """se deplace dans la direction voulu et met a jour les positions du joueur"""
    carte[var["pos_y"] + _touche[t][1]][var["pos_x"] + _touche[t][0]] = "R"
    carte[var["pos_y"]][var["pos_x"]] = "."
    var["pos_x"] += _touche[t][0]
    var["pos_y"] += _touche[t][1]


def deplacer_perso(carte, nbdiamand, ev, diamand):
    """Test si le perso peut se deplacer, si oui, deplace le perso sur la carte en fonction de la touche utilisé"""
    type_ev = type_evenement(ev)
    if type_ev == "Touche":
        t = touche(ev)
        if t in _touche:
            if test_deplacement(carte, t, "D"):
                deplace(carte, t)
                return nbdiamand + 1
            elif test_deplacement(carte, t, {"G", ".", "F"}):
                deplace(carte, t)
                return nbdiamand
            if (
                nbdiamand >= diamand
                and test_deplacement(carte, t, "E")
                and var["porte"] == 0
            ):
                deplace(carte, t)
                return nbdiamand
    return nbdiamand

# def tomber_pierre_laterale(carte):
#     for y in range (len(carte) - 1, -1, -1):
#         for x in range(len(carte[0]) - 1, -1, -1):
#             if ...:
#                 ...
#     return carte

def test_pousser_pierre(carte, ev):
    type_ev = type_evenement(ev)
    if type_ev == "Touche":
        t = touche(ev)
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
    """Test si une pierre est poussable, si oui, la pousse"""
    (
        carte[var["pos_y"]][var["pos_x"] + _touche[t][0]],
        carte[var["pos_y"]][var["pos_x"] + 2 * _touche[t][0]],
    ) = (".", "P")


def loose(carte, tempsrestant):
    """test si joueur s'est pris une pierre
    si oui met l'image de défaite et retourne True
    """
    if carte[var["pos_y"] - 1][var["pos_x"]] in ["P1", "D1"] or tempsrestant <= 0:
        efface_tout()
        esthetique.fond("black")
        esthetique.personnage_defaitiste()
        texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 4,
            "DÉFAITE !",
            couleur="red",
            ancrage="center",
            taille=75,
        )
        return True
    return False


def win(nbdiamand, diamand):
    """Regarde si l'utilisateur gagne
    si oui, met l'image de victoire et retourne True"""
    if (
        var["pos_x"] == var["pos_sortie_x"]
        and var["pos_y"] == var["pos_sortie_y"]
        and nbdiamand >= diamand
    ):
        efface_tout()
        esthetique.fond("cyan")
        texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 3,
            "Victoire !",
            couleur="black",
            ancrage="center",
            taille=75,
        )
        esthetique.personnage_victorieux()
        esthetique.coffre()
        return True
    return False


def initialiser_partie(carte):
    """Initialise les parametres par defaut de la partie"""
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


def debug(carte, nbdiamand, debug):
    """Perso joue aléatoirement"""
    choix = ["Up", "Down", "Left", "Right"]
    while True:
        x = choice(choix)
        if test_deplacement(carte, x, "D"):
            deplace(carte, x)
            return nbdiamand + 1, debug
        elif test_deplacement(carte, x, {"G", "."}):
            deplace(carte, x)
            return nbdiamand, debug
        elif test_deplacement(carte, x, "E") and var["porte"] == 0:
            deplace(carte, x)
            return nbdiamand, debug
        elif (
            x == "Right"
            and carte[var["pos_y"]][var["pos_x"] + 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] + 2] == "."
        ):
            pousser_pierre(carte, x)
            deplace(carte, x)
            return nbdiamand, debug
        elif (
            x == "Left"
            and carte[var["pos_y"]][var["pos_x"] - 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] - 2] == "."
        ):
            pousser_pierre(carte, x)
            deplace(carte, x)
            return nbdiamand, debug
        choix.remove(x)
        if choix == []:
            debug = -1
            return nbdiamand, debug
    return nbdiamand, debug


def encadrement(
    msg, x, y, couleurTXT, couleurCadre, Taille, Epaisseur, Espacement
):  # Ecrit et encadre un texte puis donne les coordonnées du cadre (pour clic)
    texte(10000000, y, msg, couleur=couleurTXT, police="Impact", taille=Taille)
    x2 = x + longueur_texte(msg) + Espacement
    y2 = y + hauteur_texte() + Espacement
    texte(x, y, msg, couleur=couleurTXT, police="Impact", taille=Taille)
    rectangle(
        x - Espacement,
        y - Espacement,
        x2,
        y2,
        couleur=couleurCadre,
        epaisseur=Epaisseur,
    )
    return [x - Espacement, y - Espacement, x2, y2]


def quitte_or_retry(a, coordretry, coordquitte):
    """Regarde si l'utilisateur à décidé de quitté ou de recommencer
    et retourne donc sa réponse"""
    if (
        a[0] < coordretry[2]
        and a[0] > coordretry[0]
        and a[1] < coordretry[3]
        and a[1] > coordretry[1]
    ):
        return 2
    if (
        a[0] < coordquitte[2]
        and a[0] > coordquitte[0]
        and a[1] < coordquitte[3]
        and a[1] > coordquitte[1]
    ):
        return 1
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
