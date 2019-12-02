import upemtk
from variable import var, _touche
from random import choice, randint
from time import time
import esthetique
from copy import deepcopy


def creer_map(nomdufichier):
    """Transforme un fichier texte contenant une map en une matrice"""
    with open(
        "map/" + nomdufichier, "r"
    ) as fichier:  # ouvre le fichier contenant la carte
        contenu = fichier.read()  # lis le fichier
        contenu = contenu.split(
            "\n"
        )  # Construit une matriche de la carte /chaque ligne = chaine de caractère
        ted = contenu.pop(0)  # Enlève le temps et nombre de diamands
        ted = ted.split()
        t = ted[0][:-1]
        d = ted[1][:-1]
        while contenu[-1] == "":
            contenu.pop()
        score4 = contenu.pop()
        score3 = contenu.pop()
        score2 = contenu.pop()
        score1 = contenu.pop()
        for i in range(len(contenu)):
            contenu[i] = list(
                contenu[i]
            )  # transforme la chaine de caractère en une list('abc'=['a','b','c'])
    return contenu, t, d, score1, score2, score3, score4


def save_map_en_cours(carte, nb_diamand, score, temps_restant):
    with open("map/map_sauvegarde.txt", "w") as f:
        f.write("{}s {}d\n".format(temps_restant, nb_diamand))
        for j in range(len(carte)):
            for i in range(len(carte[0])):
                f.write(carte[j][i])
            f.write("\n")
        for i in range(1, 4):
            f.write("{}\n".format(var["score{}".format(i)]))
        f.write("{}\n".format(score))


# on associe les lettres aux fonctions les dessinant
dico = {
    "G": esthetique.terre,
    "P": esthetique.pierre,
    "R": esthetique.rockford,
    "W": esthetique.mur,
    "D": esthetique.diamand,
    "E": esthetique.sortie,
    ".": lambda *args: None,
    "K": esthetique.pierre_eboulement,
    "C": esthetique.diamand_eboulement,
    "F": esthetique.mur,
}


def timer(tempstotal, tempscommencement):
    return int(tempstotal) - (int(time() - tempscommencement))


