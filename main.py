import fonction
from upemtk import *
from variable import var


def main():
    score = '00000000'
    debug = -1
    mode = 0
    nbdiamand = 0
    temps = 0
    carte = fonction.creer_map("map1.txt")
    fonction.initialiser_partie(carte)
    while True:
        efface_tout()
        fonction.tomber_de_pierre(carte)
        fonction.affichage(carte)
        fonction.fond_score(score)
        coordretry = fonction.encadrement(
            "Retry",
            var["dimension_fenetre"] // 15,
            var["dimension_fenetre"] + 60,
            "white",
            "white",
            12,
            5,
            5,
        )
        coordquitte = fonction.encadrement(
            "Exit_Game",
            4 * var["dimension_fenetre"] // 5,
            var["dimension_fenetre"] + 60,
            "white",
            "white",
            12,
            5,
            5,
        )
        ev = donne_evenement()
        type_ev = type_evenement(ev)
        if type_ev == "ClicGauche":
            coords = [clic_x(ev), clic_y(ev)]
            mode = fonction.quitte_or_retry(coords, coordretry, coordquitte)
        if type_ev == "Touche" and touche(ev) == "d":
            debug *= -1
        if debug == 1:
            # if not temps % 15:
            nbdiamand = fonction.debug(carte, nbdiamand)
            # temps += 1
        else:
            nbdiamand = fonction.deplacer_perso(carte, nbdiamand, ev)
        mise_a_jour()
        if mode != 0:
            return mode
        if fonction.win() or fonction.loose(carte):
            while mode == 0:
                coordretry = fonction.encadrement(
                    "Retry", var["dimension_fenetre"] // 7, 40, "red", "red", 12, 5, 5
                )
                coordquitte = fonction.encadrement(
                    "Exit_Game",
                    4 * var["dimension_fenetre"] // 5,
                    40,
                    "red",
                    "red",
                    12,
                    5,
                    5,
                )
                a = attente_clic()
                mode = fonction.quitte_or_retry(a, coordretry, coordquitte)
            return mode

if __name__ == "__main__":
    print(
        "Made by Uniiiiiifffffay corporation with the collaboration of Natsouuuuuu corporation!!! All right reserved!"
    )
    cree_fenetre(var["dimension_fenetre"], var["dimension_fenetre"] + 100)
    while True:
        if main() == 1:
            break

    ferme_fenetre()
