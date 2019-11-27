import editeur_map
import editeur_personnage
import fonction
import esthetique
from upemtk import *
from variable import var
from time import time

def menu(d, temps):
    esthetique.fond("black")
    fonction.encadrement('BOULDER DASH', 
        var["dimension_fenetre"] // 2, 
        50, "White", "black", 
        50, 1, 1) 
    MAP = fonction.encadrement('SELECTION MAP',
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 3,
        "White", "white",
        36, 1, 5) 
    EDIT_MAP = fonction.encadrement('EDITEUR DE MAP',
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 2,
        "White", "white", 
        36, 1, 5) 
    EDIT_PERSO = fonction.encadrement('EDITEUR DE PERSONNAGE', 
        var["dimension_fenetre"] // 2, 
        2 * var["dimension_fenetre"] // 3, 
        "White", "white", 
        36, 1, 5) 
    ev = donne_evenement()
    type_ev = type_evenement(ev)
    if type_ev == "ClicGauche":
        coords = [clic_x(ev), clic_y(ev)]
        if fonction.test_MAP(coords, MAP):
            return 1, temps
        if fonction.test_EDIT_MAP(coords, EDIT_MAP):
            return 2, temps
        if fonction.test_EDIT_PERSO(coords, EDIT_PERSO):
            return 3, temps
    
    if time() - d >= 1:
        temps += 0.1
        d = time()
        if temps < 4:
            esthetique.rockford(1 + temps, 5, 100, 0, 1, "black")
            esthetique.diamand(5.5, 5, 100, 0, 1, "black")
        if temps >= 4 and temps < 16.4 / 3:
            esthetique.pierre_eboulement(5, 0 + (temps  - 4)* 3, 100)
            esthetique.rockford(5, 5, 100, 1, 1, "black")
        if temps >= 16.4 / 3:
            esthetique.pierre_eboulement(5, 4.4, 100)
            esthetique.rockford_dead(5, 5, 100, 1, 1, "black")
    elif type_ev == "Quitte":
        return -1
    mise_a_jour()
    return 0, temps
    
def menu_map(cartes, d):
    cartes1, inutile, inutile1 = fonction.creer_map(cartes)
    fonction.initialiser_partie(cartes1)
    fonction.affichageV2(cartes1, 0, 1, 50, 0, -2, 8)
    mise_a_jour()
    if time() - d > 50:
        return 0
    return 1

def main():
    tempscommencement = time()
    ev1 = donne_evenement()
    score = "00000000"
    debug = -1
    mode = 0
    nbdiamand = 0
    #carte, tempstotal, diamand = fonction.creer_map("map_test.txt") 
    carte, tempstotal, diamand = fonction.creation_map_aleatoire() 

    diamand = int(diamand)
    fonction.initialiser_partie(carte)
    temps_pierre = time()
    while True:
        efface_tout()

        #mettre chaque P1 avec son temps de changement d'etat afin de tomber apres un certain temps sans avoir de temps commun entre tous les P1
        if time() - temps_pierre > 0.3:
            fonction.test_pierre_ou_diamand_eboulement(carte)
            fonction.tomber_de_pierre_ou_diamand(carte)
            fonction.tomber_pierre_laterale(carte)
            temps_pierre = time()

        if time() - temps_pierre > 0.15:
            fonction.test_si_pierre_va_tomber(carte)  
           
        fonction.affichage(carte, nbdiamand, diamand)
        tempsrestant = fonction.timer(tempstotal, tempscommencement)
        fonction.fond_score_temps_diams(score, tempsrestant, nbdiamand, diamand)

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
        if fonction.test_pousser_pierre(carte, ev):
            fonction.pousser_pierre(carte, touche(ev))
        if type_ev == "Quitte":
            return 1
        elif type_ev == "ClicGauche":
            coords = [clic_x(ev), clic_y(ev)]
            mode = fonction.quitte_or_retry(coords, coordretry, coordquitte)
        if type_ev == "Touche" and touche(ev) == "d":
            debug *= -1
        if debug == 1:
            nbdiamand, debug, tempstotal, score = fonction.debug(carte, nbdiamand, debug, tempstotal, score)
        else:
            nbdiamand, tempstotal, score = fonction.deplacer_perso(carte, nbdiamand, ev, diamand, tempstotal, score)
        if var["porte"] == 1:
            fonction.enleve_porte(carte, ev, nbdiamand, diamand)
        mise_a_jour()
        if mode != 0:
            return mode
        if fonction.win(nbdiamand, diamand, tempsrestant) or fonction.loose(carte, tempsrestant):
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
    cree_fenetre(var["dimension_fenetre"], var["dimension_fenetre"] + var["bandeau"])
    menu1 = 0
    temps = 0
    d = time()
    while True:
        while menu1 == 0:
            menu1, temps = menu(d, temps)
        while menu1 == 1:
            menu1 = menu_map('default/map2.txt', d)
        while menu1 == 2:
            menu1 = editeur_map.main()
        while menu1 == 3:
            menu1 = editeur_personnage.main()
        
        if main() == 1:
            break

    ferme_fenetre()
