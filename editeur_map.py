import upemtk
from variable import var
from fonction import dico, my_input, encadrement, test_clic
import esthetique
import os
from copy import deepcopy


def affiche_map(carte):
    """
	affiche la map en cours de creation
	
	:param list carte: liste 2D contenant le jeu
	"""
    esthetique.fond("white")
    upemtk.rectangle(
        0,
        0,
        var["w_map"] * var["taille_case"],
        var["h_map"] * var["taille_case"],
        remplissage="black",
    )
    for j in range(var["h_map"]):
        for i in range(var["w_map"]):
            dico[carte[j][i]](i, j, var["taille_case"], 0, 0, "goldenrod3")


def affiche_tools(tools):
    """
	affiche la barre d'outil dans le bandeau en bas

	:param list tools: elements disponible a afficher dans la barre d'outil
	"""
    for i, elem in enumerate(tools):
        dico[elem](i, 6, var["bandeau"], 0, 0, "goldenrod3")


def save_map(carte, file_name, temps, diamand):
    """
	sauvegarde la map cree avec le bon format 

	:param list carte: liste 2D contenant le jeu 
	:param str file_name: nom de la map a sauvegarder
	:param int temps: temps limite pour finir la map
	:param int diamand: nombre de diamant requis avant de pouvoir finir

	>>> carte = [
	...     ["W", "W", "W", "W"], 
	...     ["W", "R", "E", "W"], 
	...     ["W", "D", ".", "W"], 
	...     ["W", "W", "W", "W"]]
	>>> save_map(carte, "test", 100, 1)
	>>> with open("map/test.txt") as f: 
	...     print(f.read())
	100s 1d
	WWWW
	WREW
	WD.W
	WWWW
	personne = 00000000
	personne = 00000000
	personne = 00000000
	00000000
	test.txt
	0
	"""
    with open("map/{}.txt".format(file_name), "w") as f:
        f.write("{}s {}d\n".format(temps, diamand))
        for j in range(len(carte)):
            for i in range(len(carte[0])):
                f.write(carte[j][i])
            f.write("\n")
        for i in range(3):
            f.write("personne = 00000000\n")
        f.write("00000000\n")
        f.write("{}.txt\n".format(file_name))
        f.write("0")


def save(carte):
    """
	test si la map peut etre cree
	
	:param list carte: liste 2D contenant le jeu 
	"""
    res = test_1_entree_1_sortie(carte)
    if res:
        my_input(res, "str")
        return

    if not test_mur_autour(carte):
        copy_carte = ajout_mur_autour(carte)
    else:
        copy_carte = deepcopy(carte)

    file_name = my_input("Nom de la map:", "str")
    temps = my_input("temps limite:", "int")
    diamand = my_input("diamant requis:", "int")

    if not test_nombre_diams_requis(copy_carte, diamand):
        my_input("nombre de diamant\n requis trop grand", "str")
        return

    if not os.path.isfile("map/{}.txt".format(file_name)):
        save_map(copy_carte, file_name, temps, diamand)
        my_input("Map sauvegardée", "str")
    else:
        reponse = my_input("Nom déjà utilisé\n      Ecraser ?", "str")
        if reponse.lower() in {
            "oui",
            "y",
            "o",
            "yes",
            "ye",
            "yeah",
            "ui",
            "certainement",
            "absolument",
            "bien sur",
        }:
            save_map(copy_carte, file_name, temps, diamand)
            my_input("Map sauvegardée", "str")
        else:
            my_input("Map non enregistrée", "str")


def test_nombre_diams_requis(carte, diamant):
    """
	test si la map contient suffisamment de diamant

	:param list carte: liste 2D contenant le jeu 
	:param int diamant: nombre de diamant requis saisie par lutilisateur
	:return: bool

	>>> test_nombre_diams_requis([["D", "D", "E"], ["a", "a", "d"], "e", "f", "g"], 2)
	True
	>>> test_nombre_diams_requis([["D", "D", "E"], ["a", "a", "d"], "e", "f", "g"], 1)
	True
	>>> test_nombre_diams_requis([["D", "D", "E"], ["a", "a", "d"], "e", "f", "g"], 3)
	False
	"""
    return sum(map(lambda x: x.count("D"), carte)) >= diamant


def test_1_entree_1_sortie(carte):
    """
	test si la map contient bien 1 unique entree et sortie

	:param list carte: liste 2D contenant le jeu 
	:return: None si la condition est verifié sinon le message d'erreur a afficher

	>>> carte = [
	...     ["W", "W", "W", "W"], 
	...     ["W", "R", "E", "W"], 
	...     ["W", "D", ".", "W"], 
	...     ["W", "W", "W", "W"]]
	>>> print(test_1_entree_1_sortie(carte))
	None
	>>> retour = test_1_entree_1_sortie([
	...     ["W", "W", "W", "W"], 
	...     ["W", "R", "E", "W"], 
	...     ["W", "D", ".", "W"],
	...     ["W", "R", ".", "W"], 
	...     ["W", "W", "W", "W"]])
	>>> list(map(str.strip, retour.split("\\n")))
	["nombre d'entree", 'incorrect']
	>>> retour = test_1_entree_1_sortie([
	...     ["W", "W", "W", "W"], 
	...     ["W", "R", "E", "W"], 
	...     ["W", "D", ".", "W"],
	...     ["W", "E", ".", "W"], 
	...     ["W", "W", "W", "W"]])
	>>> list(map(str.strip, retour.split("\\n")))
	['nombre de sortie', 'incorrect']
	>>> retour = test_1_entree_1_sortie([
	...     ["W", "W", "W", "W"], 
	...     ["W", "R", "E", "W"], 
	...     ["W", "D", ".", "W"],
	...     ["W", "E", "R", "W"], 
	...     ["W", "W", "W", "W"]])
	>>> list(map(str.strip, retour.split("\\n")))
	["nombre d'entree", 'et de', 'sortie incorrect']
	"""
    entree = 0
    sortie = 0
    for j in range(len(carte)):
        for i in range(len(carte[0])):
            if carte[j][i] == "R":
                entree += 1
            elif carte[j][i] == "E":
                sortie += 1

    if entree != 1 and sortie != 1:
        return "   nombre d'entree\n            et de\n    sortie incorrect"
    elif entree != 1:
        return "nombre d'entree\n      incorrect"
    elif sortie != 1:
        return "nombre de sortie\n      incorrect"


