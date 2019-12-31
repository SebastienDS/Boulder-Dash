import editeur_map
import editeur_personnage
import fonction
import esthetique
from upemtk import *
from variable import var
from time import time
import os
from pickle import load
import argparse


def menu(d, temps):
    esthetique.fond("black")
    if time() - d >= 1:
        temps += 0.1
        d = time()
        if temps < 4:
            esthetique.rockford(1 + temps, 6, 100, 0, 1, "black")
            esthetique.diamand(5.5, 6, 100, 0, 1, "black")
        if temps >= 4 and temps < 15.4 / 3:
            esthetique.pierre_eboulement(5, 2 + (temps - 4) * 3, 100)
            esthetique.rockford(5, 6, 100, 1, 1, "black")
        if temps >= 15.4 / 3:
            esthetique.pierre_eboulement(5, 5.4, 100)
            esthetique.rockford_dead(5, 6, 100, 1, 1, "black")
        if temps >= 6:
            temps = 0

    fonction.encadrement(
        "BOULDER DASH",
        var["dimension_fenetre"] // 2,
        30,
        "White",
        "black",
        50,
        1,
        1,
        "Impact",
    )
    MAP = fonction.encadrement(
        "SELECTION MAP",
        var["dimension_fenetre"] // 2,
        var["dimension_fenetre"] // 5,
        "White",
        "white",
        36,
        1,
        5,
        "Impact",
    )
    Sauvegarde_ = fonction.encadrement(
        "DERNIERE SAUVEGARDE",
        var["dimension_fenetre"] // 2,
        2 * var["dimension_fenetre"] // 5,
        "White",
        "white",
        36,
        1,
        5,
        "Impact",
    )
    EDIT_MAP = fonction.encadrement(
        "EDITEUR DE MAP",
        var["dimension_fenetre"] // 2,
        3 * var["dimension_fenetre"] // 5,
        "White",
        "white",
        36,
        1,
        5,
        "Impact",
    )
    EDIT_PERSO = fonction.encadrement(
        "EDITEUR DE PERSONNAGE",
        var["dimension_fenetre"] // 2,
        4 * var["dimension_fenetre"] // 5,
        "White",
        "white",
        36,
        1,
        5,
        "Impact",
    )
    
    ev = donne_evenement()
    type_ev = type_evenement(ev)
    if type_ev == "ClicGauche":
        coords = [clic_x(ev), clic_y(ev)]
        if fonction.test_clic(coords, MAP):
            return 1, temps
        if fonction.test_clic(coords, Sauvegarde_):
            return 2, temps
        if fonction.test_clic(coords, EDIT_MAP):
            return 3, temps
        if fonction.test_clic(coords, EDIT_PERSO):
            return 4, temps
    elif type_ev == "Quitte":
        return -1, temps
    mise_a_jour()
    return 0, temps


def menu_map(d):
    numcarte = 0
    choisis_carte = 0

    while choisis_carte == 0:
        efface_tout()
        if numcarte == 4:
            esthetique.fond("black")
            esthetique.point_dinterogation()
        elif numcarte == 5:
            esthetique.fond("black")
            fonction.encadrement(
                "Map perso",
                var["dimension_fenetre"] // 2,
                var["dimension_fenetre"] * 2 / 5,
                "white",
                "white",
                60,
                10,
                20,
                "Calibri",
            )

        else:
            cartes = "default/map" + "{}".format(numcarte) + ".txt"
            (
                cartes1,
                inutile,
                inutile1,
                var["score1"],
                var["score2"],
                var["score3"],
                score,
                nommap,
                tempslumiere
            ) = fonction.creer_map(cartes)
            fonction.initialiser_partie(cartes1)
            fonction.affichageV2(cartes1, 0, 1, 50, 0, -2, 8)
            esthetique.affiche_score([var["score1"], var["score2"], var["score3"]])
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
            "Impact",
        )
        retour = fonction.encadrement(
                "Retour au Menu",
                var["dimension_fenetre"] // 5,
                var["dimension_fenetre"] + 30,
                "red",
                "red",
                24,
                5,
                5,
                "Impact",
            )
        mise_a_jour()
        ev = donne_evenement()
        if type_evenement(ev) == "Quitte":
            return -1
        if type_evenement(ev) == "ClicGauche":
            coords = [clic_x(ev), clic_y(ev)]
            if fonction.test_suivant_menu(coords, suivant_menu):
                numcarte += 1
                numcarte = numcarte % 6
            if fonction.test_precedent(coords, precedent):
                numcarte -= 1
                numcarte = numcarte % 6
            if fonction.test_clic(coords, choix):
                if numcarte == 4:
                    return 6
                elif numcarte == 5:
                    nom = fonction.test_ouverture_custom_map()
                    if nom:
                        return nom
                else:
                    return cartes
            if fonction.test_clic(coords, retour):
                return 0


