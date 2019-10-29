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
		couleur="sienna4",
		remplissage="sienna4",
	)


def pierre(x, y):
	"""Dessine une pierre aux coordonnées x, y"""
	cercle(
		x * var["taille_case"] + var["taille_case"] / 2,
		y * var["taille_case"] + var["taille_case"] / 2,
		(var["taille_case"] / 2) - 1,
		couleur="gray39",
		remplissage="gray39",
	)


def rockford(x, y):
	"""Dessine rockford aux coordonnées x, y"""
	cercle(
		x * var["taille_case"] + var["taille_case"] // 2 - var["taille_case"] // 4 ,
		y * var["taille_case"] + 3 * var["taille_case"] // 4 - var["taille_case"] // 8,
		var["taille_case"] // 12,
		couleur="lightpink",
		remplissage="lightpink"
	)
	cercle(
		x * var["taille_case"] + var["taille_case"] // 2 + var["taille_case"] // 4 ,
		y * var["taille_case"] + 3 *var["taille_case"] // 4 - var["taille_case"] // 8,
		var["taille_case"] // 12,
		couleur="lightpink",
		remplissage="lightpink"
	)
	cercle(
		x * var["taille_case"] + var["taille_case"] // 3,
		y * var["taille_case"] + 8 *var["taille_case"] // 9,
		var["taille_case"] // 12,
		couleur="black",
		remplissage="red"
	)
	cercle(
		x * var["taille_case"] + 2 *var["taille_case"] // 3 ,
		y * var["taille_case"] + 8 *var["taille_case"] // 9 ,
		var["taille_case"] // 12,
		couleur="black",
		remplissage="red"
	)
	cercle(
		x * var["taille_case"] + var["taille_case"] // 2,
		y * var["taille_case"] + 2 * var["taille_case"] // 3,
		var["taille_case"] // 4,
		couleur="black",
		remplissage="lightpink",
	)
	



def mur(x, y):
	"""Dessine un mur aux coordonnées x, y"""
	rectangle(						 #fond
		x * var["taille_case"],
		y * var["taille_case"],
		var["taille_case"] + x * var["taille_case"] ,
		var["taille_case"] + y * var["taille_case"] - 1,
		couleur="gray15",
		remplissage="gray15",
	)
	ligne(							#deuxième ligne horizontale
		x * var["taille_case"],
		y * var["taille_case"] + var["taille_case"] // 3 ,
		var["taille_case"] + x * var["taille_case"] ,
		(var["taille_case"] + y * var["taille_case"] - 1) - 2 * var["taille_case"] // 3,
	couleur = 'white',
	epaisseur = var["taille_case"] // 20
	)
	ligne(							#troisième ligne horizontale
		x * var["taille_case"],
		y * var["taille_case"] + 2 * var["taille_case"] // 3 ,
		var["taille_case"] + x * var["taille_case"] ,
		(var["taille_case"] + y * var["taille_case"] - 1) - var["taille_case"] // 3,
	couleur = 'white',
	epaisseur = var["taille_case"] // 20
	)
	ligne(							#première ligne horitontale
		x * var["taille_case"] ,
		y * var["taille_case"] ,
		var["taille_case"] + x * var["taille_case"] ,
		(var["taille_case"] + y * var["taille_case"] - 1) - 3 * var["taille_case"] // 3,
	couleur = 'white',
	epaisseur = var["taille_case"] // 20
	)
	ligne(							#quatrième ligne horizontale
		x * var["taille_case"],
		y * var["taille_case"] + 3 * var["taille_case"] // 3 ,
		var["taille_case"] + x * var["taille_case"],
		var["taille_case"] + y * var["taille_case"] - 1,
	couleur = 'white',
	epaisseur = var["taille_case"] // 20
	)
	ligne(							#Première ligne verticale
		x * var["taille_case"] + 1 * var["taille_case"] // 4 ,
		y * var["taille_case"] ,
		x * var["taille_case"] + 1 * var["taille_case"] // 4,
		y * var["taille_case"] + var["taille_case"] // 3,
	couleur = 'white',
	epaisseur = var["taille_case"] // 20
	)	
	ligne(							#Deuxième ligne verticale
		x * var["taille_case"] + 1 * var["taille_case"] // 2,
		y * var["taille_case"] + var["taille_case"] // 3,
		x * var["taille_case"] + 1 * var["taille_case"] // 2,
		y * var["taille_case"] + 2 * var["taille_case"] // 3,
	couleur = 'white',
	epaisseur = var["taille_case"] // 20
	)
	ligne(							#Troisième ligne verticale
		x * var["taille_case"] + 3 * var["taille_case"] // 4,
		y * var["taille_case"] + 2 * var["taille_case"] // 3,
		x * var["taille_case"] + 3 * var["taille_case"] // 4,
		y * var["taille_case"] + var["taille_case"],
		couleur = 'white',
		epaisseur = var["taille_case"] // 20
	)
	
