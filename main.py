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
        30, "White", "black", 
        50, 1, 1, "Impact") 
    MAP = fonction.encadrement('SELECTION MAP',
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 5,
        "White", "white",
        36, 1, 5, "Impact") 
    Sauvegarde_ = fonction.encadrement('DERNIERE SAUVEGARDE',
        var["dimension_fenetre"] // 2,
        2 * var["dimension_fenetre"] // 5,
        "White", "white",
        36, 1, 5, "Impact") 
    EDIT_MAP = fonction.encadrement('EDITEUR DE MAP',
        var["dimension_fenetre"] // 2,
        3 * var["dimension_fenetre"] // 5,
        "White", "white", 
        36, 1, 5, "Impact") 
    EDIT_PERSO = fonction.encadrement('EDITEUR DE PERSONNAGE', 
        var["dimension_fenetre"] // 2, 
        4 * var["dimension_fenetre"] // 5, 
        "White", "white", 
        36, 1, 5, "Impact") 

    ev = donne_evenement()
    type_ev = type_evenement(ev)
    if type_ev == "ClicGauche":
        coords = [clic_x(ev), clic_y(ev)]
        if fonction.test_MAP(coords, MAP):
            return 1, temps
        if fonction.test_sauvegarde(coords, Sauvegarde_):
            return 2, temps
        if fonction.test_EDIT_MAP(coords, EDIT_MAP):
            return 3, temps
        if fonction.test_EDIT_PERSO(coords, EDIT_PERSO):
            return 4, temps
    elif type_ev == "Quitte":
        return -1, temps 

    if time() - d >= 1:
        temps += 0.1
        d = time()
        if temps < 4:
            esthetique.rockford(1 + temps, 6, 100, 0, 1, "black")
            esthetique.diamand(5.5, 6, 100, 0, 1, "black")
        if temps >= 4 and temps < 15.4 / 3:
            esthetique.pierre_eboulement(5, 2 + (temps  - 4)* 3, 100)
            esthetique.rockford(5, 6, 100, 1, 1, "black")
        if temps >= 15.4 / 3:
            esthetique.pierre_eboulement(5, 5.4, 100)
            esthetique.rockford_dead(5, 6, 100, 1, 1, "black")
        if temps >= 6:
            temps = 0
    
    mise_a_jour()
    return 0, temps
    

def menu_map(d):
    numcarte = 0
    choisis_carte = 0

    while choisis_carte == 0:
        if numcarte == 4:
            esthetique.fond("black")
            esthetique.point_dinterogation()
        else:
            cartes = 'default/map' + '{}'.format(numcarte) + '.txt'
            cartes1, inutile, inutile1, var["score1"], var["score2"], var["score3"], score = fonction.creer_map(cartes)
            fonction.initialiser_partie(cartes1)
            fonction.affichageV2(cartes1, 0, 1, 50, 0, -2, 8)

        suivant_menu = esthetique.fleche_(11, 5, 50, 1)
        precedent = esthetique.fleche_(1, 5, 50, -1)
        choix = fonction.encadrement(
            "SUIVANT",
            4 * var["dimension_fenetre"] // 5,
            var["dimension_fenetre"] + 30,
            "red",
            "red",
            24,
            5,
            5,
            "Impact"
        )
        esthetique.affiche_score([var["score1"], var["score2"], var["score3"]])
        mise_a_jour()
        efface_tout()

        ev = donne_evenement()
        if type_evenement(ev) == "Quitte":
            return -1
        if type_evenement(ev) == "ClicGauche":
            coords = [clic_x(ev), clic_y(ev)]
            if fonction.test_suivant_menu(suivant_menu, coords):
                numcarte += 1
                numcarte = numcarte % 5
            if fonction.test_precedent(precedent, coords):
                numcarte -= 1
                numcarte = numcarte % 5
            if fonction.test_choix(choix, coords):
                if numcarte != 4:
                    return cartes
                else:
                    return 6

def main(cartes):
    tempscommencement = time()
    ev1 = donne_evenement()
    debug = -1
    mode = 0
    nbdiamand = 0
    if cartes == 6:
        carte, tempstotal, diamand = fonction.creation_map_aleatoire() 
    else:
        carte, tempstotal, diamand, var["score1"], var["score2"], var["score3"], score = fonction.creer_map(cartes) 

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
            "Impact"
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
            "Impact"
        )

        ev = donne_evenement()
        type_ev = type_evenement(ev)
        if fonction.test_pousser_pierre(carte, ev):
            fonction.pousser_pierre(carte, touche(ev))

        if type_ev == "Quitte":
            fonction.save_map_en_cours(carte, diamand - nbdiamand, score, tempsrestant)         ###################################################################
            return -1
        elif type_ev == "ClicGauche":
            coords = [clic_x(ev), clic_y(ev)]
            mode = fonction.quitte_or_retry(coords, coordretry, coordquitte)
        elif type_ev == "Touche":
            t = touche(ev)
            if t == "Escape":
                fonction.my_input("inserer menu ici", "str")
            elif t == "d":
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

        if fonction.win(nbdiamand, diamand, tempsrestant, cartes, score) or fonction.loose(carte, tempsrestant):
            while mode == 0:
                coordretry = fonction.encadrement(
                    "Retry", var["dimension_fenetre"] // 7, 40, "red", "red", 12, 5, 5,"Impact"
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
                    "Impact"
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
    choix = 0
    temps = 0
    x = 9
    d = time()

    while True:
        while menu1 == 0:
            menu1, temps = menu(d, temps)
        if menu1 == 1:
            choix = menu_map(d)
        if menu1 == 2:
            choix = "map_sauvegarde.txt"
            menu1 = 0
        while menu1 == 3:
            menu1 = editeur_map.main()
        while menu1 == 4:
            menu1 = editeur_personnage.main()
        if choix == -1 or menu1 == -1:
            break
        while choix != 0 and x == 9:
            x = main(choix)
        if x == -1:
            break

    ferme_fenetre()
