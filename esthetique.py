from upemtk import *
from variable import *

def terre(x, y):
    rectangle(
        x * var["taille_case"],
        y * var["taille_case"],
        x * var["taille_case"] + var["taille_case"] - 1,
        y * var["taille_case"] + var["taille_case"] - 1,
        couleur="sienna4",
        remplissage="sienna4",
    )

def pierre(x, y):
    cercle(
        x * var["taille_case"] + var["taille_case"] / 2,
        y * var["taille_case"] + var["taille_case"] / 2,
        (var["taille_case"] / 2) - 1,
        couleur="gray39",
        remplissage="gray39",
    )

def rockford(x, y):
    cercle(
        x * var["taille_case"] + var["taille_case"] // 2 - var["taille_case"] // 4,
        y * var["taille_case"] + 3 * var["taille_case"] // 4 - var["taille_case"] // 8,
        var["taille_case"] // 12,
        couleur="lightpink",
        remplissage="lightpink",
    )
    # main à droite
    cercle(
        x * var["taille_case"] + var["taille_case"] // 2 + var["taille_case"] // 4,
        y * var["taille_case"] + 3 * var["taille_case"] // 4 - var["taille_case"] // 8,
        var["taille_case"] // 12,
        couleur="lightpink",
        remplissage="lightpink",
    )
    # pied à gauche
    cercle(
        x * var["taille_case"] + var["taille_case"] // 3,
        y * var["taille_case"] + 8 * var["taille_case"] // 9,
        var["taille_case"] // 12,
        couleur="black",
        remplissage="red",
    )
    # pied à droite
    cercle(
        x * var["taille_case"] + 2 * var["taille_case"] // 3,
        y * var["taille_case"] + 8 * var["taille_case"] // 9,
        var["taille_case"] // 12,
        couleur="black",
        remplissage="red",
    )
    # Tête
    cercle(
        x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] + 2 * var["taille_case"] // 3,
        var["taille_case"] // 4,
        couleur="black",
        remplissage="lightpink",
    )
    # Bouche(cercle + rectangle)
    cercle(
        x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] + 2 * var["taille_case"] // 3 + var["taille_case"] // 12,
        var["taille_case"] // 8,
        couleur="black",
        remplissage="black",
    )
    rectangle(
        x * var["taille_case"] + var["taille_case"] // 2 - var["taille_case"] // 8,
        y * var["taille_case"] + 2 * var["taille_case"] // 3 - var["taille_case"] // 12,
        x * var["taille_case"] + var["taille_case"] // 2 + var["taille_case"] // 8,
        y * var["taille_case"] + 2 * var["taille_case"] // 3 + var["taille_case"] // 12,
        couleur="lightpink",
        remplissage="lightpink",
    )
    # Oeil à droite
    cercle(
        x * var["taille_case"] + var["taille_case"] // 3 + var["taille_case"] // 20,
        y * var["taille_case"] + 2 * var["taille_case"] // 3 - var["taille_case"] // 20,
        var["taille_case"] // 20,
        couleur="black",
        remplissage="black",
    )
    # Oeil à gauche
    cercle(
        x * var["taille_case"] + 2 * var["taille_case"] // 3 - var["taille_case"] // 20,
        y * var["taille_case"] + 2 * var["taille_case"] // 3 - var["taille_case"] // 20,
        var["taille_case"] // 20,
        couleur="black",
        remplissage="black",
    )

def mur(x, y):
    rectangle(  # fond
        x * var["taille_case"],
        y * var["taille_case"],
        var["taille_case"] + x * var["taille_case"],
        var["taille_case"] + y * var["taille_case"] - 1,
        couleur="gray15",
        remplissage="gray15",
    )
    ligne(  # deuxième ligne horizontale
        x * var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 3,
        var["taille_case"] + x * var["taille_case"] + 1,
        (var["taille_case"] + y * var["taille_case"] - 1) - 2 * var["taille_case"] // 3,
        couleur="white",
        epaisseur=var["taille_case"] // 25,
    )
    ligne(  # troisième ligne horizontale
        x * var["taille_case"],
        y * var["taille_case"] + 2 * var["taille_case"] // 3,
        var["taille_case"] + x * var["taille_case"] + 1,
        (var["taille_case"] + y * var["taille_case"] - 1) - var["taille_case"] // 3,
        couleur="white",
        epaisseur=var["taille_case"] // 25,
    )
    ligne(  # première ligne horitontale
        x * var["taille_case"],
        y * var["taille_case"],
        var["taille_case"] + x * var["taille_case"] + 1,
        (var["taille_case"] + y * var["taille_case"] - 1) - 3 * var["taille_case"] // 3,
        couleur="white",
        epaisseur=var["taille_case"] // 25,
    )
    ligne(  # quatrième ligne horizontale
        x * var["taille_case"],
        y * var["taille_case"] + 3 * var["taille_case"] // 3,
        var["taille_case"] + x * var["taille_case"] + 1,
        var["taille_case"] + y * var["taille_case"] - 1,
        couleur="white",
        epaisseur=var["taille_case"] // 25,
    )
    ligne(  # Première ligne verticale
        x * var["taille_case"] + 1 * var["taille_case"] // 4,
        y * var["taille_case"],
        x * var["taille_case"] + 1 * var["taille_case"] // 4,
        y * var["taille_case"] + var["taille_case"] // 3,
        couleur="white",
        epaisseur=var["taille_case"] // 25,
    )
    ligne(  # Deuxième ligne verticale
        x * var["taille_case"] + 1 * var["taille_case"] // 2,
        y * var["taille_case"] + var["taille_case"] // 3,
        x * var["taille_case"] + 1 * var["taille_case"] // 2,
        y * var["taille_case"] + 2 * var["taille_case"] // 3,
        couleur="white",
        epaisseur=var["taille_case"] // 25,
    )
    ligne(  # Troisième ligne verticale
        x * var["taille_case"] + 3 * var["taille_case"] // 4,
        y * var["taille_case"] + 2 * var["taille_case"] // 3,
        x * var["taille_case"] + 3 * var["taille_case"] // 4,
        y * var["taille_case"] + var["taille_case"],
        couleur="white",
        epaisseur=var["taille_case"] // 25,
    )

