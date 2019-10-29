from upemtk import *
from variable import var


def terre(x, y):
    """Dessine la terre aux coordonnées x, y"""
    rectangle(
        x * var["taille_case"],
        y * var["taille_case"],
        x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] + var["taille_case"],
        "brown",
        "brown",
    )


def pierre(x, y):
    """Dessine une pierre aux coordonnées x, y"""
    cercle(
        x * var["taille_case"] + var["taille_case"] / 2,
        y * var["taille_case"] + var["taille_case"] / 2,
        var["taille_case"] / 2,
        "grey",
        "grey",
    )


def rockford(x, y):
    """Dessine rockford aux coordonnées x, y"""
    cercle(
        x * var["taille_case"] + var["taille_case"] / 2,
        y * var["taille_case"] + var["taille_case"] / 2,
        var["taille_case"] / 2,
        "white",
        "white",
    )
    cercle(
        x * var["taille_case"] + var["taille_case"] / 3,
        y * var["taille_case"] + var["taille_case"] / 3,
        2,
        "black",
        "black",
    )
    cercle(
        x * var["taille_case"] + 2 * var["taille_case"] / 3,
        y * var["taille_case"] + var["taille_case"] / 3,
        2,
        "black",
        "black",
    )
    rectangle(
        x * var["taille_case"] + var["taille_case"] / 3,
        y * var["taille_case"] + 2 * var["taille_case"] / 3,
        x * var["taille_case"] + 2 * var["taille_case"] / 3,
        y * var["taille_case"] + 2 * var["taille_case"] / 3 + 2,
        "black",
        "black",
    )


def mur(x, y):
    """Dessine un mur aux coordonnées x, y"""
    pass


def diamand(x, y):
    """Dessine un diamand aux coordonnées x, y"""
    pass


def sortie(x, y):
    """Dessine la sortie aux coordonnées x, y"""
    pass


# on associe les lettres aux fonctions les dessinant
dico = {
    "G": terre,  # carre marron
    "P": pierre,  # rond gris
    "R": rockford,  # rond blanc
    "W": mur,  # carre noir
    "D": diamand,  # carre bleu
    "E": sortie,  # carre vert
}


def affichage(carte):
    """Affiche la carte"""
    for y in range(len(carte)):  # y = ligne
        for x in range(len(carte)):  # x = colonne
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
