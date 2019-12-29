from upemtk import *
from variable import *
from time import time
import fonction


def charbon(x, y, taille_case, *args):
    rectangle(
        x * taille_case,
        y * taille_case,
        x * taille_case + taille_case - 1,
        y * taille_case + taille_case - 1,
        couleur="black",
        remplissage="gray60",
    )
    polygone(
        [
            (x * taille_case + taille_case // 4, y * taille_case + taille_case // 3),
            (x * taille_case + taille_case // 2, y * taille_case + taille_case // 6),
            (
                x * taille_case + 3 * taille_case // 5,
                y * taille_case + taille_case // 4,
            ),
            (
                x * taille_case + 4 * taille_case // 5,
                y * taille_case + 3 * taille_case // 5,
            ),
            (
                x * taille_case + taille_case // 3,
                y * taille_case + 4 * taille_case // 5,
            ),
            (
                x * taille_case + taille_case // 4,
                y * taille_case + 7 * taille_case // 10,
            ),
        ],
        couleur="black",
        remplissage="black",
    )


def terre(x, y, taille_case, *args):
    """Dessine la terre aux coordonnées x, y"""
    rectangle(
        x * taille_case,
        y * taille_case,
        x * taille_case + taille_case - 1,
        y * taille_case + taille_case - 1,
        couleur="sienna4",
        remplissage="sienna4",
    )


def pierre(x, y, taille_case, *args):
    """Dessine une pierre aux coordonnées x, y"""
    cercle(
        x * taille_case + taille_case / 2,
        y * taille_case + taille_case / 2,
        (taille_case / 2) - 1,
        couleur="gray39",
        remplissage="gray39",
    )


def rockford(x, y, taille_case, nbdiamand, diamand, fond_):
    """Dessine rockford aux coordonnées x, y"""
    # main à gauche
    cercle(
        x * taille_case + taille_case // 2 - taille_case // 4,
        y * taille_case + 3 * taille_case // 4 - taille_case // 8,
        taille_case // 12,
        couleur="black",
        remplissage="lightpink",
    )
    # main à droite
    cercle(
        x * taille_case + taille_case // 2 + taille_case // 4,
        y * taille_case + 3 * taille_case // 4 - taille_case // 8,
        taille_case // 12,
        couleur="black",
        remplissage="lightpink",
    )
    # pied à gauche
    cercle(
        x * taille_case + taille_case // 3,
        y * taille_case + 8 * taille_case // 9,
        taille_case // 12,
        couleur="black",
        remplissage="red",
    )
    # pied à droite
    cercle(
        x * taille_case + 2 * taille_case // 3,
        y * taille_case + 8 * taille_case // 9,
        taille_case // 12,
        couleur="black",
        remplissage="red",
    )
    # Tête
    cercle(
        x * taille_case + taille_case // 2,
        y * taille_case + 2 * taille_case // 3,
        taille_case // 4,
        couleur="black",
        remplissage="lightpink",
    )
    # Bouche(cercle + rectangle)
    cercle(
        x * taille_case + taille_case // 2,
        y * taille_case + 2 * taille_case // 3 + taille_case // 12,
        taille_case // 8,
        couleur="black",
        remplissage="black",
    )
    rectangle(
        x * taille_case + taille_case // 2 - taille_case // 8,
        y * taille_case + 2 * taille_case // 3 - taille_case // 12,
        x * taille_case + taille_case // 2 + taille_case // 8,
        y * taille_case + 2 * taille_case // 3 + taille_case // 12,
        couleur="lightpink",
        remplissage="lightpink",
    )
    # Oeil à droite
    cercle(
        x * taille_case + taille_case // 3 + taille_case // 20,
        y * taille_case + 2 * taille_case // 3 - taille_case // 20,
        taille_case // 20,
        couleur="black",
        remplissage="black",
    )
    # Oeil à gauche
    cercle(
        x * taille_case + 2 * taille_case // 3 - taille_case // 20,
        y * taille_case + 2 * taille_case // 3 - taille_case // 20,
        taille_case // 20,
        couleur="black",
        remplissage="black",
    )
    # Torche
    rectangle(
        x * taille_case + 1 * taille_case // 4 - taille_case // 12,
        y * taille_case + 1 * taille_case // 3,
        x * taille_case + 1 * taille_case // 5 + taille_case // 30,
        y * taille_case + 3 * taille_case // 4 - taille_case // 8,
        couleur="black",
        remplissage="sienna4",
    )
    cercle(
        x * taille_case + 1 * taille_case // 4 - taille_case // 20,
        y * taille_case + 1 * taille_case // 3,
        taille_case // 9,
        couleur="black",
        remplissage="red",
    )
    rectangle(
        x * taille_case + 1 * taille_case // 4 - taille_case // 20 - taille_case // 9,
        y * taille_case + 1 * taille_case // 3,
        x * taille_case + 1 * taille_case // 4 - taille_case // 20 + taille_case // 9,
        y * taille_case + 1 * taille_case // 3 - taille_case // 9,
        couleur=fond_,
        remplissage=fond_,
    )
    polygone(
        [
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 9,
                y * taille_case + 1 * taille_case // 3,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 9,
                y * taille_case + 1 * taille_case // 3 - taille_case // 9,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 18,
                y * taille_case + 1 * taille_case // 3 - taille_case // 18,
            ),
            (
                x * taille_case + 1 * taille_case // 4 - taille_case // 20,
                y * taille_case + 1 * taille_case // 3 - taille_case // 9,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 18,
                y * taille_case + 1 * taille_case // 3 - taille_case // 18,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 9,
                y * taille_case + 1 * taille_case // 3 - taille_case // 9,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 9,
                y * taille_case + 1 * taille_case // 3,
            ),
        ],
        couleur="black",
        remplissage="red",
    )
    ligne(
        x * taille_case
        + 1 * taille_case // 4
        - taille_case // 20
        - taille_case // 9
        + 1,
        y * taille_case + 1 * taille_case // 3,
        x * taille_case
        + 1 * taille_case // 4
        - taille_case // 20
        + taille_case // 9
        - 1,
        y * taille_case + 1 * taille_case // 3,
        couleur="red",
        epaisseur=1,
    )
    cercle(
        x * taille_case + 1 * taille_case // 4 - taille_case // 20,
        y * taille_case + 1 * taille_case // 3,
        taille_case // 15,
        couleur="black",
        remplissage="orange",
    )
    polygone(
        [
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 15,
                y * taille_case + 1 * taille_case // 3,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 15,
                y * taille_case + 1 * taille_case // 3 - taille_case // 15,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 30,
                y * taille_case + 1 * taille_case // 3 - taille_case // 30,
            ),
            (
                x * taille_case + 1 * taille_case // 4 - taille_case // 20,
                y * taille_case + 1 * taille_case // 3 - taille_case // 15,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 30,
                y * taille_case + 1 * taille_case // 3 - taille_case // 30,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 15,
                y * taille_case + 1 * taille_case // 3 - taille_case // 15,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 15,
                y * taille_case + 1 * taille_case // 3,
            ),
        ],
        couleur="black",
        remplissage="orange",
    )
    ligne(
        x * taille_case
        + 1 * taille_case // 4
        - taille_case // 20
        - taille_case // 15
        + 1,
        y * taille_case + 1 * taille_case // 3,
        x * taille_case
        + 1 * taille_case // 4
        - taille_case // 20
        + taille_case // 15
        - 1,
        y * taille_case + 1 * taille_case // 3,
        couleur="orange",
        epaisseur=1,
    )

    if nbdiamand >= diamand and var["porte"] == 1:
        cercle(
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 14,
            y * taille_case + 3 * taille_case // 4 - taille_case // 8,
            taille_case // 15,
            couleur="black",
            remplissage="yellow",
        )
        cercle(
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 15,
            y * taille_case + 3 * taille_case // 4 - taille_case // 8,
            taille_case // 28,
            couleur="black",
            remplissage="lightpink",
        )
        rectangle(
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 15,
            y * taille_case + 3 * taille_case // 4 - taille_case // 6,
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 12,
            y * taille_case + 1 * taille_case // 4,
            couleur="black",
            remplissage="yellow",
        )
        rectangle(
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 15,
            y * taille_case + 1 * taille_case // 4,
            x * taille_case + 3 * taille_case // 4,
            y * taille_case + 2 * taille_case // 5,
            couleur="black",
            remplissage="yellow",
        )