def affichage(carte, nbdiamand, diamand):
    """Affiche la carte"""
    esthetique.fond("black")
    esthetique.lumiere()
    if var["porte"] == 0:
        esthetique.lumiere_escalier()
    carte[2][0] = "F"
    for y in range(len(carte) - 1, -1, -1):  # y = ligne
        for x in range(len(carte[y]) - 1, -1, -1):  # x = colonne
            dico[carte[y][x]](
                x + (var["nb_cases"] // 2 - var["pos_x"]),
                y + (var["nb_cases"] // 2 - var["pos_y"]),
                var["taille_case"],
                nbdiamand,
                diamand,
                "goldenrod3",
            )  # centre le perso
    esthetique.noir_lumiere()


def fond_score_temps_diams(score, tempsrestant, nbdiamand, diamand):
    """Affiche une banderolle avec le score et le bouton exitgame et retry"""
    nbdiamandrestant = diamand - nbdiamand
    if nbdiamandrestant < 0:
        nbdiamandrestant = 0
    esthetique.fond_score_temps_diams(score, tempsrestant, nbdiamandrestant)


def tomber_de_pierre_ou_diamand(carte):
    """Fais tomber les pierres"""
    for y in range(len(carte) - 2, -1, -1):
        for x in range(len(carte[0]) - 1, -1, -1):
            if carte[y][x] == "K" and carte[y + 1][x] == ".":
                carte[y][x], carte[y + 1][x] = ".", "K"
            if carte[y][x] == "C" and carte[y + 1][x] == ".":
                carte[y][x], carte[y + 1][x] = ".", "C"


def test_si_pierre_va_tomber(carte):
    for y in range(len(carte) - 2, -1, -1):
        for x in range(len(carte[0]) - 1, -1, -1):
            if carte[y][x] == "P" and carte[y + 1][x] == ".":
                carte[y][x] = "K"
            if carte[y][x] == "D" and carte[y + 1][x] == ".":
                carte[y][x] = "C"

def test_pierre_ou_diamand_eboulement(carte):
    for y in range(len(carte) - 1):
        for x in range(len(carte[0])):
            if carte[y][x] == "K" and carte[y + 1][x] not in [".", "R"]:
                carte[y][x] = "P"
            if carte[y][x] == "C" and carte[y + 1][x] not in [".", "R"]:
                carte[y][x] = "D"


def test_deplacement(carte, direction, liste):
    """test si le deplacement est possible"""
    return (
        carte[var["pos_y"] + _touche[direction][1]][
            var["pos_x"] + _touche[direction][0]
        ]
        in liste
    )


def enleve_porte(carte, ev, nbdiamand, diamand):
    type_ev = upemtk.type_evenement(ev)
    if type_ev == "Touche":
        t = upemtk.touche(ev)
        if t in _touche:
            if (
                carte[var["pos_y"] + _touche[t][1]][var["pos_x"] + _touche[t][0]]
                == carte[var["pos_sortie_y"]][var["pos_sortie_x"]]
                and nbdiamand >= diamand
            ):
                var["porte"] = 0


def deplace(carte, t):
    """se deplace dans la direction voulu et met a jour les positions du joueur"""
    carte[var["pos_y"] + _touche[t][1]][var["pos_x"] + _touche[t][0]] = "R"
    carte[var["pos_y"]][var["pos_x"]] = "."
    var["pos_x"] += _touche[t][0]
    var["pos_y"] += _touche[t][1]


def deplacer_perso(carte, nbdiamand, ev, diamand, tempstotal, score):
    """Test si le perso peut se deplacer, si oui, deplace le perso sur la carte en fonction de la touche utilisé"""
    type_ev = upemtk.type_evenement(ev)
    if type_ev == "Touche":
        t = upemtk.touche(ev)
        if t in _touche:
            if test_deplacement(carte, t, "D"):
                deplace(carte, t)
                return (
                    nbdiamand + 1,
                    int(tempstotal) + 10,
                    (8 - len((str(int(score) + 350)))) * "0" + (str(int(score) + 350)),
                )
            elif test_deplacement(carte, t, {"G", ".", "F"}):
                deplace(carte, t)
                return nbdiamand, tempstotal, score
            if (
                nbdiamand >= diamand
                and test_deplacement(carte, t, "E")
                and var["porte"] == 0
            ):
                deplace(carte, t)
                return nbdiamand, tempstotal, score
    return nbdiamand, tempstotal, score


def tomber_pierre_laterale(carte):
    for y in range(len(carte) - 2, 0, -1):
        for x in range(len(carte[0]) - 2, 0, -1):
            if (
                carte[y][x] in ["P", "D"]
                and carte[y][x + 1] == "."
                and carte[y + 1][x + 1] == "."
                and carte[y + 1][x] in ["P", "D", "W"]
            ):
                carte[y][x], carte[y][x + 1] = ".", carte[y][x]
            if (
                carte[y][x] in ["P", "D"]
                and carte[y][x - 1] == "."
                and carte[y + 1][x - 1] == "."
                and carte[y + 1][x] in ["P", "D", "W"]
            ):
                carte[y][x], carte[y][x - 1] = ".", carte[y][x]
    return carte


def test_pousser_pierre(carte, ev):
    type_ev = upemtk.type_evenement(ev)
    if type_ev == "Touche":
        t = upemtk.touche(ev)
        if (
            t == "Right"
            and carte[var["pos_y"]][var["pos_x"] + 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] + 2] == "."
        ):
            return True
        if (
            t == "Left"
            and carte[var["pos_y"]][var["pos_x"] - 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] - 2] == "."
        ):
            return True
    return False


def pousser_pierre(carte, t):
    """Test si une pierre est poussable, si oui, la pousse"""
    (
        carte[var["pos_y"]][var["pos_x"] + _touche[t][0]],
        carte[var["pos_y"]][var["pos_x"] + 2 * _touche[t][0]],
    ) = (".", "P")


def loose(carte, tempsrestant):
    """test si joueur s'est pris une pierre
    si oui met l'image de défaite et retourne True
    """
    if carte[var["pos_y"] - 1][var["pos_x"]] in ["K", "C"] or tempsrestant <= 0:
        upemtk.efface_tout()
        esthetique.fond("black")
        esthetique.personnage_defaitiste()
        upemtk.texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 4,
            "DÉFAITE !",
            couleur="red",
            ancrage="center",
            taille=75,
        )
        return True
    return False


