import upemtk
import fonction
import esthetique
from variable import var



###  Mettre donne_evenement afin d'avoir le deplacement de la souris et y placer une croix sur le curseur pour plus de precision


def cree_cercle(historique, points):
    pos1, pos2 = points
    r = round(((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5, 3)

    historique[len(historique) + 1] = ["C", *pos1, r, *choix_couleur(historique)]


def cree_rect(historique, points):
    pos1, pos2 = points 

    historique[len(historique) + 1] = ["R", *pos1, *pos2, *choix_couleur(historique)]


def cree_polygone(historique, points):
    historique[len(historique) + 1] = ["P", points.copy(), *choix_couleur(historique)]


def affiche_croix(x, y, taille):
    upemtk.ligne(x - taille, y, x + taille, y, couleur="red")
    upemtk.ligne(x, y - taille, x, y + taille, couleur="red")


def choix_couleur_remplissage_epaisseur(historique):
    if not len(historique): 
        return "white", "", "1"
    return historique[len(historique)][-3], historique[len(historique)][-2], str(historique[len(historique)][-1])


def choix_couleur(historique):
    couleur_, remplissage_, epaisseur_ = choix_couleur_remplissage_epaisseur(historique)

    couleur = fonction.my_input("Couleur:", "str", couleur_)
    remplissage = fonction.my_input("Remplissage:", "str", remplissage_)
    epaisseur = fonction.my_input("Epaisseur", "int", epaisseur_)
    return couleur, remplissage, epaisseur


def main():
    forme_possible = {    
        "C": (cree_cercle, upemtk.cercle),
        "R": (cree_rect, upemtk.rectangle),
        "P": (cree_polygone, upemtk.polygone),
    }
    historique = {}

    zone_edit = (
        var["dimension_fenetre"] - var["dimension_fenetre"] // 6, 
        var["dimension_fenetre"] - var["dimension_fenetre"] // 6
    )

    coordonnee_souris_x = coordonnee_souris_y = 0
    liste_clic = []
    forme_active = ""

    taille_fen = (var["dimension_fenetre"], var["dimension_fenetre"] + var["bandeau"])
    upemtk.cree_fenetre(taille_fen[0], taille_fen[1])

    while True:
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)
        if type_ev == "Touche":
            t = upemtk.touche(ev)
            if t.upper() in forme_possible:
                forme_active = t.upper()

            elif t == "space":
                break 
                upemtk.ferme_fenetre()

        elif type_ev == "Quitte":
            break 
            upemtk.ferme_fenetre()

        elif type_ev == "Deplacement":
            coordonnee_souris_x = upemtk.clic_x(ev)
            coordonnee_souris_y = upemtk.clic_y(ev)

        elif type_ev == "ClicGauche":
            if forme_active != "" and (len(liste_clic) < 2 or forme_active == "P"):
                liste_clic.append((upemtk.clic_x(ev), upemtk.clic_y(ev)))

        elif type_ev == "ClicDroit" and forme_active != "":
            forme_possible[forme_active][0](historique, liste_clic)
            forme_active = ""
            del liste_clic[:]

        upemtk.efface_tout()
        upemtk.rectangle(
            0, 
            0,
            zone_edit[0],
            zone_edit[1], 
            remplissage="black",
        )
        
        for elem in historique.values():
            forme_possible[elem[0]][1](*elem[1:])

        for elem in liste_clic:
            affiche_croix(*elem, 5)

        #efface les traits sortant de la zone d'edit
        upemtk.rectangle(
            zone_edit[0],
            0,
            var["dimension_fenetre"],
            var["dimension_fenetre"] - var["dimension_fenetre"] // 6,
            couleur="white",
            remplissage="white"
        )
        upemtk.rectangle(
            0,
            zone_edit[1],
            var["dimension_fenetre"],
            var["dimension_fenetre"] + var["bandeau"],
            couleur="white",
            remplissage="white"
        )

        affiche_croix(coordonnee_souris_x, coordonnee_souris_y, 20)
        upemtk.mise_a_jour()
        
    upemtk.attente_clic()
    upemtk.ferme_fenetre()


if __name__ == '__main__':
    main()