def main(cartes):
    """Lance le jeu"""
    tempscommencement = time()
    tempslumiere = time()
    ev1 = donne_evenement()
    debug = -1
    mode = 0
    nbdiamand = 0
    if cartes == 6:
        fonction.creation_map_aleatoire()
        cartes = "map_aleatoire.txt"
    elif cartes == 7:
        nom = fonction.test_ouverture_custom_map()
        if not nom:
            cartes = "map_aleatoire.txt"
        else:
            cartes = nom

    (
        carte,
        tempstotal,
        diamand,
        var["score1"],
        var["score2"],
        var["score3"],
        score,
        nommap,
        tempslumiere
    ) = fonction.creer_map(cartes)

    diamand = int(diamand)
    fonction.initialiser_partie(carte)
    temps_pierre = time()

    if var["personnage"]:
        with open("personnage/{}".format(var["personnage"]), "rb") as f:
            var["forme_personnage"] = load(f)
            editeur_personnage.redimensionner_forme(
                var["forme_personnage"], var["taille_case"]
            )

    while True:
        efface_tout()
        if time() - temps_pierre > 0.3:  # fait tomber pierre toute les ~ 0.3 sec
            fonction.test_pierre_ou_diamand_eboulement(carte)
            fonction.tomber_de_pierre_ou_diamand(carte)
            fonction.tomber_pierre_laterale(carte)
            temps_pierre = time()

        if (
            time() - temps_pierre > 0.15
        ):  # transforme des pierre qui peuvent tomber en des pierres qui vont tomber
            fonction.test_si_pierre_va_tomber(carte)
        fonction.affichage(carte, nbdiamand, diamand, tempslumiere)
        tempsrestant = fonction.timer(int(tempstotal), tempscommencement)
        fonction.fond_score_temps_diams(score, tempsrestant, nbdiamand, diamand)
        ev = donne_evenement()
        type_ev = type_evenement(ev)
        if fonction.test_pousser_pierre(carte, ev):
            fonction.pousser_pierre(carte, touche(ev))
        if type_ev == "Quitte":  # Peut quitter avec la croix
            return -1, nommap
        elif type_ev == "Touche":
            t = touche(ev)
            if (
                t == "Escape"
            ):  # ALLUME UN MENU pour sauvegarder recommencer ou quitter si l'utilisateur appui sur echap
                suite, tempscommencement, tempslumiere = fonction.menu_echap(tempscommencement, tempslumiere)
                if suite == -1:
                    return -1, nommap
                if suite == 6:
                    fonction.save_map_en_cours(
                        carte, diamand - nbdiamand, score, tempsrestant, nommap, time() - tempslumiere
                    )
                    return 0, nommap
                if suite == 7:
                    return 7, nommap
                if suite == 9:
                    return 9, nommap
            elif t == "d":
                debug *= -1
        if debug == 1:
            nbdiamand, debug, tempstotal, score, tempslumiere = fonction.debug(
                carte, nbdiamand, debug, tempstotal, score, tempslumiere
            )
        else:
            nbdiamand, tempstotal, score, tempslumiere = fonction.deplacer_perso(
                carte, nbdiamand, ev, diamand, tempstotal, score, tempslumiere
            )

        if var["porte"] == 1:
            fonction.enleve_porte(carte, ev, nbdiamand, diamand)
        mise_a_jour()
        if mode != 0:
            return mode, nommap

        if fonction.win(
            nbdiamand, diamand, tempsrestant, cartes, score, nommap
        ) or fonction.loose(carte, tempsrestant):
            while mode == 0:
                coordretry = fonction.encadrement(
                    "Retry",
                    var["dimension_fenetre"] // 7,
                    40,
                    "red",
                    "red",
                    12,
                    5,
                    5,
                    "Impact",
                )
                coordmenu = fonction.encadrement(
                    "Menu",
                    4 * var["dimension_fenetre"] // 5,
                    40,
                    "red",
                    "red",
                    12,
                    5,
                    5,
                    "Impact",
                )
                a = attente_clic()

                mode = fonction.menu_or_retry(a, coordretry, coordmenu)
            return mode, nommap


if __name__ == "__main__":
    print(
        "Made by Uniiiiiifffffay corporation with the collaboration of Natsouuuuuu corporation!!! All right reserved!"
    )
    menu1 = 0
    temps = 0

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--map", help="ouvre la map choisi")
    parser.add_argument(
        "-p", "--personnage", help="permet de changer le personnage en jeu"
    )
    parser.add_argument(
        "-l", "--lumiere", help="enleve la restriction de lumiere", action="store_true"
    )

    args = parser.parse_args()

    if args.map and os.path.isfile(os.path.join("map", args.map)):
        menu1 = 42
        choix = args.map
    if args.personnage and os.path.isfile(os.path.join("personnage", args.personnage)):
        var["personnage"] = args.personnage
    if args.lumiere:
        var["lumiere"] = True

    cree_fenetre(var["dimension_fenetre"], var["dimension_fenetre"] + var["bandeau"])

    d = time()
    while True:
        while menu1 == 0:
            choix = 0
            menu1, temps = menu(d, temps)
        if menu1 == 1:
            choix = menu_map(d)
        if menu1 == 2:
            choix = "map_sauvegarde.txt"
        while menu1 == 3:
            menu1 = editeur_map.main()
        while menu1 == 4:
            menu1 = editeur_personnage.main()
        if choix == -1 or menu1 == -1:
            break
        x = 9
        while choix != 0 and x == 9:
            x, choix = main(choix)
        menu1 = 0
        if x == -1:
            break

    ferme_fenetre()