def win(nbdiamand, diamand, tempsrestant, cartes, score):
    """Regarde si l'utilisateur gagne
    si oui, met l'image de victoire et retourne True"""
    if (
        var["pos_x"] == var["pos_sortie_x"]
        and var["pos_y"] == var["pos_sortie_y"]
        and nbdiamand >= diamand
    ):
        suivant = 0
        upemtk.efface_tout()
        while suivant == 0:
            suivant, score = esthetique.menu_score(nbdiamand, tempsrestant, suivant, score)
        upemtk.efface_tout()
        esthetique.fond("cyan")
        upemtk.texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 3,
            "Victoire !",
            couleur="black",
            ancrage="center",
            taille=75,
        )
        esthetique.personnage_victorieux()
        esthetique.coffre()
        esthetique.affiche_score_victoire(score)
        if cartes == 6:
            del var["carte"]
        return True
    return False


def initialiser_partie(carte):
    """Initialise les parametres par defaut de la partie"""
    for y in range(len(carte)):
        for x in range(len(carte[y])):
            if carte[y][x] == "R":  # on recupere la position du perso
                var["pos_x"] = x
                var["pos_y"] = y
            elif carte[y][x] == "E":  # on recupere la position de l'arrivée
                var["pos_sortie_x"] = x
                var["pos_sortie_y"] = y
    var["porte"] = 1
    var["taille_case"] = var["dimension_fenetre"] // var["nb_cases"]


def debug(carte, nbdiamand, debug, tempstotal, score):
    """Perso joue aléatoirement"""
    choix = ["Up", "Down", "Left", "Right"]
    while True:
        x = choice(choix)
        if test_deplacement(carte, x, "D"):
            deplace(carte, x)
            return (
                nbdiamand + 1,
                debug,
                int(tempstotal) + 10,
                (8 - (len(str(int(score) + 350)))) * "0" + (str(int(score) + 350)),
            )
        elif test_deplacement(carte, x, {"G", "."}):
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score
        elif test_deplacement(carte, x, "E") and var["porte"] == 0:
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score
        elif (
            x == "Right"
            and carte[var["pos_y"]][var["pos_x"] + 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] + 2] == "."
        ):
            pousser_pierre(carte, x)
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score
        elif (
            x == "Left"
            and carte[var["pos_y"]][var["pos_x"] - 1] == "P"
            and carte[var["pos_y"]][var["pos_x"] - 2] == "."
        ):
            pousser_pierre(carte, x)
            deplace(carte, x)
            return nbdiamand, debug, tempstotal, score
        choix.remove(x)
        if choix == []:
            debug = -1
            return nbdiamand, debug, tempstotal, score
    return nbdiamand, debug, tempstotal, score


def encadrement(
    msg, x, y, couleurTXT, couleurCadre, Taille, Epaisseur, Espacement, polise
):  # Ecrit et encadre un texte puis donne les coordonnées du cadre (pour clic)
    upemtk.texte(10000000, y, msg, couleur=couleurTXT, police=polise, taille=Taille)
    upemtk.longueur_texte(msg)
    x2 = x + upemtk.longueur_texte(msg) // 2 + Espacement
    y2 = y + upemtk.hauteur_texte() + Espacement
    upemtk.texte(
        x - upemtk.longueur_texte(msg) // 2,
        y,
        msg,
        couleur=couleurTXT,
        police="Impact",
        taille=Taille,
    )
    upemtk.rectangle(
        x - Espacement - upemtk.longueur_texte(msg) // 2,
        y - Espacement,
        x2,
        y2,
        couleur=couleurCadre,
        epaisseur=Epaisseur,
    )
    return [x - Espacement, y - Espacement, x2, y2]