def diamand(x, y):
    polygone(
        [(x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] + var["taille_case"]),
        (x * var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6),
        (x * var["taille_case"] + var["taille_case"] // 6,
        y * var["taille_case"] + 1),
        (x * var["taille_case"] + 5 * var["taille_case"] // 6,
        y * var["taille_case"] + 1),
        (x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6),
        ],
        couleur = "lightblue",
        remplissage = "lightblue"
    )
    for i in range(4):
        ligne(
            x * var["taille_case"] + i * var["taille_case"] // 3,
            y * var["taille_case"] + var["taille_case"] // 6,
            x * var["taille_case"] + var["taille_case"] // 2,
            y * var["taille_case"] + var["taille_case"],
            epaisseur=var["taille_case"] // 25
        )
    for i in range(3):
        ligne(
            x * var["taille_case"] + var["taille_case"] // 6 + i * var["taille_case"] // 3,
            y * var["taille_case"],
            x * var["taille_case"] + var["taille_case"] // 3 + i * var["taille_case"] // 3,
            y * var["taille_case"] + var["taille_case"] // 6,
            epaisseur=var["taille_case"] // 25
        )
        ligne(
            x * var["taille_case"] + var["taille_case"] // 6 + i * var["taille_case"] // 3,
            y * var["taille_case"],
            x * var["taille_case"] + i * var["taille_case"] // 3,
            y * var["taille_case"] + var["taille_case"] // 6,
            epaisseur=var["taille_case"] // 25
        )
    ligne(
        x * var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6 ,
        x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6,
        epaisseur=var["taille_case"] // 25
    )


def sortie(x, y):
    rectangle(
        x * var["taille_case"],
        y * var["taille_case"],
        var["taille_case"] + x * var["taille_case"] - 1,
        var["taille_case"] + y * var["taille_case"] - 1,
        couleur="green",
        remplissage="green",
    )

