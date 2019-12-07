import upemtk
import fonction
import esthetique
from variable import var
import tkinter.colorchooser


def cree_cercle(historique, points):
    """ajoute le cercle dans l'historique"""
    pos1, pos2 = points
    r = round(((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5, 3)

    historique[len(historique) + 1] = [
        choix_nom_forme(historique),
        "C",
        *pos1,
        r,
        var["couleur"], var["remplissage"], var["epaisseur"],
    ]


def cree_rect(historique, points):
    """ajoute le rectangle dans l'historique"""
    pos1, pos2 = points

    historique[len(historique) + 1] = [
        choix_nom_forme(historique),
        "R",
        *pos1,
        *pos2,
        var["couleur"], var["remplissage"], var["epaisseur"],
    ]


def cree_polygone(historique, points):
    """ajoute le polygone dans l'historique"""
    historique[len(historique) + 1] = [
        choix_nom_forme(historique),
        "P",
        points.copy(),
        var["couleur"], var["remplissage"], var["epaisseur"],
    ]


def affiche_croix(x, y, taille):
    upemtk.ligne(x - taille, y, x + taille, y, couleur="red")
    upemtk.ligne(x, y - taille, x, y + taille, couleur="red")


# def choix_couleur_remplissage_epaisseur(historique):
#     """recupere les valeurs de la derniere forme afin de les mettre par defaut dans l'input"""
#     if not len(historique):
#         return "white", "", "1"
#     return (
#         historique[len(historique)][-3],
#         historique[len(historique)][-2],
#         str(historique[len(historique)][-1]),
#     )


# def choix_couleur(historique):
#     couleur_, remplissage_, epaisseur_ = choix_couleur_remplissage_epaisseur(historique)

#     # couleur = fonction.my_input("Couleur:", "str", couleur_)
#     couleur = tkinter.colorchooser.askcolor()[1]
#     # remplissage = fonction.my_input("Remplissage:", "str", remplissage_)
#     epaisseur = fonction.my_input("Epaisseur", "int", epaisseur_)
#     remplissage = tkinter.colorchooser.askcolor()[1]
#     return couleur, remplissage, epaisseur


def choix_nom_forme(historique):
    return fonction.my_input("Nom de la forme:", "str", str(len(historique) + 1))


def tool_bar(zone_edit):
    c = ["C", zone_edit[0] + 50, 50, 47, "white", "red"]
    r = ["R", zone_edit[0] + 5, 105, zone_edit[1] + 95, 200, "white", "red"]
    p = ["P", [(zone_edit[0] + 5, 250), (zone_edit[0] + 50, 205), (zone_edit[0] + 95, 250), (zone_edit[0] + 95, 325), (zone_edit[0] + 5, 325)], "white", "red"]
    return [c, r, p]


def changer_c_r_e(num):
    if num == 0:
        var["couleur"] = tkinter.colorchooser.askcolor()[1]
    elif num == 1:
        var["remplissage"] = tkinter.colorchooser.askcolor()[1]
    elif num == 2:
        var["epaisseur"] = fonction.my_input("Epaisseur", "int", str(var["epaisseur"]))


def main():
    forme_possible = {  # cree_forme / dessine_forme / nombre_points_mini
        "C": (cree_cercle, upemtk.cercle, 2),
        "R": (cree_rect, upemtk.rectangle, 2),
        "P": (cree_polygone, upemtk.polygone, 1),
    }
    historique = {}

    zone_edit = (
        var["dimension_fenetre"] - var["dimension_fenetre"] // 6,
        var["dimension_fenetre"] - var["dimension_fenetre"] // 6,
    )

    coordonnee_souris_x = coordonnee_souris_y = 0
    liste_clic = []
    c_r_e_encadrement = []
    forme_active = ""
    var["couleur"] = "white"
    var["remplissage"] = ""
    var["epaisseur"] = 1

    while True:
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)
        if type_ev == "Touche":
            t = upemtk.touche(ev)
            if t.upper() in forme_possible and not forme_active:
                forme_active = t.upper()

            elif t == "space":
                break

        elif type_ev == "Quitte":
            return -1

        elif type_ev == "Deplacement":
            coordonnee_souris_x = upemtk.clic_x(ev)
            coordonnee_souris_y = upemtk.clic_y(ev)

        elif type_ev == "ClicGauche":
            x, y = upemtk.clic_x(ev), upemtk.clic_y(ev)
            if (
                forme_active != ""
                and (len(liste_clic) < 2 or forme_active == "P")
                and (x <= zone_edit[0] and y <= zone_edit[1])
            ):
                liste_clic.append((x, y))
            
            for i, elem in enumerate(c_r_e_encadrement):
                if elem[0] < x < elem[2] and elem[1] < y < elem[3]:
                    changer_c_r_e(i)


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

            print(historique[len(historique)])

        upemtk.efface_tout()
        upemtk.rectangle(
            0, 0, zone_edit[0], zone_edit[1], remplissage="black",
        )

        # affiche les formes dans l'historique
        for elem in historique.values():
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

        for elem in tool_bar(zone_edit):
            forme_possible[elem[0]][1](*elem[1:])

        c_r_e_encadrement = [
            fonction.encadrement(
                "couleur", 75, zone_edit[1] + 50, "black", var["couleur"], 30, 4, 1, "Impact"
            ),
            fonction.encadrement(
                "remplissage", 275, zone_edit[1] + 50, "black", var["remplissage"], 30, 4, 1, "Impact"
            ),
            fonction.encadrement(
                "epaisseur", 500, zone_edit[1] + 50, "black", "black", 30, 4, 1, "Impact"
            ) 
        ]

        # affiche la croix sur le curseur pour plus de precision du clic
        affiche_croix(coordonnee_souris_x, coordonnee_souris_y, 20)
        upemtk.mise_a_jour()

    upemtk.attente_clic()
    return 0


if __name__ == "__main__":
    main()