def diamand(x, y):
	"""Dessine un diamand aux coordonnées x, y"""
	rectangle(
		x * var["taille_case"],
		y * var["taille_case"],
		var["taille_case"] + x * var["taille_case"] - 1,
		var["taille_case"] + y * var["taille_case"] - 1,
		couleur="lightblue",
		remplissage="lightblue",
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
		couleur="black",
		remplissage="black",
	)


def personnage_victorieux():
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3,
		var["dimension_fenetre"] // 4,
		couleur="lightpink",
		remplissage="lightpink",
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
		couleur="lightpink",
		remplissage="lightpink",
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

def personnage_defaitiste():
	cercle(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 4 ,
		3 *var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 12,
		couleur="lightpink",
		remplissage="lightpink"
	)
	cercle(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 4 ,
		3 *var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 12,
		couleur="lightpink",
		remplissage="lightpink"
	)
	cercle(
		var["dimension_fenetre"] // 3,
		8 *var["dimension_fenetre"] // 9,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="red"
	)
	cercle(
		2 *var["dimension_fenetre"] // 3 ,
		8 *var["dimension_fenetre"] // 9 ,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="red"
	)
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3,
		var["dimension_fenetre"] // 4,
		couleur="black",
		remplissage="lightpink",
	)
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="black",
	)
	
	ligne(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 20, 
		var["dimension_fenetre"] // 2,
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
		couleur = "black",
		epaisseur = 10
		)
	ligne(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8, 
		var["dimension_fenetre"] // 2 ,
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
		couleur="black",
		epaisseur = 10
	)
	ligne(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 20, 
		var["dimension_fenetre"] // 2,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
		couleur = "black",
		epaisseur = 10
		)
	ligne(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8, 
		var["dimension_fenetre"] // 2 ,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
		couleur="black",
		epaisseur = 10
	)

	ligne(
		var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7,
		3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7,
		3 * var["dimension_fenetre"] // 4 + var["dimension_fenetre"] // 15 - 10,
		couleur='saddle brown',
		epaisseur = 10
	)
	ligne(
		var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7-5,
		3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7-5,
		3 * var["dimension_fenetre"] // 4 + var["dimension_fenetre"] // 16 + 30,
		couleur='saddle brown',
		epaisseur = 5
	)
	
	cercle(
		var["dimension_fenetre"] // 8,
		14 * var["dimension_fenetre"] // 15,
		var["dimension_fenetre"] // 14,
		couleur = 'LightSteelBlue2',
		remplissage = 'LightSteelBlue2'
	)
	cercle(
		var["dimension_fenetre"] // 7,
		14 * var["dimension_fenetre"] // 15,
		var["dimension_fenetre"] // 14,
		couleur = 'black',
		remplissage = 'black'
	)
	ligne(
		var["dimension_fenetre"] // 14,
		14 * var["dimension_fenetre"] // 15,
		var["dimension_fenetre"] // 5,
		14 * var["dimension_fenetre"] // 15,
		couleur='saddle brown',
		epaisseur = 5
	)
	ligne(
		var["dimension_fenetre"] // 14,
		14 * var["dimension_fenetre"] // 15 - 5,
		var["dimension_fenetre"] // 5 - 30,
		14 * var["dimension_fenetre"] // 15 - 5,
		couleur='saddle brown',
		epaisseur = 5
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

def loose(carte):
	if carte[var["pos_y"]-1][var["pos_x"]] == 'P':
		efface_tout()
		fond()
		personnage_defaitiste()
		texte(
			var["dimension_fenetre"] // 2,
			var["dimension_fenetre"] // 4,
			"DÉFAITE !",
			couleur="red",
			ancrage="center",
			taille=75
		)
		return True
	return False

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
		personnage_victorieux()
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