def mur(x, y, taille_case, *args):
    """Dessine un mur aux coordonnées x, y"""
    rectangle(  # fond
        x * taille_case,
        y * taille_case,
        taille_case + x * taille_case,
        taille_case + y * taille_case - 1,
        couleur="gray15",
        remplissage="gray15",
    )
    ligne(  # deuxième ligne horizontale
        x * taille_case,
        y * taille_case + taille_case // 3,
        taille_case + x * taille_case + 1,
        (taille_case + y * taille_case - 1) - 2 * taille_case // 3,
        couleur="white",
        epaisseur=taille_case // 25,
    )
    ligne(  # troisième ligne horizontale
        x * taille_case,
        y * taille_case + 2 * taille_case // 3,
        taille_case + x * taille_case + 1,
        (taille_case + y * taille_case - 1) - taille_case // 3,
        couleur="white",
        epaisseur=taille_case // 25,
    )
    ligne(  # première ligne horitontale
        x * taille_case,
        y * taille_case,
        taille_case + x * taille_case + 1,
        (taille_case + y * taille_case - 1) - 3 * taille_case // 3,
        couleur="white",
        epaisseur=taille_case // 25,
    )
    ligne(  # quatrième ligne horizontale
        x * taille_case,
        y * taille_case + 3 * taille_case // 3,
        taille_case + x * taille_case + 1,
        taille_case + y * taille_case - 1,
        couleur="white",
        epaisseur=taille_case // 25,
    )
    ligne(  # Première ligne verticale
        x * taille_case + 1 * taille_case // 4,
        y * taille_case,
        x * taille_case + 1 * taille_case // 4,
        y * taille_case + taille_case // 3,
        couleur="white",
        epaisseur=taille_case // 25,
    )
    ligne(  # Deuxième ligne verticale
        x * taille_case + 1 * taille_case // 2,
        y * taille_case + taille_case // 3,
        x * taille_case + 1 * taille_case // 2,
        y * taille_case + 2 * taille_case // 3,
        couleur="white",
        epaisseur=taille_case // 25,
    )
    ligne(  # Troisième ligne verticale
        x * taille_case + 3 * taille_case // 4,
        y * taille_case + 2 * taille_case // 3,
        x * taille_case + 3 * taille_case // 4,
        y * taille_case + taille_case,
        couleur="white",
        epaisseur=taille_case // 25,
    )


