from upemtk import *
from variable import var


def creer_map(nomdufichier):
    with open("map/" + nomdufichier, "r") as fichier:
        contenu = fichier.read()
        contenu = contenu.split("\n")
        contenu.pop(0)
        for i in range(len(contenu)):
            contenu[i] = list(contenu[i])
    return contenu


def terre(x, y):
    """Dessine la terre aux coordonnées x, y"""
    rectangle(
        x * var["taille_case"],
        y * var["taille_case"],
        x * var["taille_case"] + var["taille_case"] - 1,
        y * var["taille_case"] + var["taille_case"] - 1,
        couleur="pink",
        remplissage="pink",
    )


def pierre(x, y):
    """Dessine une pierre aux coordonnées x, y"""
    cercle(
        x * var["taille_case"] + var["taille_case"] / 2,
        y * var["taille_case"] + var["taille_case"] / 2,
        (var["taille_case"] / 2) - 1,
        couleur="grey",
        remplissage="grey",
    )


def rockford(x, y):
    """Dessine rockford aux coordonnées x, y"""
    cercle(
        x * var["taille_case"] + var["taille_case"] / 2,
        y * var["taille_case"] + var["taille_case"] / 2,
        (var["taille_case"] / 2) - 1,
        couleur="green",
        remplissage="green",
    )
    cercle(
        x * var["taille_case"] + var["taille_case"] / 2,
        y * var["taille_case"] + 2 * var["taille_case"] / 3 - var["taille_case"] / 15,
        var["taille_case"] / 4,
        couleur="black",
        remplissage="black",
    )
    rectangle(
        x * var["taille_case"] + (var["taille_case"] / 2) - var["taille_case"] / 4,
        y * var["taille_case"]
        + (2 * var["taille_case"] / 3)
        - var["taille_case"] / 4
        - var["taille_case"] / 15,
        x * var["taille_case"] + (var["taille_case"] / 2) + var["taille_case"] / 4,
        y * var["taille_case"] + (2 * var["taille_case"] / 3) - var["taille_case"] / 15,
        couleur="green",
        remplissage="green",
    )
    cercle(
        x * var["taille_case"] + var["taille_case"] / 3,
        y * var["taille_case"] + var["taille_case"] / 3,
        var["taille_case"] / 13,
        couleur="black",
        remplissage="black",
    )
    cercle(
        x * var["taille_case"] + 2 * var["taille_case"] / 3,
        y * var["taille_case"] + var["taille_case"] / 3,
        var["taille_case"] / 13,
        couleur="black",
        remplissage="black",
    )


def mur(x, y):
    """Dessine un mur aux coordonnées x, y"""
    rectangle(
        x * var["taille_case"],
        y * var["taille_case"],
        var["taille_case"] + x * var["taille_case"] - 1,
        var["taille_case"] + y * var["taille_case"] - 1,
        couleur="black",
        remplissage="black",
    )


def diamand(x, y):
    """Dessine un diamand aux coordonnées x, y"""
    rectangle(
        x * var["taille_case"],
        y * var["taille_case"],
        var["taille_case"] + x * var["taille_case"] - 1,
        var["taille_case"] + y * var["taille_case"] - 1,
        couleur="blue",
        remplissage="blue",
    )


def sortie(x, y):
    """Dessine la sortie aux coordonnées x, y"""
    rectangle(
        x * var["taille_case"],
        y * var["taille_case"],
        var["taille_case"] + x * var["taille_case"] - 1,
        var["taille_case"] + y * var["taille_case"] - 1,
        couleur="green",
        remplissage="green",
    )


def rien(x, y):
    pass


# on associe les lettres aux fonctions les dessinant
dico = {
    "G": terre,  # carre marron
    "P": pierre,  # rond gris
    "R": rockford,  # rond blanc
    "W": mur,  # carre noir
    "D": diamand,  # carre bleu
    "E": sortie,  # carre vert
    ".": rien,
}


def affichage(carte):
    """Affiche la carte"""
    rectangle(
        0,
        0,
        var["dimension_fenetre"],
        var["dimension_fenetre"],
        couleur="purple",
        remplissage="purple",
    )
    for y in range(len(carte)):  # y = ligne
        for x in range(len(carte[y])):  # x = colonne
            dico[carte[y][x]](x, y)


def tomber_de_pierre(carte):
    """Fais tomber les pierres"""
    pass


def deplacer_perso(carte, deplacement):
    """Test si le perso peut se deplacer, si oui, deplace le perso sur la carte en fonction de la touche utilisé"""
    pass


def pousser_pierre(carte, deplacement):
    """Test si une pierre est poussable, si oui, la pousse"""
    pass


def win(carte):
    """Regarde si l'utilisateur gagne
	>>> win([['l', 'k', 'E']])
	False
	>>> win([['l', 'k', 'o']])
	True
	"""
    for element in carte:
        if "E" not in element:
            return True
    return False


def initialiser_partie(carte):
    """Initialise les parametres par defaut de la partie"""
    pass


def debug(carte):
    """Perso joue aléatoirement"""
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
