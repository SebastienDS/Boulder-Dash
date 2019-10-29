from upemtk import *
from variable import var


def creer_map(nomdufichier):
	with open("map/" + nomdufichier, "r") as fichier:
		contenu = fichier.read()
		contenu = contenu.split("\n")
		contenu.pop(0)
		for i in range(len(contenu)):
			contenu[i] = list(contenu[i])
	return contenu


def terre(x, y):
	"""Dessine la terre aux coordonnées x, y"""
	rectangle(
		x * var["taille_case"],
		y * var["taille_case"],
		x * var["taille_case"] + var["taille_case"] - 1,
		y * var["taille_case"] + var["taille_case"] - 1,
		couleur="pink",
		remplissage="pink",
	)


def pierre(x, y):
	"""Dessine une pierre aux coordonnées x, y"""
	cercle(
		x * var["taille_case"] + var["taille_case"] / 2,
		y * var["taille_case"] + var["taille_case"] / 2,
		(var["taille_case"] / 2) - 1,
		couleur="grey",
		remplissage="grey",
	)


def rockford(x, y):
	"""Dessine rockford aux coordonnées x, y"""
	cercle(
		x * var["taille_case"] + var["taille_case"] / 2,
		y * var["taille_case"] + var["taille_case"] / 2,
		(var["taille_case"] / 2) - 1,
		couleur="green",
		remplissage="green",
	)
	cercle(
		x * var["taille_case"] + var["taille_case"] / 2,
		y * var["taille_case"] + 2 * var["taille_case"] / 3 - var["taille_case"] / 15,
		var["taille_case"] / 4,
		couleur="black",
		remplissage="black",
	)
	rectangle(
		x * var["taille_case"] + (var["taille_case"] / 2) - var["taille_case"] / 4,
		y * var["taille_case"]
		+ (2 * var["taille_case"] / 3)
		- var["taille_case"] / 4
		- var["taille_case"] / 15,
		x * var["taille_case"] + (var["taille_case"] / 2) + var["taille_case"] / 4,
		y * var["taille_case"] + (2 * var["taille_case"] / 3) - var["taille_case"] / 15,
		couleur="green",
		remplissage="green",
	)
	cercle(
		x * var["taille_case"] + var["taille_case"] / 3,
		y * var["taille_case"] + var["taille_case"] / 3,
		var["taille_case"] / 13,
		couleur="black",
		remplissage="black",
	)
	cercle(
		x * var["taille_case"] + 2 * var["taille_case"] / 3,
		y * var["taille_case"] + var["taille_case"] / 3,
		var["taille_case"] / 13,
		couleur="black",
		remplissage="black",
	)


def mur(x, y):
	"""Dessine un mur aux coordonnées x, y"""
	rectangle(
		x * var["taille_case"],
		y * var["taille_case"],
		var["taille_case"] + x * var["taille_case"] - 1,
		var["taille_case"] + y * var["taille_case"] - 1,
		couleur="black",
		remplissage="black",
	)


def diamand(x, y):
	"""Dessine un diamand aux coordonnées x, y"""
	rectangle(
		x * var["taille_case"],
		y * var["taille_case"],
		var["taille_case"] + x * var["taille_case"] - 1,
		var["taille_case"] + y * var["taille_case"] - 1,
		couleur="blue",
		remplissage="blue",
	)


def sortie(x, y):
	"""Dessine la sortie aux coordonnées x, y"""
	rectangle(
		x * var["taille_case"],
		y * var["taille_case"],
		var["taille_case"] + x * var["taille_case"] - 1,
		var["taille_case"] + y * var["taille_case"] - 1,
		couleur="green",
		remplissage="green",
	)


def rien(x, y):
	pass


# on associe les lettres aux fonctions les dessinant
dico = {
	"G": terre,  # carre marron
	"P": pierre,  # rond gris
	"R": rockford,  # rond blanc
	"W": mur,  # carre noir
	"D": diamand,  # carre bleu
	"E": sortie,  # carre vert
	".": rien,
}


def affichage(carte):
	"""Affiche la carte"""
	fond()
	for y in range(len(carte)):  # y = ligne
		for x in range(len(carte[y])):  # x = colonne
			dico[carte[y][x]](x, y)


def fond():
	rectangle(
		0,
		0,
		var["dimension_fenetre"],
		var["dimension_fenetre"],
		couleur="purple",
		remplissage="purple",
	)


def personnage():
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3,
		var["dimension_fenetre"] // 4,
		couleur="green",
		remplissage="green",
	)
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 8,
		couleur="black",
		remplissage="black",
	)
	rectangle(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
		2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
		couleur="green",
		remplissage="green",
	)
	cercle(
		var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 20,
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 20,
		couleur="black",
		remplissage="black",
	)
	cercle(
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 20,
		couleur="black",
		remplissage="black",
	)


def tomber_de_pierre(carte):
    """Fais tomber les pierres"""
    for y in range(len(carte)):
    	for x in range(len(carte[0])):
    		if carte[y][x] == 'P' and carte[y+1][x]=='.':
    			carte[y][x], carte[y+1][x] = '.' , 'P'


def deplacer_perso(carte):
	"""Test si le perso peut se deplacer, si oui, deplace le perso sur la carte en fonction de la touche utilisé"""
	ev = donne_evenement()
	type_ev = type_evenement(ev)
	if type_ev == "Touche":
		t = touche(ev)
		if t == "Right" and carte[var["pos_y"]][var["pos_x"] +1] in ["G", ".", "E"]:
			carte[var["pos_y"]][var["pos_x"] +1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] += 1
		elif t == "Left" and carte[var["pos_y"]][var["pos_x"] -1] in ["G", ".", "E"]:
			carte[var["pos_y"]][var["pos_x"] -1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] -= 1
		elif t == "Up" and carte[var["pos_y"] -1][var["pos_x"]] in ["G", ".", "E"]:
			carte[var["pos_y"] -1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] -= 1
		elif t == "Down" and carte[var["pos_y"] +1][var["pos_x"]] in ["G", ".", "E"]:
			carte[var["pos_y"] +1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] += 1


def pousser_pierre(carte, deplacement):
	"""Test si une pierre est poussable, si oui, la pousse"""
	pass


def win():
	"""Regarde si l'utilisateur gagne"""
	if var["pos_x"] == var["pos_sortie_x"] and var["pos_y"] == var["pos_sortie_y"]:
		efface_tout()
		fond()
		texte(
			var["dimension_fenetre"] // 2,
			var["dimension_fenetre"] // 4,
			"Victoire !",
			couleur="black",
			ancrage="center",
			taille=75
		)
		personnage()
		return True
	return False


def initialiser_partie(carte):
	"""Initialise les parametres par defaut de la partie"""
	for y in range(len(carte)):
		for x in range(len(carte[y])): 
			if carte[y][x] == "R":
				var["pos_x"] = x
				var["pos_y"] = y
			elif carte[y][x] == "E":
				var["pos_sortie_x"] = x
				var["pos_sortie_y"] = y


def debug(carte):
	"""Perso joue aléatoirement"""
	pass


if __name__ == "__main__":
	import doctest

	doctest.testmod()