def diamand(x, y, taille_case, *args):
    """Dessine un diamand aux coordonnées x, y"""
    polygone(
        [
            (x * taille_case + taille_case // 2, y * taille_case + taille_case),
            (x * taille_case, y * taille_case + taille_case // 6),
            (x * taille_case + taille_case // 6, y * taille_case + 1),
            (x * taille_case + 5 * taille_case // 6, y * taille_case + 1),
            (x * taille_case + taille_case, y * taille_case + taille_case // 6),
        ],
        couleur="black",
        remplissage="lightblue",
        epaisseur=taille_case // 25,
    )
    for i in range(4):
        ligne(
            x * taille_case + i * taille_case // 3,
            y * taille_case + taille_case // 6,
            x * taille_case + taille_case // 2,
            y * taille_case + taille_case,
            epaisseur=taille_case // 25,
        )
    for i in range(3):
        ligne(
            x * taille_case + taille_case // 6 + i * taille_case // 3,
            y * taille_case,
            x * taille_case + taille_case // 3 + i * taille_case // 3,
            y * taille_case + taille_case // 6,
            epaisseur=taille_case // 25,
        )
        ligne(
            x * taille_case + taille_case // 6 + i * taille_case // 3,
            y * taille_case,
            x * taille_case + i * taille_case // 3,
            y * taille_case + taille_case // 6,
            epaisseur=taille_case // 25,
        )
    ligne(
        x * taille_case,
        y * taille_case + taille_case // 6,
        x * taille_case + taille_case,
        y * taille_case + taille_case // 6,
        epaisseur=taille_case // 25,
    )


def sortie(x, y, taille_case, *args):
    """Dessine la sortie aux coordonnées x, y"""
    if var["porte"] == 0:
        rectangle(
            x * taille_case,
            y * taille_case + 2 * taille_case // 3,
            x * taille_case + taille_case,
            y * taille_case + taille_case,
            couleur="gray20",
            remplissage="gray20",
        )
        rectangle(
            x * taille_case + taille_case // 3,
            y * taille_case + taille_case // 3,
            x * taille_case + taille_case,
            y * taille_case + 2 * taille_case // 3,
            couleur="gray20",
            remplissage="gray20",
        )
        rectangle(
            x * taille_case + 2 * taille_case // 3,
            y * taille_case,
            x * taille_case + taille_case,
            y * taille_case + taille_case,
            couleur="gray20",
            remplissage="gray20",
        )
    else:
        cercle(
            x * taille_case + taille_case // 2,
            y * taille_case + taille_case // 2,
            taille_case // 2,
            couleur="brown4",
            remplissage="brown4",
        )
        rectangle(
            x * taille_case,
            y * taille_case + taille_case // 2,
            x * taille_case + taille_case,
            y * taille_case + taille_case,
            couleur="brown4",
            remplissage="brown4",
        )
        ligne(
            x * taille_case + taille_case // 4,
            y * taille_case + taille_case // 11,
            x * taille_case + taille_case // 4,
            y * taille_case + taille_case,
            epaisseur=5,
        )
        ligne(
            x * taille_case + 3 * taille_case // 4,
            y * taille_case + taille_case // 11,
            x * taille_case + 3 * taille_case // 4,
            y * taille_case + taille_case,
            epaisseur=5,
        )
        rectangle(
            x * taille_case + taille_case // 4,
            y * taille_case + taille_case // 3,
            x * taille_case + 3 * taille_case // 4,
            y * taille_case + 5 * taille_case // 6,
            couleur="yellow",
            remplissage="yellow",
        )
        cercle(
            x * taille_case + taille_case // 2,
            y * taille_case + taille_case // 2,
            taille_case // 12,
            couleur="black",
            remplissage="black",
        )
        rectangle(
            x * taille_case + taille_case // 2 - taille_case // 22,
            y * taille_case + taille_case // 2,
            x * taille_case + taille_case // 2 + taille_case // 22,
            y * taille_case + 5 * taille_case // 7,
            couleur="black",
            remplissage="black",
        )
        cercle(
            x * taille_case + taille_case // 2,
            y * taille_case + 5 * taille_case // 7,
            taille_case // 22,
            remplissage="black",
        )


def pierre_eboulement(x, y, taille_case, *args):
    """Affiche pierre qui tombe"""
    polygone(
        [
            (x * taille_case, y * taille_case + taille_case // 2),
            (x * taille_case, y * taille_case - taille_case // 2),
            (x * taille_case + taille_case // 4, y * taille_case - taille_case // 4),
            (x * taille_case + taille_case // 2, y * taille_case - taille_case // 2),
            (
                x * taille_case + 3 * taille_case // 4,
                y * taille_case - taille_case // 4,
            ),
            (x * taille_case + taille_case, y * taille_case - taille_case // 2),
            (x * taille_case + taille_case, y * taille_case + taille_case // 2),
        ],
        couleur="red",
        remplissage="red",
    )
    polygone(
        [
            (x * taille_case + taille_case // 14, y * taille_case + taille_case // 2),
            (
                x * taille_case + taille_case // 14,
                y * taille_case - taille_case // 2 + taille_case // 8,
            ),
            (
                x * taille_case + taille_case // 4,
                y * taille_case - taille_case // 4 + taille_case // 8,
            ),
            (
                x * taille_case + taille_case // 2,
                y * taille_case - taille_case // 2 + taille_case // 8,
            ),
            (
                x * taille_case + 3 * taille_case // 4,
                y * taille_case - taille_case // 4 + taille_case // 8,
            ),
            (
                x * taille_case + taille_case - taille_case // 14,
                y * taille_case - taille_case // 2 + taille_case // 8,
            ),
            (
                x * taille_case + taille_case - taille_case // 14,
                y * taille_case + taille_case // 2,
            ),
        ],
        couleur="orange",
        remplissage="orange",
    )
    polygone(
        [
            (x * taille_case + taille_case // 8, y * taille_case + taille_case // 2),
            (
                x * taille_case + taille_case // 8,
                y * taille_case - taille_case // 2 + taille_case // 4,
            ),
            (
                x * taille_case + taille_case // 4,
                y * taille_case - taille_case // 4 + taille_case // 4,
            ),
            (
                x * taille_case + taille_case // 2,
                y * taille_case - taille_case // 2 + taille_case // 4,
            ),
            (
                x * taille_case + 3 * taille_case // 4,
                y * taille_case - taille_case // 4 + taille_case // 4,
            ),
            (
                x * taille_case + taille_case - taille_case // 8,
                y * taille_case - taille_case // 2 + taille_case // 4,
            ),
            (
                x * taille_case + taille_case - taille_case // 8,
                y * taille_case + taille_case // 2,
            ),
        ],
        couleur="yellow",
        remplissage="yellow",
    )
    cercle(
        x * taille_case + taille_case / 2,
        y * taille_case + taille_case / 2,
        (taille_case / 2) - 1,
        couleur="gray39",
        remplissage="gray39",
    )


def diamand_eboulement(x, y, taille_case, *args):
    """affiche diamant qui tombe"""
    polygone(
        [
            (x * taille_case, y * taille_case + taille_case // 6),
            (x * taille_case, y * taille_case - taille_case // 2),
            (x * taille_case + taille_case // 4, y * taille_case - taille_case // 4),
            (x * taille_case + taille_case // 2, y * taille_case - taille_case // 2),
            (
                x * taille_case + 3 * taille_case // 4,
                y * taille_case - taille_case // 4,
            ),
            (x * taille_case + taille_case, y * taille_case - taille_case // 2),
            (x * taille_case + taille_case, y * taille_case + taille_case // 6),
        ],
        couleur="red",
        remplissage="red",
    )
    polygone(
        [
            (x * taille_case + taille_case // 14, y * taille_case + taille_case // 6),
            (
                x * taille_case + taille_case // 14,
                y * taille_case - taille_case // 2 + taille_case // 8,
            ),
            (
                x * taille_case + taille_case // 4,
                y * taille_case - taille_case // 4 + taille_case // 8,
            ),
            (
                x * taille_case + taille_case // 2,
                y * taille_case - taille_case // 2 + taille_case // 8,
            ),
            (
                x * taille_case + 3 * taille_case // 4,
                y * taille_case - taille_case // 4 + taille_case // 8,
            ),
            (
                x * taille_case + taille_case - taille_case // 14,
                y * taille_case - taille_case // 2 + taille_case // 8,
            ),
            (
                x * taille_case + taille_case - taille_case // 14,
                y * taille_case + taille_case // 6,
            ),
        ],
        couleur="orange",
        remplissage="orange",
    )
    polygone(
        [
            (x * taille_case + taille_case // 8, y * taille_case + taille_case // 6),
            (
                x * taille_case + taille_case // 8,
                y * taille_case - taille_case // 2 + taille_case // 4,
            ),
            (
                x * taille_case + taille_case // 4,
                y * taille_case - taille_case // 4 + taille_case // 4,
            ),
            (
                x * taille_case + taille_case // 2,
                y * taille_case - taille_case // 2 + taille_case // 4,
            ),
            (
                x * taille_case + 3 * taille_case // 4,
                y * taille_case - taille_case // 4 + taille_case // 4,
            ),
            (
                x * taille_case + taille_case - taille_case // 8,
                y * taille_case - taille_case // 2 + taille_case // 4,
            ),
            (
                x * taille_case + taille_case - taille_case // 8,
                y * taille_case + taille_case // 6,
            ),
        ],
        couleur="yellow",
        remplissage="yellow",
    )
    polygone(
        [
            (x * taille_case + taille_case // 2, y * taille_case + taille_case),
            (x * taille_case, y * taille_case + taille_case // 6),
            (x * taille_case + taille_case // 6, y * taille_case + 1),
            (x * taille_case + 5 * taille_case // 6, y * taille_case + 1),
            (x * taille_case + taille_case, y * taille_case + taille_case // 6),
        ],
        couleur="lightblue",
        remplissage="lightblue",
    )
    for i in range(4):
        ligne(
            x * taille_case + i * taille_case // 3,
            y * taille_case + taille_case // 6,
            x * taille_case + taille_case // 2,
            y * taille_case + taille_case,
            epaisseur=taille_case // 25,
        )
    for i in range(3):
        ligne(
            x * taille_case + taille_case // 6 + i * taille_case // 3,
            y * taille_case,
            x * taille_case + taille_case // 3 + i * taille_case // 3,
            y * taille_case + taille_case // 6,
            epaisseur=taille_case // 25,
        )
        ligne(
            x * taille_case + taille_case // 6 + i * taille_case // 3,
            y * taille_case,
            x * taille_case + i * taille_case // 3,
            y * taille_case + taille_case // 6,
            epaisseur=taille_case // 25,
        )
    ligne(
        x * taille_case,
        y * taille_case + taille_case // 6,
        x * taille_case + taille_case,
        y * taille_case + taille_case // 6,
        epaisseur=taille_case // 25,
    )


def fond(couleur):
    """Affiche le fond de la couleur demander"""
    rectangle(
        0,
        0,
        var["dimension_fenetre"],
        var["dimension_fenetre"] + var["bandeau"],
        couleur=couleur,
        remplissage=couleur,
    )


def fond_score_temps_diams(score, tempsrestant, nbdiamandrestant):
    """affiche un fond(banderolle) avec le nombre de temps restant et de diamant"""
    rectangle(
        0,
        var["dimension_fenetre"],
        var["dimension_fenetre"],
        var["dimension_fenetre"] + var["bandeau"],
        remplissage="black",
    )
    texte(
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] + 70,
        "Score:{}".format(score),
        couleur="white",
        ancrage="center",
        taille=15,
        police="Impact",
    )
    texte(
        var["dimension_fenetre"] // 4,
        var["dimension_fenetre"] + 30,
        "Temps Restant:{}".format(tempsrestant),
        couleur="white",
        ancrage="center",
        taille=15,
        police="Impact",
    )
    texte(
        3 * var["dimension_fenetre"] // 4,
        var["dimension_fenetre"] + 30,
        "Nombre de diamant{0} manquant{0}:{1}".format(
            ["", "s"][nbdiamandrestant > 1], nbdiamandrestant
        ),
        couleur="white",
        ancrage="center",
        taille=15,
        police="Impact",
    )


def personnage_victorieux():
    """Affiche ce personnage en cas de victoire"""
    cercle(
        var["dimension_fenetre"] // 2,
        2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 8,
        couleur="black",
        remplissage="black",
    )
    rectangle(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
        2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
        couleur="lightpink",
        remplissage="lightpink",
    )
    # Main à gauche puis à droite
    cercle(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 4,
        3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 12,
        couleur="black",
        remplissage="lightpink",
    )
    cercle(
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 4,
        3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 12,
        couleur="black",
        remplissage="lightpink",
    )
    # pied à gauche puis à droite
    cercle(
        var["dimension_fenetre"] // 3,
        8 * var["dimension_fenetre"] // 9,
        var["dimension_fenetre"] // 12,
        couleur="black",
        remplissage="red",
    )
    cercle(
        2 * var["dimension_fenetre"] // 3,
        8 * var["dimension_fenetre"] // 9,
        var["dimension_fenetre"] // 12,
        couleur="black",
        remplissage="red",
    )
    # Tête
    cercle(
        var["dimension_fenetre"] // 2,
        2 * var["dimension_fenetre"] // 3,
        var["dimension_fenetre"] // 4,
        couleur="black",
        remplissage="lightpink",
    )
    # Bouche
    cercle(
        var["dimension_fenetre"] // 2,
        2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 12,
        couleur="black",
        remplissage="black",
    )
    # 6 prochaine = yeux(droite puis gauche)
    cercle(
        var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 20,
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
        var["dimension_fenetre"] // 20,
        couleur="black",
        remplissage="black",
    )
    cercle(
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
        var["dimension_fenetre"] // 20,
        couleur="black",
        remplissage="black",
    )
    cercle(
        var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 20,
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
        var["dimension_fenetre"] // 24,
        couleur="lightpink",
        remplissage="lightpink",
    )
    cercle(
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
        var["dimension_fenetre"] // 24,
        couleur="lightpink",
        remplissage="lightpink",
    )
    rectangle(
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 10,
        2 * var["dimension_fenetre"] // 3,
        2 * var["dimension_fenetre"] // 3,
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 17,
        couleur="lightpink",
        remplissage="lightpink",
    )
    rectangle(
        var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 10,
        2 * var["dimension_fenetre"] // 3,
        var["dimension_fenetre"] // 3,
        2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 17,
        couleur="lightpink",
        remplissage="lightpink",
    )


def personnage_defaitiste():
    """Affiche ce personnage en cas de défaite"""
    cercle(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 4,
        3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 12,
        couleur="lightpink",
        remplissage="lightpink",
    )
    cercle(
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 4,
        3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 12,
        couleur="lightpink",
        remplissage="lightpink",
    )
    cercle(
        var["dimension_fenetre"] // 3,
        8 * var["dimension_fenetre"] // 9,
        var["dimension_fenetre"] // 12,
        couleur="black",
        remplissage="red",
    )
    cercle(
        2 * var["dimension_fenetre"] // 3,
        8 * var["dimension_fenetre"] // 9,
        var["dimension_fenetre"] // 12,
        couleur="black",
        remplissage="red",
    )
    # Tête
    cercle(
        var["dimension_fenetre"] // 2,
        2 * var["dimension_fenetre"] // 3,
        var["dimension_fenetre"] // 4,
        couleur="black",
        remplissage="lightpink",
    )
    # Bouche
    cercle(
        var["dimension_fenetre"] // 2,
        2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 12,
        couleur="black",
        remplissage="black",
    )
    # 4 prochaines = yeux(gauche puis droite)
    ligne(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 20,
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
        couleur="black",
        epaisseur=10,
    )
    ligne(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 20,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
        couleur="black",
        epaisseur=10,
    )
    ligne(
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 20,
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
        couleur="black",
        epaisseur=10,
    )
    ligne(
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 20,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
        couleur="black",
        epaisseur=10,
    )
    # baton cassé main
    ligne(
        var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7,
        3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7,
        3 * var["dimension_fenetre"] // 4 + var["dimension_fenetre"] // 15 - 10,
        couleur="saddle brown",
        epaisseur=5,
    )
    ligne(
        var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7 - 5,
        3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7 - 5,
        3 * var["dimension_fenetre"] // 4 + var["dimension_fenetre"] // 15 + 30,
        couleur="saddle brown",
        epaisseur=5,
    )
    # Pioche
    cercle(
        var["dimension_fenetre"] // 8,
        14 * var["dimension_fenetre"] // 15,
        var["dimension_fenetre"] // 14,
        couleur="LightSteelBlue2",
        remplissage="LightSteelBlue2",
    )
    cercle(
        var["dimension_fenetre"] // 7,
        14 * var["dimension_fenetre"] // 15,
        var["dimension_fenetre"] // 14,
        couleur="black",
        remplissage="black",
    )
    # baton au sol
    ligne(
        var["dimension_fenetre"] // 14,
        14 * var["dimension_fenetre"] // 15,
        var["dimension_fenetre"] // 5,
        14 * var["dimension_fenetre"] // 15,
        couleur="saddle brown",
        epaisseur=5,
    )
    ligne(
        var["dimension_fenetre"] // 14,
        14 * var["dimension_fenetre"] // 15 - 5,
        var["dimension_fenetre"] // 5 - 30,
        14 * var["dimension_fenetre"] // 15 - 5,
        couleur="saddle brown",
        epaisseur=5,
    )


def coffre():
    """Affiche un coffre"""
    # or milieu, droite puis gauche
    rectangle(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 10,
        couleur="gold",
        remplissage="gold",
    )
    rectangle(
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
        var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 10,
        couleur="gold",
        remplissage="gold",
    )
    rectangle(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 24,
        var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 24,
        var["dimension_fenetre"] // 10,
        couleur="gold",
        remplissage="gold",
    )
    # COffre
    rectangle(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 6,
        var["dimension_fenetre"] // 10,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 6,
        var["dimension_fenetre"] // 5,
        couleur="saddle brown",
        remplissage="saddle brown",
    )
    # ligne noir droite puis gauche
    ligne(
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 10,
        var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 5,
        couleur="black",
        epaisseur=10,
    )
    ligne(
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 10,
        var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 12,
        var["dimension_fenetre"] // 5,
        couleur="black",
        epaisseur=10,
    )
    # ligne rayonnement droite à gauche(inversement deux dernier)
    ligne(
        2.75 * var["dimension_fenetre"] // 4,
        15,
        3 * var["dimension_fenetre"] // 5,
        var["dimension_fenetre"] // 14,
        couleur="gold",
        epaisseur=3,
    )
    ligne(
        3 * var["dimension_fenetre"] // 5,
        15,
        8 * var["dimension_fenetre"] // 15,
        var["dimension_fenetre"] // 14,
        couleur="gold",
        epaisseur=3,
    )
    ligne(
        1.5 * var["dimension_fenetre"] // 5,
        15,
        6 * var["dimension_fenetre"] // 15,
        var["dimension_fenetre"] // 14,
        couleur="gold",
        epaisseur=3,
    )
    ligne(
        2 * var["dimension_fenetre"] // 5,
        15,
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 14,
        couleur="gold",
        epaisseur=3,
    )


def lumiere(longueur):
    """Lumière du perso"""
    cercle(
        var["dimension_fenetre"] // 2 + var["taille_case"] // 2,
        var["dimension_fenetre"] // 2 + var["taille_case"] // 2,
        50 * var["taille_case"],
        couleur="goldenrod4",
        remplissage="goldenrod4",
    )

    cercle(
        var["dimension_fenetre"] // 2 + var["taille_case"] // 2,
        var["dimension_fenetre"] // 2 + var["taille_case"] // 2,
        var["taille_case"] - 3 * longueur // 4,
        couleur="goldenrod3",
        remplissage="goldenrod3",
    )


def lumiere_escalier():
    """lumière afficher quand la porte est ouverte"""
    cercle(
        (var["pos_sortie_x"] + (var["nb_cases"] // 2 - var["pos_x"]))
        * var["taille_case"]
        + var["taille_case"] / 2,
        (var["pos_sortie_y"] + (var["nb_cases"] // 2 - var["pos_y"]))
        * var["taille_case"]
        + var["taille_case"] / 2,
        var["taille_case"] * 2 / 3,
        couleur="white",
        remplissage="white",
    )


def noir_lumiere(epaisseurd):
    """Affiche un cercle dont l'intérieur est le jeu, l'extérieur est noir pour un effet de lumière"""
    cercle(
        var["dimension_fenetre"] // 2 + var["taille_case"] // 2,
        var["dimension_fenetre"] // 2 + var["taille_case"] // 2,
        var["taille_case"] * 6,
        epaisseur=epaisseurd,
    )


def menu_score(nbdiamand, tempsrestant, suivant, score):
    """affiche un menu avec les différentes parties du score """
    fond("cyan")
    texte(10000000, 0, "5c c ccc c ccccc", taille=24, police="Arial")
    rectangle(
        var["dimension_fenetre"] // 6,
        var["dimension_fenetre"] // 6,
        5 * var["dimension_fenetre"] // 6,
        5 * var["dimension_fenetre"] // 6,
        couleur="white",
        remplissage="gray39",
    )
    var["porte"] = 1
    diamand(0, 0.1, 100)
    diamand(5, 0.1, 100)
    diamand(0, 5.1, 100)
    diamand(5, 5.1, 100)
    rockford(0, 2.5, 100, 0, 0, "cyan")
    rockford(5, 2.5, 100, 0, 0, "cyan")
    couronne(2.5, 0.1, 100)
    a = time()
    while time() - a <= 1:
        texte(
            var["dimension_fenetre"] // 2
            - longueur_texte("{} x 350 = {}".format(int(score) // 350, int(score)))
            // 2,
            var["dimension_fenetre"] // 3 - hauteur_texte() // 2,
            "{} x 350 = {}".format(int(score) // 350, int(score)),
            taille=24,
            police="Arial",
            couleur="red",
        )
        mise_a_jour()
    while time() - a <= 2:
        texte(
            var["dimension_fenetre"] // 2
            - longueur_texte("+ {} x 100 = {}".format(tempsrestant, tempsrestant * 100))
            // 2,
            var["dimension_fenetre"] // 2 - hauteur_texte() // 2,
            "+ {} x 100 = {}".format(tempsrestant, tempsrestant * 100),
            taille=24,
            police="Arial",
            couleur="red",
        )
        mise_a_jour()
    while time() - a <= 3:
        ligne(
            var["dimension_fenetre"] // 2
            - longueur_texte("Score final : {}".format(int(score) + tempsrestant * 100))
            // 2,
            4 * var["dimension_fenetre"] // 7 - hauteur_texte() // 2,
            var["dimension_fenetre"] // 2
            + longueur_texte("Score final : {}".format(int(score) + tempsrestant * 100))
            // 2,
            4 * var["dimension_fenetre"] // 7 - hauteur_texte() // 2,
            couleur="red",
            epaisseur=3,
        )

        texte(
            var["dimension_fenetre"] // 2
            - longueur_texte(
                "Score final : {}".format(nbdiamand * 350 + tempsrestant * 100)
            )
            // 2,
            2 * var["dimension_fenetre"] // 3 - hauteur_texte() // 2,
            "Score final : {}".format(int(score) + tempsrestant * 100),
            taille=24,
            police="Arial",
            couleur="red",
        )
        mise_a_jour()
    S = fonction.encadrement(
        "SUIVANT",
        2 * var["dimension_fenetre"] // 3,
        var["dimension_fenetre"] + 30,
        "red",
        "red",
        24,
        5,
        5,
        "Impact",
    )
    while suivant == 0:
        suivant = fonction.test_clic(attente_clic(), S)
    return suivant, int(score) + tempsrestant * 100


def affiche_score_victoire(score):
    """affiche le score en cas de victoire"""
    texte(10000000, 0, "5c c ccc c ccccc", taille=24, police="Arial")
    texte(
        var["dimension_fenetre"] // 2
        - longueur_texte("Score final : {}".format(score)) // 2,
        var["dimension_fenetre"] + 50 - hauteur_texte() // 2,
        "Score final : {}".format(score),
        taille=24,
        police="Arial",
        couleur="red",
    )


def couronne(x, y, taille_case):
    """affiche une couronne"""
    polygone(
        [
            (x * taille_case - taille_case // 2, y * taille_case + taille_case),
            (x * taille_case - taille_case // 2, y * taille_case),
            (x * taille_case, y * taille_case + taille_case // 2),
            (x * taille_case + taille_case // 2, y * taille_case),
            (x * taille_case + taille_case, y * taille_case + taille_case // 2),
            (x * taille_case + 3 * taille_case // 2, y * taille_case),
            (x * taille_case + 3 * taille_case // 2, y * taille_case + taille_case),
        ],
        couleur="yellow",
        remplissage="yellow",
    )
    polygone(
        [
            (x * taille_case + taille_case // 2, y * taille_case + taille_case // 4),
            (
                x * taille_case + 2 * taille_case // 5,
                y * taille_case + 5 * taille_case // 12,
            ),
            (
                x * taille_case + 2 * taille_case // 5,
                y * taille_case + 9 * taille_case // 12,
            ),
            (
                x * taille_case + taille_case // 2,
                y * taille_case + 11 * taille_case // 12,
            ),
            (
                x * taille_case + 3 * taille_case // 5,
                y * taille_case + 9 * taille_case // 12,
            ),
            (
                x * taille_case + 3 * taille_case // 5,
                y * taille_case + 5 * taille_case // 12,
            ),
        ],
        couleur="black",
        remplissage="green",
    )
    polygone(
        [
            (
                x * taille_case + taille_case // 2,
                y * taille_case + 6 * taille_case // 20,
            ),
            (
                x * taille_case + 9 * taille_case // 20,
                y * taille_case + 5 * taille_case // 12,
            ),
            (
                x * taille_case + 9 * taille_case // 20,
                y * taille_case + 9 * taille_case // 12,
            ),
            (
                x * taille_case + taille_case // 2,
                y * taille_case + 11 * taille_case // 12 - taille_case // 20,
            ),
            (
                x * taille_case + 11 * taille_case // 20,
                y * taille_case + 9 * taille_case // 12,
            ),
            (
                x * taille_case + 11 * taille_case // 20,
                y * taille_case + 5 * taille_case // 12,
            ),
        ],
        couleur="black",
        remplissage="green2",
    )
    # polygone(
    #     [
    #         (x * taille_case + taille_case // 6, y * taille_case + 6 * taille_case // 20),
    #         (x * taille_case + taille_case // 6 - taille_case // 30,
    #         y * taille_case + 5 * taille_case // 12),
    #         (x * taille_case + 9 * taille_case // 20,
    #         y * taille_case + 9 * taille_case // 12),
    #         (x * taille_case + taille_case // 6,
    #         y * taille_case + 11 * taille_case // 12 - taille_case // 20),
    #         (x * taille_case + 11 * taille_case // 20,
    #         y * taille_case + 9 * taille_case // 12),
    #         (x * taille_case + 11 * taille_case // 20,
    #          y * taille_case + 5 * taille_case // 12),
    #     ],
    #     couleur = 'black',
    #     remplissage = 'red'
    # )


def rockford_dead(x, y, taille_case, nbdiamand, diamand, fond_):
    """Dessine rockford aux coordonnées x, y"""
    # main à gauche
    cercle(
        x * taille_case + taille_case // 2 - taille_case // 4,
        y * taille_case + 3 * taille_case // 4 - taille_case // 8,
        taille_case // 12,
        couleur="black",
        remplissage="lightpink",
    )
    # main à droite
    cercle(
        x * taille_case + taille_case // 2 + taille_case // 4,
        y * taille_case + 3 * taille_case // 4 - taille_case // 8,
        taille_case // 12,
        couleur="black",
        remplissage="lightpink",
    )
    # pied à gauche
    cercle(
        x * taille_case + taille_case // 3,
        y * taille_case + 8 * taille_case // 9,
        taille_case // 12,
        couleur="black",
        remplissage="red",
    )
    # pied à droite
    cercle(
        x * taille_case + 2 * taille_case // 3,
        y * taille_case + 8 * taille_case // 9,
        taille_case // 12,
        couleur="black",
        remplissage="red",
    )
    # Tête
    cercle(
        x * taille_case + taille_case // 2,
        y * taille_case + 2 * taille_case // 3,
        taille_case // 4,
        couleur="black",
        remplissage="lightpink",
    )
    # Bouche(cercle + rectangle)
    cercle(
        x * taille_case + taille_case // 2,
        y * taille_case + 2 * taille_case // 3 + taille_case // 12,
        taille_case // 8,
        couleur="black",
        remplissage="black",
    )
    rectangle(
        x * taille_case + taille_case // 2 - taille_case // 8,
        y * taille_case + 2 * taille_case // 3 - taille_case // 12,
        x * taille_case + taille_case // 2 + taille_case // 8,
        y * taille_case + 2 * taille_case // 3 + taille_case // 12,
        couleur="lightpink",
        remplissage="lightpink",
    )
    ligne(
        x * taille_case + taille_case // 2 - taille_case // 20,
        y * taille_case + taille_case // 2,
        x * taille_case + taille_case // 2 - taille_case // 8,
        y * taille_case + taille_case // 2 + taille_case // 10,
        couleur="black",
        epaisseur=3,
    )
    ligne(
        x * taille_case + taille_case // 2 - taille_case // 8,
        y * taille_case + taille_case // 2,
        x * taille_case + taille_case // 2 - taille_case // 20,
        y * taille_case + taille_case // 2 + taille_case // 10,
        couleur="black",
        epaisseur=3,
    )
    ligne(
        x * taille_case + taille_case // 2 + taille_case // 20,
        y * taille_case + taille_case // 2,
        x * taille_case + taille_case // 2 + taille_case // 8,
        y * taille_case + taille_case // 2 + taille_case // 10,
        couleur="black",
        epaisseur=3,
    )
    ligne(
        x * taille_case + taille_case // 2 + taille_case // 8,
        y * taille_case + taille_case // 2,
        x * taille_case + taille_case // 2 + taille_case // 20,
        y * taille_case + taille_case // 2 + taille_case // 10,
        couleur="black",
        epaisseur=3,
    )
    # Torche
    rectangle(
        x * taille_case + 1 * taille_case // 4 - taille_case // 12,
        y * taille_case + 1 * taille_case // 3,
        x * taille_case + 1 * taille_case // 5 + taille_case // 30,
        y * taille_case + 3 * taille_case // 4 - taille_case // 8,
        couleur="black",
        remplissage="sienna4",
    )
    cercle(
        x * taille_case + 1 * taille_case // 4 - taille_case // 20,
        y * taille_case + 1 * taille_case // 3,
        taille_case // 9,
        couleur="black",
        remplissage="red",
    )
    rectangle(
        x * taille_case + 1 * taille_case // 4 - taille_case // 20 - taille_case // 9,
        y * taille_case + 1 * taille_case // 3,
        x * taille_case + 1 * taille_case // 4 - taille_case // 20 + taille_case // 9,
        y * taille_case + 1 * taille_case // 3 - taille_case // 9,
        couleur=fond_,
        remplissage=fond_,
    )
    polygone(
        [
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 9,
                y * taille_case + 1 * taille_case // 3,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 9,
                y * taille_case + 1 * taille_case // 3 - taille_case // 9,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 18,
                y * taille_case + 1 * taille_case // 3 - taille_case // 18,
            ),
            (
                x * taille_case + 1 * taille_case // 4 - taille_case // 20,
                y * taille_case + 1 * taille_case // 3 - taille_case // 9,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 18,
                y * taille_case + 1 * taille_case // 3 - taille_case // 18,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 9,
                y * taille_case + 1 * taille_case // 3 - taille_case // 9,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 9,
                y * taille_case + 1 * taille_case // 3,
            ),
        ],
        couleur="black",
        remplissage="red",
    )
    ligne(
        x * taille_case
        + 1 * taille_case // 4
        - taille_case // 20
        - taille_case // 9
        + 1,
        y * taille_case + 1 * taille_case // 3,
        x * taille_case
        + 1 * taille_case // 4
        - taille_case // 20
        + taille_case // 9
        - 1,
        y * taille_case + 1 * taille_case // 3,
        couleur="red",
        epaisseur=1,
    )
    cercle(
        x * taille_case + 1 * taille_case // 4 - taille_case // 20,
        y * taille_case + 1 * taille_case // 3,
        taille_case // 15,
        couleur="black",
        remplissage="orange",
    )
    polygone(
        [
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 15,
                y * taille_case + 1 * taille_case // 3,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 15,
                y * taille_case + 1 * taille_case // 3 - taille_case // 15,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                - taille_case // 30,
                y * taille_case + 1 * taille_case // 3 - taille_case // 30,
            ),
            (
                x * taille_case + 1 * taille_case // 4 - taille_case // 20,
                y * taille_case + 1 * taille_case // 3 - taille_case // 15,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 30,
                y * taille_case + 1 * taille_case // 3 - taille_case // 30,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 15,
                y * taille_case + 1 * taille_case // 3 - taille_case // 15,
            ),
            (
                x * taille_case
                + 1 * taille_case // 4
                - taille_case // 20
                + taille_case // 15,
                y * taille_case + 1 * taille_case // 3,
            ),
        ],
        couleur="black",
        remplissage="orange",
    )
    ligne(
        x * taille_case
        + 1 * taille_case // 4
        - taille_case // 20
        - taille_case // 15
        + 1,
        y * taille_case + 1 * taille_case // 3,
        x * taille_case
        + 1 * taille_case // 4
        - taille_case // 20
        + taille_case // 15
        - 1,
        y * taille_case + 1 * taille_case // 3,
        couleur="orange",
        epaisseur=1,
    )

    if nbdiamand >= diamand and var["porte"] == 1:
        cercle(
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 14,
            y * taille_case + 3 * taille_case // 4 - taille_case // 8,
            taille_case // 15,
            couleur="black",
            remplissage="yellow",
        )
        cercle(
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 15,
            y * taille_case + 3 * taille_case // 4 - taille_case // 8,
            taille_case // 28,
            couleur="black",
            remplissage="lightpink",
        )
        rectangle(
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 15,
            y * taille_case + 3 * taille_case // 4 - taille_case // 6,
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 12,
            y * taille_case + 1 * taille_case // 4,
            couleur="black",
            remplissage="yellow",
        )
        rectangle(
            x * taille_case + taille_case // 2 + taille_case // 4 + taille_case // 15,
            y * taille_case + 1 * taille_case // 4,
            x * taille_case + 3 * taille_case // 4,
            y * taille_case + 2 * taille_case // 5,
            couleur="black",
            remplissage="yellow",
        )


def fleche_(x, y, taille, sens):
    """Créer une flèche au coordonnée x, y ayant pour sens droite si sens = 1 et gauche pour sens = -1"""
    assert sens == 1 or sens != 1
    polygone(
        [
            (x * taille, y * taille),
            (x * taille, y * taille + taille),
            (x * taille + taille * sens, y * taille + taille // 2),
        ],
        remplissage="gray50",
        couleur="white",
    )
    return [
        (x * taille, y * taille),
        (x * taille, y * taille + taille),
        (x * taille + taille * sens, y * taille + taille // 2),
    ]


def point_dinterogation():
    """affiche un point d'interrogation pour la map aléatoire"""
    fonction.encadrement(
        "?",
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 7,
        "white",
        "white",
        180,
        10,
        40,
        "Calibri",
    )


def affiche_score(L):
    """affiche le score"""
    for i in range(3):
        texte(1000000, 1000000, L[i], police="Impact", taille=24)
        texte(
            var["dimension_fenetre"] // 2 - longueur_texte(L[i]) // 2,
            3 * var["dimension_fenetre"] // 4 + hauteur_texte() * i,
            L[i],
            police="Impact",
            taille=24,
            couleur="white",
        )


if __name__ == "__main__":
    print("Programme principal: main.py")