def _input(msg, reponse_defaut):
    texte = reponse_defaut
    while True:
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)
        if type_ev == "Touche":
            x = upemtk.touche(ev)

            if x == "Return":
                return texte
            elif x == "BackSpace":
                texte = texte[:-1]

            elif len(x) == 1 and len(texte) <= 18:
                texte += x
            elif x == "space":
                texte += " "
            elif x == "minus":
                texte += "-"
            elif x == "underscore":
                texte += "_"
            elif x == "period":
                texte += "."

        elif type_ev == "ClicGauche":
            return texte

        upemtk.efface("texte_input")
        upemtk.texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 2,
            texte,
            couleur="white",
            ancrage="center",
            tag="texte_input",
        )
        upemtk.mise_a_jour()


def my_input(msg, type_retour, reponse_defaut=""):
    upemtk.rectangle(
        var["dimension_fenetre"] // 2 - 180,
        var["dimension_fenetre"] // 2 - 100,
        var["dimension_fenetre"] // 2 + 180,
        var["dimension_fenetre"] // 2 + 100,
        couleur="gray28",
        remplissage="gray",
        epaisseur=5,
        tag="cadre",
    )

    while True:
        upemtk.texte(
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 2 - 50,
            msg,
            couleur="white",
            ancrage="center",
            tag="msg",
        )
        _var = _input(msg, reponse_defaut)
        if type_retour == "int":
            if _var.isdigit():
                if int(_var) < 500 and int(_var) > 0:
                    upemtk.efface("msg")
                    upemtk.efface("msg_erreur")
                    upemtk.efface("texte_input")
                    upemtk.efface("cadre")
                    return int(_var)
                elif int(_var) == 0:
                    upemtk.efface("msg_erreur")
                    upemtk.texte(
                        var["dimension_fenetre"] // 2,
                        var["dimension_fenetre"] // 2 + 75,
                        "Valeur trop petite",
                        couleur="red",
                        ancrage="center",
                        police="impact",
                        tag="msg_erreur",
                    )
                else:
                    upemtk.efface("msg_erreur")
                    upemtk.texte(
                        var["dimension_fenetre"] // 2,
                        var["dimension_fenetre"] // 2 + 75,
                        "Valeur trop grande",
                        couleur="red",
                        ancrage="center",
                        police="impact",
                        tag="msg_erreur",
                    )
            else:
                upemtk.efface("msg_erreur")
                upemtk.texte(
                    var["dimension_fenetre"] // 2,
                    var["dimension_fenetre"] // 2 + 75,
                    "Valeur entiere requis",
                    couleur="red",
                    ancrage="center",
                    police="impact",
                    tag="msg_erreur",
                )
        else:
            upemtk.efface("msg")
            upemtk.efface("msg_erreur")
            upemtk.efface("texte_input")
            upemtk.efface("cadre")
            return _var

def creation_map_aleatoire(x=40, y=22):
    if "carte" not in var.keys():
        carte = [["W" for _ in range(x)] for _ in range(y)]
        nb_diam = 0

        for j in range(1, y - 1):
            for i in range(1, x - 1):
                nb_random = randint(0, 1000)
                if nb_random < 650:
                    carte[j][i] = "G"
                elif nb_random < 750:
                    carte[j][i] = "."
                elif nb_random < 850:
                    carte[j][i] = "P"
                elif nb_random < 900:
                    carte[j][i] = "D"
                    nb_diam += 1

        coord_entree = (randint(1, x - 2), randint(1, y - 2))
        coord_sortie = (randint(1, x - 2), randint(1, y - 2))
        while coord_entree == coord_sortie:
            coord_sortie = (randint(1, x - 2), randint(1, y - 2))

        carte[coord_entree[1]][coord_entree[0]] = "R"
        carte[coord_sortie[1]][coord_sortie[0]] = "E"
        var["carte"] = (carte, nb_diam - randint(3, 8))
        return deepcopy(var["carte"][0]), 100, var["carte"][1]
    else:
        return deepcopy(var["carte"][0]), 100, var["carte"][1]

def menu_or_retry(a, coordretry, coordmenu):
    """Regarde si l'utilisateur à décidé de quitté ou de recommencer
    et retourne donc sa réponse"""
    if (
        a[0] < coordretry[2]
        and a[0] > coordretry[0]
        and a[1] < coordretry[3]
        and a[1] > coordretry[1]
    ):
        return 9
    if (
        a[0] < coordmenu[2]
        and a[0] > coordmenu[0]
        and a[1] < coordmenu[3]
        and a[1] > coordmenu[1]
    ):
        return 7
    return 0