def test_mur_autour(carte):
    """
	test si la map est entouree de mur

	:param list carte: liste 2D contenant le jeu 
	:return: bool

	>>> test_mur_autour([
	...     ["W", "W", "W", "W"], 
	...     ["W", "R", "E", "W"], 
	...     ["W", "D", ".", "W"], 
	...     ["W", "W", "W", "W"]])
	True
	>>> test_mur_autour([
	...     ["W", ".", "W", "W"], 
	...     ["W", "R", "E", "W"], 
	...     ["W", "D", ".", "W"], 
	...     ["W", "W", "W", "W"]])
	False
	>>> test_mur_autour([ 
	...     ["R", "E"], 
	...     ["D", "."]])
	False
	"""
    if set(carte[0]) != {"W"}:
        return False
    if set(carte[-1]) != {"W"}:
        return False
    for j in range(len(carte)):
        if carte[j][0] != "W":
            return False
        if carte[j][-1] != "W":
            return False
    return True


def ajout_mur_autour(carte):
    """
	ajoute une ligne de mur autour de la carte

	:param list carte: liste 2D contenant le jeu 
	
	>>> ajout_mur_autour([
	...     ["W", ".", "W", "W"], 
	...     ["W", "R", "E", "W"], 
	...     ["W", "D", ".", "W"], 
	...     ["W", "W", "W", "W"]])
	[['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', '.', 'W', 'W', 'W'], ['W', 'W', 'R', 'E', 'W', 'W'], ['W', 'W', 'D', '.', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']]
	>>> ajout_mur_autour([["R", "E"], ["D", "."]])
	[['W', 'W', 'W', 'W'], ['W', 'R', 'E', 'W'], ['W', 'D', '.', 'W'], ['W', 'W', 'W', 'W']]
	"""
    copy_carte = deepcopy(carte)
    for j in range(len(copy_carte)):
        copy_carte[j].append("W")
        copy_carte[j].insert(0, "W")
    copy_carte.append(["W" for _ in range(len(copy_carte[0]))])
    copy_carte.insert(0, ["W" for _ in range(len(copy_carte[0]))])
    return copy_carte


def main():
    tools = ["G", "P", "W", "D", "R", "E"]  # block disponible dans la barre d'outil

    esthetique.fond("black")
    var["w_map"] = my_input("Nombre de colonnes:", "int")
    var["h_map"] = my_input("Nombre de lignes:", "int")

    var["taille_case"] = int(
        var["dimension_fenetre"] / max([var["w_map"], var["h_map"]])
    )  # fait en sorte que la map reste sur l'ecran
    carte = [["." for i in range(var["w_map"])] for i in range(var["h_map"])]
    element = "."

    while True:
        upemtk.efface_tout()
        affiche_map(carte)
        affiche_tools(tools)

        quitter = encadrement(
            "Quitter",
            var["dimension_fenetre"] * 2 / 3,
            2,
            "White",
            "white",
            15,
            1,
            1,
            "Impact",
        )

        sauvegarder = encadrement(
            "Sauvegarder",
            var["dimension_fenetre"] / 3,
            2,
            "White",
            "white",
            15,
            1,
            1,
            "Impact",
        )

        upemtk.mise_a_jour()
        ev = upemtk.donne_evenement()
        type_ev = upemtk.type_evenement(ev)
        if type_ev == "Quitte":
            return -1

        if type_ev == "ClicGauche":
            x_, y_ = (upemtk.clic_x(ev), upemtk.clic_y(ev))
            if test_clic((x_, y_), quitter):
                return 0
            if test_clic((x_, y_), sauvegarder):
                save(carte)
            else:
                x = x_ // var["taille_case"]
                y = y_ // var["taille_case"]

                if x < var["w_map"] and y < var["h_map"]:
                    carte[y][x] = element
                elif y_ // var["bandeau"] == 6:
                    element = tools[x_ // var["bandeau"]]

        elif type_ev == "Touche":
            t = upemtk.touche(ev)
            if t.upper() in dico:
                element = t.upper()
            elif t.lower() == "s":
                save(carte)
            elif t.lower() == "t":
                # touche pour les test
                pass
            elif t == "Escape":
                break

        elif type_ev == "ClicDroit":
            if upemtk.clic_y(ev) // var["taille_case"] < len(carte):
                carte[upemtk.clic_y(ev) // var["taille_case"]][
                    upemtk.clic_x(ev) // var["taille_case"]
                ] = "."

    return 0


if __name__ == "__main__":
    print("Programme principal: main.py")
