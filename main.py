import sys
from time import sleep

import fonction
import pathfinding
from upemtk import *
from variable import var


def main():
    score = '00000000'
    debug = -1
    mode = 0
    nbdiamand = 0
    temps = 0
    carte = fonction.creer_map("map_test.txt")
    fonction.initialiser_partie(carte)
    print(carte)
    print((var["pos_x"], var["pos_y"]), (var["pos_sortie_x"], var["pos_sortie_y"]))

    if len(sys.argv) > 1 and sys.argv[1] == "-p":
        path = pathfinding.astar(carte, (var["pos_x"], var["pos_y"]), (var["pos_sortie_x"], var["pos_sortie_y"]))
    while True:
        efface_tout()
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
        fonction.pousser_pierre(carte, ev)
        if type_ev == "ClicGauche":
            coords = [clic_x(ev), clic_y(ev)]
            mode = fonction.quitte_or_retry(coords, coordretry, coordquitte)
        
        if len(sys.argv) > 1 and sys.argv[1] == "-p":
            next_pos = path.pop(0)
            direction = ""
            if next_pos[0] > var["pos_x"]:
                direction = "Right"
            elif next_pos[0] < var["pos_x"]:
                direction = "Left"
            elif next_pos[1] > var["pos_y"]:
                direction = "Down"
            elif next_pos[1] < var["pos_y"]:
                direction = "Up"
            nbdiamand = fonction.deplacer_perso(carte, nbdiamand, direction, True)       
            sleep(0.2)
        else:
            if type_ev == "Touche" and touche(ev) == "d":
                debug *= -1
            if debug == 1:
                # if not temps % 15:
                nbdiamand = fonction.debug(carte, nbdiamand)
                # temps += 1
            else:
                nbdiamand = fonction.deplacer_perso(carte, nbdiamand, ev)
        
        fonction.tomber_de_pierre(carte)
        fonction.affichage(carte)
        fonction.fond_score(score)
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
