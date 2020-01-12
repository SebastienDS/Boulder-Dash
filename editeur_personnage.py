import upemtk
import fonction
import esthetique
from variable import var
from pickle import dump
from tkinter.colorchooser import askcolor


def cree_torche(historique, points):
    """
	ajoute la torche dans l'historique
	
	:param dict historique: contient les formes du personnage deja cree
	:param list points: contient le point placant la torche
	"""
    historique[len(historique) + 1] = [
        "torche",
        "T",
        points[0][0],
        points[0][1],
        var["dimension_fenetre"],
    ]


def cree_cle(historique, points):
    """
	ajoute la cle dans l'historique
	
	:param dict historique: contient les formes du personnage deja cree
	:param list points: contient le point placant la cle
	"""
    historique[len(historique) + 1] = [
        "cle",
        "Y",
        points[0][0],
        points[0][1],
        var["dimension_fenetre"],
    ]


def cree_cercle(historique, points):
    """
	ajoute le cercle dans l'historique
	
	:param dict historique: contient les formes du personnage deja cree
	:param list points: contient les points permettant de realisé un cercle 
		(centre puis rayon)
	"""
    pos1, pos2 = points
    r = round(((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5, 3)

    historique[len(historique) + 1] = [
        choix_nom_forme(historique),
        "C",
        *pos1,
        r,
        *choix_couleur(historique),
    ]


def cree_rect(historique, points):
    """
	ajoute le rectangle dans l'historique

	:param dict historique: contient les formes du personnage deja cree
	:param list points: contient les points permettant de realisé un rect
		(point_haut_gauche puis point_bas_droite)
	"""
    pos1, pos2 = points

    historique[len(historique) + 1] = [
        choix_nom_forme(historique),
        "R",
        *pos1,
        *pos2,
        *choix_couleur(historique),
    ]


def cree_polygone(historique, points):
    """
	ajoute le polygone dans l'historique
	
	:param dict historique: contient les formes du personnage deja cree
	:param list points: contient les points permettant de realisé un polygone
		(nombre de points illimité)
	"""
    historique[len(historique) + 1] = [
        choix_nom_forme(historique),
        "P",
        points.copy(),
        *choix_couleur(historique),
    ]


def affiche_croix(x, y, taille):
    """
	affiche une croix pour le curseur et pour les visualiser les points 
	lors de la creation d'une forme
	
	:param int x: position x de la croix
	:param int y: position y de la croix
	:param int taille: taille de la croix
	"""
    upemtk.ligne(x - taille, y, x + taille, y, couleur="red")
    upemtk.ligne(x, y - taille, x, y + taille, couleur="red")


def choix_couleur_remplissage_epaisseur(historique):
    """
	recupere les valeurs de la derniere forme afin de les mettre 
	par defaut dans l'input
	
	:param dict historique: contient les formes du personnage deja cree
	:return: (couleur, remplissage, epaisseur)

	>>> choix_couleur_remplissage_epaisseur({})
	('white', '', '1')
	>>> historique = {1: ['cercle', 'C', 100, 200, 123.45, '#ff0080', '#ff0080', 1]}
	>>> choix_couleur_remplissage_epaisseur(historique)
	('#ff0080', '#ff0080', '1')
	"""
    if (
        not len(historique)
        or not historique[len(historique)]
        or historique[len(historique)][1] in {"T", "Y"}
    ):
        return "white", "", "1"
    return (
        historique[len(historique)][-3],
        historique[len(historique)][-2],
        str(historique[len(historique)][-1]),
    )


def choix_couleur(historique):
    """
	demande la couleur, le remplissage ainsi que lepaisseur
	
	:param dict historique: contient les formes du personnage deja cree
	"""
    couleur_, remplissage_, epaisseur_ = choix_couleur_remplissage_epaisseur(historique)

    couleur = fonction.my_input("Couleur:", "str", couleur_)
    if couleur == "+":
        couleur = askcolor()[1]

    remplissage = fonction.my_input("Remplissage:", "str", remplissage_)
    if remplissage == "+":
        remplissage = askcolor()[1]

    epaisseur = fonction.my_input("Epaisseur", "int", epaisseur_)

    return couleur, remplissage, epaisseur


def choix_nom_forme(historique):
    """
	demande le nom de la forme

	:param dict historique: contient les formes du personnage deja cree
	:return: str
	"""
    return fonction.my_input("Nom de la forme:", "str", str(len(historique) + 1))


def redimensionner_forme(historique, multiplicateur):
    """
	redimensionne les formes afin de pouvoir les ouvrir dans de differente taille
	
	
	:param dict historique: contient les formes du personnage deja cree
	:param int multiplicateur: permet d'agrandir ou de diminuer la taille des formes
	
	>>> historique = {
	...     1: ['cercle', 'C', 100, 200, 123.45, '#ff0080', '#ff0080', 1],
	...     2: ['2', 'R', 300, 350, 400, 500, 'red', '', 1],
	... }
	>>> redimensionner_forme(historique, 2)
	>>> historique
	{1: ['cercle', 'C', 200, 400, 246.9, '#ff0080', '#ff0080', 1], \
2: ['2', 'R', 600, 700, 800, 1000, 'red', '', 1]}
	>>> redimensionner_forme(historique, 1/2)
	>>> historique
	{1: ['cercle', 'C', 100.0, 200.0, 123.45, '#ff0080', '#ff0080', 1], \
2: ['2', 'R', 300.0, 350.0, 400.0, 500.0, 'red', '', 1]}
	>>> redimensionner_forme(historique, 0.1)
	>>> historique
	{1: ['cercle', 'C', 10.0, 20.0, 12.345, '#ff0080', '#ff0080', 1], \
2: ['2', 'R', 30.0, 35.0, 40.0, 50.0, 'red', '', 1]}
	"""
    for forme in historique:
        if historique[forme][1] in {"C", "R"}:
            for i in range(2, 2 + len(historique[forme][2:-3])):
                historique[forme][i] *= multiplicateur

        elif historique[forme][1] == "P":
            for i in range(len(historique[forme][2])):
                historique[forme][2][i] = (
                    historique[forme][2][i][0] * multiplicateur,
                    historique[forme][2][i][1] * multiplicateur,
                )
        elif historique[forme][1] in {"T", "Y"}:
            historique[forme][2] *= multiplicateur
            historique[forme][3] *= multiplicateur


def affiche_historique(historique, pos=None):
    """
	affiche l'historique dans le terminal

	:param dict historique: contient les formes du personnage deja cree
	:param int pos: cle de la forme souhaitant etre affiché

	>>> historique = {
	...     1: ['cercle', 'C', 100, 200, 123.45, '#ff0080', '#ff0080', 1],
	...     2: ['2', 'R', 300, 350, 400, 500, 'red', '', 1],
	... }
	>>> affiche_historique(historique)
	<BLANKLINE>
	<BLANKLINE>
	['cercle', 'C', 100, 200, 123.45, '#ff0080', '#ff0080', 1]
	['2', 'R', 300, 350, 400, 500, 'red', '', 1]
	>>> affiche_historique(historique, 2)
	['2', 'R', 300, 350, 400, 500, 'red', '', 1]
	>>> affiche_historique(historique, 1)
	['cercle', 'C', 100, 200, 123.45, '#ff0080', '#ff0080', 1]
	>>> affiche_historique({})
	<BLANKLINE>
	<BLANKLINE>
	"""
    if not pos:
        print("\n")
        for elem in historique.values():
            print(elem)
    else:
        print(historique[pos])


def verif_1_cle_1_torche(historique):
    """
	verifie <ue le personnage contient bien 1 cle et 1 torche

	:param dict historique: contient les formes du personnage deja cree
	:return: None si la condition est verifié sinon le message d'erreur a afficher

	>>> historique = {
	...     1: ['cercle', 'C', 100, 200, 120, '#ff0080', '#ff0080', 1],
	...     2: ['2', 'R', 300, 350, 400, 500, 'red', '', 1],
	... }
	>>> retour = verif_1_cle_1_torche(historique)
	>>> list(map(str.strip, retour.split("\\n")))
	['nombre de cle', 'et de', 'torche incorrect']
	>>> historique = {
	...     1: ['cle', 'Y', 200, 200, 600],
	...     2: ['2', 'R', 300, 350, 400, 500, 'red', '', 1],
	... }
	>>> retour = verif_1_cle_1_torche(historique)
	>>> list(map(str.strip, retour.split("\\n")))
	['nombre de torche', 'incorrect']
	>>> historique = {
	...     1: ['torche', 'T', 300, 200, 600],
	...     2: ['2', 'R', 300, 350, 400, 500, 'red', '', 1],
	... }
	>>> retour = verif_1_cle_1_torche(historique)
	>>> list(map(str.strip, retour.split("\\n")))
	['nombre de cle', 'incorrect']
	>>> historique = {
	...     1: ['torche', 'T', 300, 200, 600],
	...     2: ['cle', 'Y', 200, 200, 600],
	... }
	>>> print(verif_1_cle_1_torche(historique))
	None
	"""
    cle = 0
    torche = 0
    for elem in historique.values():
        if elem:
            if elem[1] == "T":
                torche += 1
            elif elem[1] == "Y":
                cle += 1

    if cle != 1 and torche != 1:
        return "   nombre de cle\n          et de\n    torche incorrect"
    elif cle != 1:
        return "nombre de cle\n    incorrect"
    elif torche != 1:
        return "nombre de torche\n       incorrect"


def sauvegarde_historique(historique):
    """
	sauvegarde l'historique dans un fichier

	:param dict historique: contient les formes du personnage deja cree
	"""
    for i in range(1, len(historique) + 1):
        if not historique[i]:
            del historique[i]

    redimensionner_forme(historique, 1 / var["dimension_fenetre"])
    with open(
        "personnage/{}".format(fonction.my_input("Nom du personnage: ", "str")), "wb",
    ) as f:
        dump(historique, f)


forme_possible = {  # cree_forme / dessine_forme / nombre_points_mini / nombre_points_maxi
    "C": (cree_cercle, upemtk.cercle, 2, 2),
    "R": (cree_rect, upemtk.rectangle, 2, 2),
    "P": (cree_polygone, upemtk.polygone, 1, 999),
    "T": (cree_torche, esthetique.torche, 1, 1),
    "Y": (cree_cle, esthetique.cle, 1, 1),
}


def main():
    historique = {}

    zone_edit = (
        var["dimension_fenetre"],
        var["dimension_fenetre"],
    )

    coordonnee_souris_x = coordonnee_souris_y = 0
    liste_clic = []
    forme_active = ""

    boutons = {
        "C": ("cercle", 50, 655, "green", "black", 20, 1, 2, "Impact"),
        "R": ("rectangle", 75, 610, "green", "black", 20, 1, 2, "Impact"),
        "P": ("polygone", 152, 655, "green", "black", 20, 1, 2, "Impact"),
        "Y": ("cle", 160, 610, "#ff0080", "black", 20, 1, 2, "Impact"),
        "T": ("torche", 257, 655, "#ff0080", "black", 20, 1, 2, "Impact"),
        "suppr (backspace)": (
            "supprimer (dernier)",
            302,
            610,
            "red",
            "black",
            20,
            1,
            2,
            "Impact",
        ),
        "suppr (enter)": (
            "supprimer (nom)",
            402,
            655,
            "red",
            "black",
            20,
            1,
            2,
            "Impact",
        ),
        "sauvegarder": ("sauvegarder", 500, 610, "black", "black", 20, 1, 2, "Impact"),
        "quitter": ("quitter", 548, 655, "black", "black", 20, 1, 2, "Impact"),
    }

    while True:
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)

        if type_ev == "Quitte":
            return -1

        if type_ev == "Touche":
            t = upemtk.touche(ev)
            t_upper = t.upper()

            if (
                t_upper in forme_possible
                and not forme_active
                and t_upper not in {"T", "Y"}
            ):
                forme_active = t_upper
            elif (
                t_upper in {"T", "Y"}
                and not forme_active
                and not any(map(lambda x: t_upper in x, historique.values()))
            ):
                forme_active = t_upper

            elif t == "BackSpace":
                if len(historique):
                    del historique[len(historique)]
                    affiche_historique(historique)

            elif t == "Return":
                nom_forme_a_suppr = fonction.my_input(
                    "nom de la forme\n    a supprimer", "str"
                )
                for cle, valeur in historique.items():
                    if valeur and valeur[0] == nom_forme_a_suppr:
                        historique[cle] = []
                        affiche_historique(historique)
                        break

            elif t == "Escape":
                return 0

            elif t_upper == "S":
                res = verif_1_cle_1_torche(historique)
                if res:
                    fonction.my_input(res, "str")
                else:
                    sauvegarde_historique(historique)
                    return 0

        elif type_ev == "Deplacement":
            coordonnee_souris_x = upemtk.clic_x(ev)
            coordonnee_souris_y = upemtk.clic_y(ev)

        if type_ev == "ClicGauche":
            x, y = upemtk.clic_x(ev), upemtk.clic_y(ev)
            if (
                forme_active != ""
                and (len(liste_clic) < forme_possible[forme_active][3])
                and (x <= zone_edit[0] and y <= zone_edit[1])
            ):
                liste_clic.append((x, y))

        elif (
            type_ev == "ClicDroit"
            and forme_active != ""
            and len(liste_clic) >= forme_possible[forme_active][2]
        ):
            forme_possible[forme_active][0](
                historique, liste_clic
            )  # cree la forme dans l'historique a partir des clics
            forme_active = ""
            del liste_clic[:]
            affiche_historique(historique, len(historique))

        upemtk.efface_tout()
        upemtk.rectangle(
            0, 0, zone_edit[0], zone_edit[1], remplissage="black",
        )

        # affiche les formes dans l'historique
        for elem in historique.values():
            if elem:
                forme_possible[elem[1]][1](*elem[2:])

        # affiche une croix sur les clics afin de conserver visuellement leur position
        for elem in liste_clic:
            affiche_croix(*elem, 5)

        # efface les traits sortant de la zone d'edit
        upemtk.rectangle(
            zone_edit[0],
            0,
            var["dimension_fenetre"],
            var["dimension_fenetre"] - var["dimension_fenetre"] // 6,
            couleur="white",
            remplissage="white",
        )
        upemtk.rectangle(
            0,
            zone_edit[1],
            var["dimension_fenetre"],
            var["dimension_fenetre"] + var["bandeau"],
            couleur="white",
            remplissage="white",
        )

        for cle, elem in boutons.items():

            pos = fonction.encadrement(*boutons[cle])
            if type_ev == "ClicGauche" and fonction.test_clic(
                (coordonnee_souris_x, coordonnee_souris_y), pos
            ):
                if cle in forme_possible and cle not in {"T", "Y"}:
                    del liste_clic[:]
                    forme_active = cle
                elif cle in forme_possible and not any(
                    map(lambda x: cle in x, historique.values())
                ):
                    del liste_clic[:]
                    forme_active = cle

                elif cle == "sauvegarder":
                    res = verif_1_cle_1_torche(historique)
                    if res:
                        fonction.my_input(res, "str")
                    else:
                        sauvegarde_historique(historique)
                        return 0
                elif cle == "quitter":
                    return 0

                elif cle == "suppr (backspace)":
                    if len(historique):
                        del historique[len(historique)]
                    affiche_historique(historique)
                elif cle == "suppr (enter)":
                    nom_forme_a_suppr = fonction.my_input(
                        "nom de la forme\n    a supprimer", "str"
                    )
                    for cle, valeur in historique.items():
                        if valeur and valeur[0] == nom_forme_a_suppr:
                            historique[cle] = []
                            affiche_historique(historique)
                            break

        # affiche la croix sur le curseur pour plus de precision du clic
        affiche_croix(coordonnee_souris_x, coordonnee_souris_y, 20)
        upemtk.mise_a_jour()

        # fait de la place dans les evenements car le surplus d'evenemement est très présent et casse tout
        # la lignes peut etre supprimé afin de bien apprécier le spectacle puis venir la remettre dans les secondes qui suivent ;)
        del upemtk.__canevas.eventQueue[:-5]

    return 0


if __name__ == "__main__":
    print("Programme principal: main.py")