def pierre_eboulement(x, y):
    polygone(
        [(x * var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 2),
        (x * var["taille_case"],
        y * var["taille_case"] - var["taille_case"] // 2),
        (x * var["taille_case"] + var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4),
        (x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] - var["taille_case"] // 2),
        (x * var["taille_case"] + 3 * var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4),    
        (x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] - var["taille_case"] // 2),
        (x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 2)
        ],
        couleur="red",
        remplissage="red",
    )
    polygone(
        [(x * var["taille_case"] + var["taille_case"] //14,
        y * var["taille_case"] + var["taille_case"] // 2 ),
        (x * var["taille_case"] + var["taille_case"] //14,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 8),
        (x * var["taille_case"] + var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4 + var["taille_case"] // 8),
        (x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 8),
        (x * var["taille_case"] + 3 * var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4 + var["taille_case"] // 8),    
        (x * var["taille_case"] + var["taille_case"] - var["taille_case"] // 14,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 8),
        (x * var["taille_case"] + var["taille_case"] - var["taille_case"] // 14,
        y * var["taille_case"] + var["taille_case"] // 2)
        ],
        couleur="orange",
        remplissage="orange",
    )
    polygone(
        [(x * var["taille_case"] + var["taille_case"] // 8,
        y * var["taille_case"] + var["taille_case"] // 2),
        (x * var["taille_case"] + var["taille_case"] // 8,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 4),
        (x * var["taille_case"] + var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4 + var["taille_case"] // 4),
        (x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 4),
        (x * var["taille_case"] + 3 * var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4 + var["taille_case"] // 4),    
        (x * var["taille_case"] + var["taille_case"] - var["taille_case"] // 8,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 4),
        (x * var["taille_case"] + var["taille_case"] - var["taille_case"] // 8,
        y * var["taille_case"] + var["taille_case"] // 2)
        ],
        couleur="yellow",
        remplissage="yellow",
    )
    cercle(
        x * var["taille_case"] + var["taille_case"] / 2,
        y * var["taille_case"] + var["taille_case"] / 2,
        (var["taille_case"] / 2) - 1,
        couleur="gray39",
        remplissage="gray39",
    )

def diamand_eboulement(x, y):
    polygone(
        [(x * var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6),
        (x * var["taille_case"],
        y * var["taille_case"] - var["taille_case"] // 2),
        (x * var["taille_case"] + var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4),
        (x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] - var["taille_case"] // 2),
        (x * var["taille_case"] + 3 * var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4),    
        (x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] - var["taille_case"] // 2),
        (x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6)
        ],
        couleur="red",
        remplissage="red",
    )
    polygone(
        [(x * var["taille_case"] + var["taille_case"] //14,
        y * var["taille_case"] + var["taille_case"] // 6 ),
        (x * var["taille_case"] + var["taille_case"] //14,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 8),
        (x * var["taille_case"] + var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4 + var["taille_case"] // 8),
        (x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 8),
        (x * var["taille_case"] + 3 * var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4 + var["taille_case"] // 8),    
        (x * var["taille_case"] + var["taille_case"] - var["taille_case"] // 14,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 8),
        (x * var["taille_case"] + var["taille_case"] - var["taille_case"] // 14,
        y * var["taille_case"] + var["taille_case"] // 6)
        ],
        couleur="orange",
        remplissage="orange",
    )
    polygone(
        [(x * var["taille_case"] + var["taille_case"] // 8,
        y * var["taille_case"] + var["taille_case"] // 6),
        (x * var["taille_case"] + var["taille_case"] // 8,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 4),
        (x * var["taille_case"] + var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4 + var["taille_case"] // 4),
        (x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 4),
        (x * var["taille_case"] + 3 * var["taille_case"] // 4,
        y * var["taille_case"] - var["taille_case"] // 4 + var["taille_case"] // 4),    
        (x * var["taille_case"] + var["taille_case"] - var["taille_case"] // 8,
        y * var["taille_case"] - var["taille_case"] // 2 + var["taille_case"] // 4),
        (x * var["taille_case"] + var["taille_case"] - var["taille_case"] // 8,
        y * var["taille_case"] + var["taille_case"] // 6)
        ],
        couleur="yellow",
        remplissage="yellow",
    )
    polygone(
        [(x * var["taille_case"] + var["taille_case"] // 2,
        y * var["taille_case"] + var["taille_case"]),
        (x * var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6),
        (x * var["taille_case"] + var["taille_case"] // 6,
        y * var["taille_case"] + 1),
        (x * var["taille_case"] + 5 * var["taille_case"] // 6,
        y * var["taille_case"] + 1),
        (x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6),
        ],
        couleur = "lightblue",
        remplissage = "lightblue"
    )
    for i in range(4):
        ligne(
            x * var["taille_case"] + i * var["taille_case"] // 3,
            y * var["taille_case"] + var["taille_case"] // 6,
            x * var["taille_case"] + var["taille_case"] // 2,
            y * var["taille_case"] + var["taille_case"],
            epaisseur=var["taille_case"] // 25
        )
    for i in range(3):
        ligne(
            x * var["taille_case"] + var["taille_case"] // 6 + i * var["taille_case"] // 3,
            y * var["taille_case"],
            x * var["taille_case"] + var["taille_case"] // 3 + i * var["taille_case"] // 3,
            y * var["taille_case"] + var["taille_case"] // 6,
            epaisseur=var["taille_case"] // 25
        )
        ligne(
            x * var["taille_case"] + var["taille_case"] // 6 + i * var["taille_case"] // 3,
            y * var["taille_case"],
            x * var["taille_case"] + i * var["taille_case"] // 3,
            y * var["taille_case"] + var["taille_case"] // 6,
            epaisseur=var["taille_case"] // 25
        )
    ligne(
        x * var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6 ,
        x * var["taille_case"] + var["taille_case"],
        y * var["taille_case"] + var["taille_case"] // 6,
        epaisseur=var["taille_case"] // 25
    )

def fond():
    rectangle(
        0,
        0,
        var["dimension_fenetre"],
        var["dimension_fenetre"] + 100,
        couleur="black",
        remplissage="black",
    )

def fond_victorieux():
    rectangle(
        0,
        0,
        var["dimension_fenetre"],
        var["dimension_fenetre"] + 100,
        couleur="cyan",
        remplissage="cyan",
    )

def fond_score_temps_diams(score, tempsrestant, nbdiamandrestant):
    rectangle(
        0,
        var["dimension_fenetre"],
        var["dimension_fenetre"],
        var["dimension_fenetre"] + 100,
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
        "Nombre de diamand manquant:{}".format(nbdiamandrestant),
        couleur="white",
        ancrage="center",
        taille=15,
        police="Impact",
    )

def personnage_victorieux():
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