def test_clic(coordsclic, coordscarre):
    if (
        coordsclic[0] < coordscarre[2]
        and coordsclic[0] > coordscarre[0]
        and coordsclic[1] < coordscarre[3]
        and coordsclic[1] > coordscarre[1]
    ):
        return True
    return False

def test_suivant_menu(coords, suivant):
    if (
        suivant[0][0] <= coords[0] <= suivant[2][0]
        and suivant[0][1] + (coords[0] - suivant[0][0]) * 0.5
        <= coords[1]
        <= suivant[1][1] - (coords[0] - suivant[0][0]) * 0.5
    ):
        return 1
    return 0


def test_precedent(coords, precedent):
    if (
        precedent[0][0] >= coords[0] >= precedent[2][0]
        and precedent[0][1] + (precedent[0][0] - coords[0]) * 0.5
        <= coords[1]
        <= precedent[1][1] - (precedent[0][0] - coords[0]) * 0.5
    ):
        return 1
    return 0

def affichageV2(carte, nbdiamand, diamand, taille, x_, y_, nbrcase):
    """Affiche la carte"""
    esthetique.fond("black")
    for y in range(len(carte) - 1, -1, -1):  # y = ligne
        for x in range(len(carte[y]) - 1, -1, -1):  # x = colonne
            dico[carte[y][x]](
                (x + (var["nb_cases"] // 2 - var["pos_x"])) + x_,
                (y + (var["nb_cases"] // 2 - var["pos_y"])) + y_,
                taille,
                nbdiamand,
                diamand,
                "goldenrod3",
            )  # centre le perso
    upemtk.rectangle(
        x_ * taille + nbrcase * taille + 2 * taille,
        y_ * taille,
        var["dimension_fenetre"],
        var["dimension_fenetre"] + 100,
        remplissage="black",
    )
    upemtk.rectangle(
        x_ * taille,
        y_ * taille + nbrcase * taille + 2 * taille,
        var["dimension_fenetre"],
        var["dimension_fenetre"] + 100,
        remplissage="black",
    )
    upemtk.rectangle(
        x_ * taille + 2 * taille,
        y_ * taille + 3 * taille,
        x_ * taille + nbrcase * taille + 2 * taille + 5,
        y_ * taille + nbrcase * taille + 2 * taille + 5,
        couleur="gold",
        epaisseur=10,
    )

def menu_echap(temps):
    d = time()
    while True:
        esthetique.fond("black")
        encadrement('MENU', 
            var["dimension_fenetre"] // 2, 
            30, "White", "black", 
            50, 1, 1, "Impact") 

        continuer = encadrement('CONTINUER',
            var["dimension_fenetre"] // 2,
            var["dimension_fenetre"] // 5,
            "White", "white",
            36, 1, 5, "Impact") 
        sauvegarder = encadrement('SAUVEGARDER',
            var["dimension_fenetre"] // 2,
            2 * var["dimension_fenetre"] // 5,
            "White", "white",
            36, 1, 5, "Impact") 
        recommencer = encadrement('RECOMMENCER',
            var["dimension_fenetre"] // 2,
            3 * var["dimension_fenetre"] // 5,
            "White", "white", 
            36, 1, 5, "Impact") 
        quitter = encadrement('QUITTER LE JEU', 
            var["dimension_fenetre"] // 2, 
            4 * var["dimension_fenetre"] // 5, 
            "White", "white", 
            36, 1, 5, "Impact")
        upemtk.mise_a_jour()
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)
        if type_ev == "Touche":
            t = upemtk.touche(ev)
            if t == "Escape":
                return 5
        if type_ev == "ClicGauche":
            coords = [upemtk.clic_x(ev), upemtk.clic_y(ev)]
            if test_clic(coords, continuer):
                return 5, temps + time() - d
            if test_clic(coords, sauvegarder):
                return 6, temps + time() - d
            if test_clic(coords, recommencer):
                return 9, temps + time() - d
            if test_clic(coords, quitter):
                return -1, temps + time() - d
