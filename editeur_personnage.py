import upemtk
import fonction
import esthetique
from variable import var



def dessine_cercle(historique):
    x1, y1, _ = upemtk.attente_clic()
    upemtk.point(x1, y1, "red", 3, tag="point")
    x2, y2, _ = upemtk.attente_clic()
    r = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 3)
    couleur = "white"
    remplissage = ""
    epaisseur = 1

    upemtk.cercle(x1, y1, r, remplissage=couleur)
    upemtk.efface("point")
    historique[len(historique) + 1] = ["C", x1, y1, r, couleur, remplissage, epaisseur]


def dessine_rect(historique):
    x1, y1, t = upemtk.attente_clic()
    upemtk.point(x1, y1, "red", 3, tag="point") 
    x2, y2, _ = upemtk.attente_clic()
    couleur = "white"
    remplissage = ""
    epaisseur = 1

    upemtk.rectangle(x1, y1, x2, y2, remplissage="white")
    upemtk.efface("point")
    historique[len(historique) + 1] = ["R", x1, y1, x2, y2, couleur, remplissage, epaisseur]


def dessine_polygone():
    pass


def main():
    forme_possible = {
        "C": dessine_cercle,
        "R": dessine_rect,
        "P": dessine_polygone,
    }
    historique = {}

    zone_edit = (
        var["dimension_fenetre"] - var["dimension_fenetre"] // 6, 
        var["dimension_fenetre"] - var["dimension_fenetre"] // 6
    )
    taille_fen = (var["dimension_fenetre"], var["dimension_fenetre"] + var["bandeau"])
    upemtk.cree_fenetre(taille_fen[0], taille_fen[1])

    upemtk.rectangle(
        0, 
        0,
        zone_edit[0],
        zone_edit[1], 
        remplissage="black",
    )

    while True:
        print(historique)
        upemtk.mise_a_jour()
        ev = upemtk.attente_clic_ou_touche()

        if ev[2] == "ClicGauche":
            pass

        elif ev[2] == "Touche":
            if ev[1].upper() in forme_possible:
                forme_possible[ev[1].upper()](historique)

            elif ev[1] == "space":
                break
                upemtk.ferme_fenetre()


    upemtk.attente_clic()
    upemtk.ferme_fenetre()


if __name__ == '__main__':
    main()
