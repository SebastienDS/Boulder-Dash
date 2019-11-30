import upemtk
import fonction
import esthetique
from variable import var



def cree_cercle(historique, points):
    pos1, pos2 = points
    r = round(((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5, 3)

    historique[len(historique) + 1] = [choix_nom_forme(historique), "C", *pos1, r, *choix_couleur(historique)]


def cree_rect(historique, points):
    pos1, pos2 = points 

    historique[len(historique) + 1] = [choix_nom_forme(historique), "R", *pos1, *pos2, *choix_couleur(historique)]


def cree_polygone(historique, points):
    historique[len(historique) + 1] = [choix_nom_forme(historique), "P", points.copy(), *choix_couleur(historique)]


def affiche_croix(x, y, taille):
    upemtk.ligne(x - taille, y, x + taille, y, couleur="red")
    upemtk.ligne(x, y - taille, x, y + taille, couleur="red")


def choix_couleur_remplissage_epaisseur(historique):
    """recupere les valeurs de la derniere forme afin de les mettre par defaut dans l'input"""
    if not len(historique): 
        return "white", "", "1"
    return historique[len(historique)][-3], historique[len(historique)][-2], str(historique[len(historique)][-1])


def choix_couleur(historique):
    couleur_, remplissage_, epaisseur_ = choix_couleur_remplissage_epaisseur(historique)

    couleur = fonction.my_input("Couleur:", "str", couleur_)
    remplissage = fonction.my_input("Remplissage:", "str", remplissage_)
    epaisseur = fonction.my_input("Epaisseur", "int", epaisseur_)
    return couleur, remplissage, epaisseur


def choix_nom_forme(historique):
    return fonction.my_input("Nom de la forme:", "str", str(len(historique) + 1))



def main():
    forme_possible = {    #cree_forme / dessine_forme / nombre_points_mini
        "C": (cree_cercle, upemtk.cercle, 2),
        "R": (cree_rect, upemtk.rectangle, 2),
        "P": (cree_polygone, upemtk.polygone, 1),
    }
    historique = {}

    zone_edit = (
        var["dimension_fenetre"] - var["dimension_fenetre"] // 6, 
        var["dimension_fenetre"] - var["dimension_fenetre"] // 6
    )

    coordonnee_souris_x = coordonnee_souris_y = 0
    liste_clic = []
    forme_active = ""

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
            if forme_active != "" and (len(liste_clic) < 2 or forme_active == "P") and (x <= zone_edit[0] and y <= zone_edit[1]):
                liste_clic.append((x, y))     

        elif type_ev == "ClicDroit" and forme_active != "" and len(liste_clic) >= forme_possible[forme_active][2]:
            forme_possible[forme_active][0](historique, liste_clic)     #cree la forme dans l'historique a partir des clics
            forme_active = ""   
            del liste_clic[:]  

            print(historique[len(historique)])         


        upemtk.efface_tout()
        upemtk.rectangle(
            0, 
            0,
            zone_edit[0],
            zone_edit[1], 
            remplissage="black",
        )
        
        #affiche les formes dans l'historique
        for elem in historique.values():
            forme_possible[elem[1]][1](*elem[2:])

        #affiche une croix sur les clics afin de conserver visuellement leur position
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

        #affiche la croix sur le curseur pour plus de precision du clic
        affiche_croix(coordonnee_souris_x, coordonnee_souris_y, 20)
        upemtk.mise_a_jour()
        
    upemtk.attente_clic()
    return 0


if __name__ == '__main__':
    main()

