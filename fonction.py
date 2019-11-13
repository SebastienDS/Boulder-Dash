from upemtk import *
from variable import var, _touche
from random import choice
import esthetique


def creer_map(nomdufichier):
    """Transforme un fichier texte contenant une map en une matriche"""
    with open(
        "map/" + nomdufichier, "r"
    ) as fichier:  # ouvre le fichier contenant la carte
        contenu = fichier.read()  # lis le fichier
        contenu = contenu.split(
            "\n"
        )                                # Construit une matriche de la carte /chaque ligne = chaine de caractère
        ted = contenu.pop(0)             # Enlève le temps et nombre de diamands
        ted = ted.split()
        t = ted[0][:-1]
        d = ted[1][:-1]
        for i in range(len(contenu)):
            contenu[i] = list(
                contenu[i]
            )  # transforme la chaine de caractère en une list('abc'=['a','b','c'])
    return contenu, t, d


def terre(x, y):
    """Dessine la terre aux coordonnées x, y"""
    esthetique.terre(x, y)

def pierre(x, y):
    """Dessine une pierre aux coordonnées x, y"""
    esthetique.pierre(x, y)

def rockford(x, y):
    """Dessine rockford aux coordonnées x, y"""
    # main à gauche
    esthetique.rockford(x, y)

def mur(x, y):
    """Dessine un mur aux coordonnées x, y"""
    esthetique.mur(x, y)

def diamand(x, y):
    """Dessine un diamand aux coordonnées x, y"""
    esthetique.diamand(x, y)

def sortie(x, y):
    """Dessine la sortie aux coordonnées x, y"""
    esthetique.sortie(x, y)

def rien(x, y):
    """Ne fait rien(cas = ".")"""
    pass

def pierre_eboulement(x, y):
    """Affiche pierre qui tombe"""
    esthetique.pierre_eboulement(x, y)
    
def diamand_eboulement(x, y):
    esthetique.diamand_eboulement(x, y)
    
# on associe les lettres aux fonctions les dessinant
dico = {
    "G": terre,  # carre marron
    "P": pierre,  # rond gris
    "R": rockford,  # rond blanc
    "W": mur,  # carre noir
    "D": diamand,  # carre bleu
    "E": sortie,  # carre vert
    ".": rien,
    "P1": pierre_eboulement,
    "D1": diamand_eboulement,
    "F": mur
}


def affichage(carte):
    """Affiche la carte"""
    fond()
    carte[2][0] = "F"
    for y in range(len(carte)):  # y = ligne
        for x in range(len(carte[y])):  # x = colonne
            dico[carte[y][x]](
                x + (var["nb_cases"] // 2 - var["pos_x"]),
                y + (var["nb_cases"] // 2 - var["pos_y"]),
            )  # centre le perso


def fond():
    """Affiche le fond"""
    esthetique.fond()

def fond_victorieux():
    """Affiche le fond en cas de victoire"""
    esthetique.fond_victorieux()

def fond_score(score):
    """Affiche une banderolle avec le score et le bouton exitgame et retry"""
    esthetique.fond_score(score)

def personnage_victorieux():
    """Affiche ce personnage en cas de victoire"""
    esthetique.personnage_victorieux()

def personnage_defaitiste():
    """Affiche ce personnage en cas de défaite"""
    esthetique.personnage_defaitiste()

def coffre():
    """Affiche un coffre"""
    esthetique.coffre()


def tomber_de_pierre_ou_diamand(carte):
    """Fais tomber les pierres"""
    for y in range(len(carte) - 2, -1, -1 ):
        for x in range(len(carte[0]) - 1, -1, -1):
            if carte[y][x] in ["P", "P1"] and carte[y + 1][x] == ".":
                carte[y][x], carte[y + 1][x] = ".", "P1"
            if carte[y][x] in ["D", "D1"] and carte[y + 1][x] == ".":
                carte[y][x], carte[y + 1][x] = ".", "D1"

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
            elif test_deplacement(carte, t, {"G", ".","F"}):
                deplace(carte, t)
                return nbdiamand
            if nbdiamand >= diamand and test_deplacement(carte,t, "E"):
                deplace(carte, t)
                return nbdiamand
                
    return nbdiamand


def pousser_pierre(carte, ev):
    """Test si une pierre est poussable, si oui, la pousse"""
    type_ev = type_evenement(ev)
    if type_ev == "Touche":
        t = touche(ev)
        if (
            t == "Right"
            and carte[var["pos_y"]][var["pos_x"] + 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] + 2] == "."
        ):
            (
                carte[var["pos_y"]][var["pos_x"] + 1],
                carte[var["pos_y"]][var["pos_x"] + 2],
            ) = (".", "P")
        if (
            t == "Left"
            and carte[var["pos_y"]][var["pos_x"] - 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] - 2] == "."
        ):
            (
                carte[var["pos_y"]][var["pos_x"] - 1],
                carte[var["pos_y"]][var["pos_x"] - 2],
            ) = (".", "P")


def loose(carte):
    """test si joueur s'est pris une pierre
    si oui met l'image de défaite et retourne True
    """
    if carte[var["pos_y"] - 1][var["pos_x"]] in ["P1", "D1"]:
        efface_tout()
        fond()
        personnage_defaitiste()
        texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 4,
            "DÉFAITE !",
            couleur="red",
            ancrage="center",
            taille=75,
        )
     #if time
        return True
    return False


def win(nbdiamand, diamand):
    """Regarde si l'utilisateur gagne
    si oui, met l'image de victoire et retourne True"""
    if var["pos_x"] == var["pos_sortie_x"] and var["pos_y"] == var["pos_sortie_y"] and nbdiamand >= diamand:
        efface_tout()
        fond_victorieux()
        texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 3,
            "Victoire !",
            couleur="black",
            ancrage="center",
            taille=75,
        )
        personnage_victorieux()
        coffre()
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


def debug(carte, nbdiamand):
    """Perso joue aléatoirement"""
    while True:
        x = choice(["Up", "Down", "Left", "Right"])

        if test_deplacement(carte, x, "D"):
            deplace(carte, x)
            return nbdiamand + 1
        elif test_deplacement(carte, x, {"G", ".", "E"}):
            deplace(carte, x)
            return nbdiamand
    return nbdiamand


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
