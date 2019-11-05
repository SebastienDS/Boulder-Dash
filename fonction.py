from upemtk import *
from variable import var
from random import choice


def creer_map(nomdufichier):
	'''Transforme un fichier texte contenant une map en une matriche'''
	with open("map/" + nomdufichier, "r") as fichier:    #ouvre le fichier contenant la carte
		contenu = fichier.read()					     #lis le fichier 
		contenu = contenu.split("\n")				     #Construit une matriche de la carte /chaque ligne = chaine de caractère
		contenu.pop(0)								     #Enlève le temps et nombre de diamands
		for i in range(len(contenu)):				   
			contenu[i] = list(contenu[i])			     #transforme la chaine de caractère en une list('abc'=['a','b','c'])
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
	#main à gauche
	cercle(
		x * var["taille_case"] + var["taille_case"] // 2 - var["taille_case"] // 4,
		y * var["taille_case"] + 3 * var["taille_case"] // 4 - var["taille_case"] // 8,
		var["taille_case"] // 12,
		couleur="lightpink",
		remplissage="lightpink",
	)
	#main à droite
	cercle(
		x * var["taille_case"] + var["taille_case"] // 2 + var["taille_case"] // 4,
		y * var["taille_case"] + 3 * var["taille_case"] // 4 - var["taille_case"] // 8,
		var["taille_case"] // 12,
		couleur="lightpink",
		remplissage="lightpink",
	)
	#pied à gauche
	cercle(
		x * var["taille_case"] + var["taille_case"] // 3,
		y * var["taille_case"] + 8 * var["taille_case"] // 9,
		var["taille_case"] // 12,
		couleur="black",
		remplissage="red",
	)
	#pied à droite
	cercle(
		x * var["taille_case"] + 2 * var["taille_case"] // 3,
		y * var["taille_case"] + 8 * var["taille_case"] // 9,
		var["taille_case"] // 12,
		couleur="black",
		remplissage="red",
	)
	#Tête
	cercle(
		x * var["taille_case"] + var["taille_case"] // 2,
		y * var["taille_case"] + 2 * var["taille_case"] // 3,
		var["taille_case"] // 4,
		couleur="black",
		remplissage="lightpink",
	)
	#Bouche(cercle + rectangle)
	cercle(
		x * var["taille_case"] + var["taille_case"] // 2,
		y * var["taille_case"] + 2 * var["taille_case"] // 3 + var["taille_case"] // 12,
		var["taille_case"] // 8,
		couleur="black",
		remplissage="black",
	)
	rectangle(
		x * var["taille_case"] + var["taille_case"] // 2 - var["taille_case"] // 8,
		y * var["taille_case"] + 2 * var["taille_case"] // 3 - var["taille_case"] // 12,
		x * var["taille_case"] + var["taille_case"] // 2 + var["taille_case"] // 8,
		y * var["taille_case"] + 2 * var["taille_case"] // 3 + var["taille_case"] // 12,
		couleur="lightpink",
		remplissage="lightpink",
	)
	#Oeil à droite
	cercle(
		x * var["taille_case"] + var["taille_case"] // 3 + var["taille_case"] // 20,
		y * var["taille_case"] + 2 * var["taille_case"] // 3 - var["taille_case"] // 20,
		var["taille_case"] // 20,
		couleur="black",
		remplissage="black",
	)
	#Oeil à gauche
	cercle(
		x * var["taille_case"] + 2 * var["taille_case"] // 3 - var["taille_case"] // 20,
		y * var["taille_case"] + 2 * var["taille_case"] // 3 - var["taille_case"] // 20,
		var["taille_case"] // 20,
		couleur="black",
		remplissage="black",
	)


def mur(x, y):
	"""Dessine un mur aux coordonnées x, y"""
	rectangle(  # fond
		x * var["taille_case"],
		y * var["taille_case"],
		var["taille_case"] + x * var["taille_case"],
		var["taille_case"] + y * var["taille_case"] - 1,
		couleur="gray15",
		remplissage="gray15",
	)
	ligne(  # deuxième ligne horizontale
		x * var["taille_case"],
		y * var["taille_case"] + var["taille_case"] // 3,
		var["taille_case"] + x * var["taille_case"],
		(var["taille_case"] + y * var["taille_case"] - 1) - 2 * var["taille_case"] // 3,
		couleur="white",
		epaisseur=var["taille_case"] // 25,
	)
	ligne(  # troisième ligne horizontale
		x * var["taille_case"],
		y * var["taille_case"] + 2 * var["taille_case"] // 3,
		var["taille_case"] + x * var["taille_case"],
		(var["taille_case"] + y * var["taille_case"] - 1) - var["taille_case"] // 3,
		couleur="white",
		epaisseur=var["taille_case"] // 25,
	)
	ligne(  # première ligne horitontale
		x * var["taille_case"],
		y * var["taille_case"],
		var["taille_case"] + x * var["taille_case"],
		(var["taille_case"] + y * var["taille_case"] - 1) - 3 * var["taille_case"] // 3,
		couleur="white",
		epaisseur=var["taille_case"] // 25,
	)
	ligne(  # quatrième ligne horizontale
		x * var["taille_case"],
		y * var["taille_case"] + 3 * var["taille_case"] // 3,
		var["taille_case"] + x * var["taille_case"],
		var["taille_case"] + y * var["taille_case"] - 1,
		couleur="white",
		epaisseur=var["taille_case"] // 25,
	)
	ligne(  # Première ligne verticale
		x * var["taille_case"] + 1 * var["taille_case"] // 4,
		y * var["taille_case"],
		x * var["taille_case"] + 1 * var["taille_case"] // 4,
		y * var["taille_case"] + var["taille_case"] // 3,
		couleur="white",
		epaisseur=var["taille_case"] // 25,
	)
	ligne(  # Deuxième ligne verticale
		x * var["taille_case"] + 1 * var["taille_case"] // 2,
		y * var["taille_case"] + var["taille_case"] // 3,
		x * var["taille_case"] + 1 * var["taille_case"] // 2,
		y * var["taille_case"] + 2 * var["taille_case"] // 3,
		couleur="white",
		epaisseur=var["taille_case"] // 25,
	)
	ligne(  # Troisième ligne verticale
		x * var["taille_case"] + 3 * var["taille_case"] // 4,
		y * var["taille_case"] + 2 * var["taille_case"] // 3,
		x * var["taille_case"] + 3 * var["taille_case"] // 4,
		y * var["taille_case"] + var["taille_case"],
		couleur="white",
		epaisseur=var["taille_case"] // 25,
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
	'''Ne fait rien(cas = ".")'''
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
			dico[carte[y][x]](x + (5 - var["pos_x"]), y + (5 - var["pos_y"])) #5= nbrcase//2 pour avoir perso au milieu


def fond():
	'''Affiche le fond'''
	rectangle(
		0,
		0,
		var["dimension_fenetre"],
		var["dimension_fenetre"] + 100,
		couleur="black",
		remplissage="black",
	)


def fond_victorieux():
	'''Affiche le fond en cas de victoire'''
	rectangle(
		0,
		0,
		var["dimension_fenetre"],
		var["dimension_fenetre"] + 100,
		couleur="cyan",
		remplissage="cyan",
	)

def fond_score(score):
	'''Affiche une banderolle avec le score'''
	rectangle(0, var["dimension_fenetre"], var["dimension_fenetre"], var["dimension_fenetre"] + 100, remplissage="black")
	texte(
		var["dimension_fenetre"] // 2,
		var["dimension_fenetre"] + 70,
		"Score:{}".format(score),
		couleur="white",
		ancrage="center",
		taille = 24,
		police = 'Impact'
	)

def personnage_victorieux():
	'''Affiche ce personnage en cas de victoire'''
	#Bouche(cercle + rectangle)
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
	#Main à gauche puis à droite
	cercle(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 4,
		3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="lightpink",
	)
	cercle(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 4,
		3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="lightpink",
	)
	# pied à gauche puis à droite
	cercle(
		var["dimension_fenetre"] // 3,
		8 * var["dimension_fenetre"] // 9,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="red",
	)
	cercle(
		2 * var["dimension_fenetre"] // 3,
		8 * var["dimension_fenetre"] // 9,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="red",
	)
	#Tête
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3,
		var["dimension_fenetre"] // 4,
		couleur="black",
		remplissage="lightpink",
	)
	#Bouche
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="black",
	)
	#6 prochaine = yeux(droite puis gauche)
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
	cercle(
		var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 20,
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 24,
		couleur="lightpink",
		remplissage="lightpink",
	)
	cercle(
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 24,
		couleur="lightpink",
		remplissage="lightpink",
	)
	rectangle(
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 10,
		2 * var["dimension_fenetre"] // 3,
		2 * var["dimension_fenetre"] // 3,
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 17,
		couleur="lightpink",
		remplissage="lightpink",
	)
	rectangle(
		var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 10,
		2 * var["dimension_fenetre"] // 3,
		var["dimension_fenetre"] // 3,
		2 * var["dimension_fenetre"] // 3 - var["dimension_fenetre"] // 17,
		couleur="lightpink",
		remplissage="lightpink",
	)


def personnage_defaitiste():
	#main puis pied(gauche puis droite)
	cercle(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 4,
		3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 12,
		couleur="lightpink",
		remplissage="lightpink",
	)
	cercle(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 4,
		3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 12,
		couleur="lightpink",
		remplissage="lightpink",
	)
	cercle(
		var["dimension_fenetre"] // 3,
		8 * var["dimension_fenetre"] // 9,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="red",
	)
	cercle(
		2 * var["dimension_fenetre"] // 3,
		8 * var["dimension_fenetre"] // 9,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="red",
	)
	#Tête
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3,
		var["dimension_fenetre"] // 4,
		couleur="black",
		remplissage="lightpink",
	)
	#Bouche
	cercle(
		var["dimension_fenetre"] // 2,
		2 * var["dimension_fenetre"] // 3 + var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 12,
		couleur="black",
		remplissage="black",
	)
	# 4 prochaines = yeux(gauche puis droite)
	ligne(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 2,
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
		couleur="black",
		epaisseur=10,
	)
	ligne(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2,
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
		couleur="black",
		epaisseur=10,
	)
	ligne(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 2,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
		couleur="black",
		epaisseur=10,
	)
	ligne(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 20,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 10,
		couleur="black",
		epaisseur=10,
	)
	#baton cassé main
	ligne(
		var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7,
		3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7,
		3 * var["dimension_fenetre"] // 4 + var["dimension_fenetre"] // 15 - 10,
		couleur="saddle brown",
		epaisseur=5,
	)
	ligne(
		var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7 - 5,
		3 * var["dimension_fenetre"] // 4 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 2 - 2 * var["dimension_fenetre"] // 7 - 5,
		3 * var["dimension_fenetre"] // 4 + var["dimension_fenetre"] // 15 + 30,
		couleur="saddle brown",
		epaisseur=5,
	)
	#Pioche 
	cercle(
		var["dimension_fenetre"] // 8,
		14 * var["dimension_fenetre"] // 15,
		var["dimension_fenetre"] // 14,
		couleur="LightSteelBlue2",
		remplissage="LightSteelBlue2",
	)
	cercle(
		var["dimension_fenetre"] // 7,
		14 * var["dimension_fenetre"] // 15,
		var["dimension_fenetre"] // 14,
		couleur="black",
		remplissage="black",
	)
	#baton au sol
	ligne(
		var["dimension_fenetre"] // 14,
		14 * var["dimension_fenetre"] // 15,
		var["dimension_fenetre"] // 5,
		14 * var["dimension_fenetre"] // 15,
		couleur="saddle brown",
		epaisseur=5,
	)
	ligne(
		var["dimension_fenetre"] // 14,
		14 * var["dimension_fenetre"] // 15 - 5,
		var["dimension_fenetre"] // 5 - 30,
		14 * var["dimension_fenetre"] // 15 - 5,
		couleur="saddle brown",
		epaisseur=5,
	)


def coffre():
	rectangle(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 10,
		couleur="gold",
		remplissage="gold",
	)
	rectangle(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 8,
		var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 10,
		couleur="gold",
		remplissage="gold",
	)
	rectangle(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 24,
		var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 24,
		var["dimension_fenetre"] // 10,
		couleur="gold",
		remplissage="gold",
	)
	rectangle(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 6,
		var["dimension_fenetre"] // 10,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 6,
		var["dimension_fenetre"] // 5,
		couleur="saddle brown",
		remplissage="saddle brown",
	)
	ligne(
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 10,
		var["dimension_fenetre"] // 2 + var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 5,
		couleur="black",
		epaisseur=10,
	)
	ligne(
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 10,
		var["dimension_fenetre"] // 2 - var["dimension_fenetre"] // 12,
		var["dimension_fenetre"] // 5,
		couleur="black",
		epaisseur=10,
	)
	ligne(
		2.75 * var["dimension_fenetre"] // 4,
		15,
		3 * var["dimension_fenetre"] // 5,
		var["dimension_fenetre"] // 14,
		couleur="gold",
		epaisseur=3,
	)
	ligne(
		3 * var["dimension_fenetre"] // 5,
		15,
		8 * var["dimension_fenetre"] // 15,
		var["dimension_fenetre"] // 14,
		couleur="gold",
		epaisseur=3,
	)
	ligne(
		1.5 * var["dimension_fenetre"] // 5,
		15,
		6 * var["dimension_fenetre"] // 15,
		var["dimension_fenetre"] // 14,
		couleur="gold",
		epaisseur=3,
	)
	ligne(
		2 * var["dimension_fenetre"] // 5,
		15,
		var["dimension_fenetre"] // 2,
		var["dimension_fenetre"] // 14,
		couleur="gold",
		epaisseur=3,
	)


def tomber_de_pierre(carte):
	"""Fais tomber les pierres"""
	for y in range(len(carte) -1):
		for x in range(len(carte[0])):
			if carte[y][x] == "P" and carte[y + 1][x] == ".":
				carte[y][x], carte[y + 1][x] = ".", "P"


def deplacer_perso(carte, nbdiamand, ev):
	"""Test si le perso peut se deplacer, si oui, deplace le perso sur la carte en fonction de la touche utilisé"""
	type_ev = type_evenement(ev)
	if type_ev == "Touche":
		t = touche(ev)
		if t == "Right" and carte[var["pos_y"]][var["pos_x"] + 1] in ["G", ".", "E"]:
			carte[var["pos_y"]][var["pos_x"] + 1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] += 1
		elif t == "Left" and carte[var["pos_y"]][var["pos_x"] - 1] in ["G", ".", "E"]:
			carte[var["pos_y"]][var["pos_x"] - 1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] -= 1
		elif t == "Up" and carte[var["pos_y"] - 1][var["pos_x"]] in ["G", ".", "E"]:
			carte[var["pos_y"] - 1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] -= 1
		elif t == "Down" and carte[var["pos_y"] + 1][var["pos_x"]] in ["G", ".", "E"]:
			carte[var["pos_y"] + 1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] += 1
		elif t == "Right" and carte[var["pos_y"]][var["pos_x"] + 1] in ["D"]:
			carte[var["pos_y"]][var["pos_x"] + 1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] += 1
			nbdiamand += 1
		elif t == "Left" and carte[var["pos_y"]][var["pos_x"] - 1] in ["D"]:
			carte[var["pos_y"]][var["pos_x"] - 1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] -= 1
			nbdiamand += 1
		elif t == "Up" and carte[var["pos_y"] - 1][var["pos_x"]] in ["D"]:
			carte[var["pos_y"] - 1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] -= 1
			nbdiamand += 1
		elif t == "Down" and carte[var["pos_y"] + 1][var["pos_x"]] in ["D"]:
			carte[var["pos_y"] + 1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] += 1
			nbdiamand += 1
	return nbdiamand


def pousser_pierre(carte, ev):
	"""Test si une pierre est poussable, si oui, la pousse"""
	type_ev = type_evenement(ev)
	if type_ev == "Touche":
		t = touche(ev)
		if t == "Right" and carte[var["pos_y"]][var["pos_x"] + 1] in ["P"] and carte[var["pos_y"]][var["pos_x"] + 2] in ["."]:
			carte[var["pos_y"]][var["pos_x"] + 1], carte[var["pos_y"]][var["pos_x"] + 2] = ".", "P"
		if t == "Left" and carte[var["pos_y"]][var["pos_x"] - 1] in ["P"] and carte[var["pos_y"]][var["pos_x"] - 2] in ["."]:
			carte[var["pos_y"]][var["pos_x"] - 1], carte[var["pos_y"]][var["pos_x"] - 2] = ".", "P"


def loose(carte):
	if carte[var["pos_y"] - 1][var["pos_x"]] == "P":
		efface_tout()
		fond()
		personnage_defaitiste()
		texte(
			var["dimension_fenetre"] // 2,
			var["dimension_fenetre"] // 4,
			"DÉFAITE !",
			couleur="red",
			ancrage="center",
			taille=75,
		)
		return True
	return False


def win():
	"""Regarde si l'utilisateur gagne"""
	if var["pos_x"] == var["pos_sortie_x"] and var["pos_y"] == var["pos_sortie_y"]:
		efface_tout()
		fond_victorieux()
		texte(
			var["dimension_fenetre"] // 2,
			var["dimension_fenetre"] // 3,
			"Victoire !",
			couleur="black",
			ancrage="center",
			taille=75,
		)
		personnage_victorieux()
		coffre()
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


def debug(carte, nbdiamand):
	"""Perso joue aléatoirement"""
	while True:
		x = choice(["Up", "Down", "Left", "Right"])
		if x == "Right" and carte[var["pos_y"]][var["pos_x"] + 1] in ["D"]:
			carte[var["pos_y"]][var["pos_x"] + 1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] += 1
			nbdiamand += 1
			return nbdiamand
		elif x == "Left" and carte[var["pos_y"]][var["pos_x"] - 1] in ["D"]:
			carte[var["pos_y"]][var["pos_x"] - 1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] -= 1
			nbdiamand += 1
			return nbdiamand
		elif x == "Up" and carte[var["pos_y"] - 1][var["pos_x"]] in ["D"]:
			carte[var["pos_y"] - 1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] -= 1
			nbdiamand += 1
			return nbdiamand
		elif x == "Down" and carte[var["pos_y"] + 1][var["pos_x"]] in ["D"]:
			carte[var["pos_y"] + 1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] += 1
			nbdiamand += 1
			return nbdiamand
		elif x == "Right" and carte[var["pos_y"]][var["pos_x"] + 1] in ["G", ".", "E"]:
			carte[var["pos_y"]][var["pos_x"] + 1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] += 1
			return nbdiamand
		elif x == "Left" and carte[var["pos_y"]][var["pos_x"] - 1] in ["G", ".", "E"]:
			carte[var["pos_y"]][var["pos_x"] - 1] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_x"] -= 1
			return nbdiamand
		elif x == "Up" and carte[var["pos_y"] - 1][var["pos_x"]] in ["G", ".", "E"]:
			carte[var["pos_y"] - 1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] -= 1
			return nbdiamand
		elif x == "Down" and carte[var["pos_y"] + 1][var["pos_x"]] in ["G", ".", "E"]:
			carte[var["pos_y"] + 1][var["pos_x"]] = "R"
			carte[var["pos_y"]][var["pos_x"]] = "."
			var["pos_y"] += 1
			return nbdiamand


def encadrement(
	msg, x, y, couleurTXT, couleurCadre, Taille, Epaisseur, Espacement
):  # Ecrit et encadre un texte puis donne les coordonnées du cadre (pour clic)
	texte(10000000, y, msg, couleur=couleurTXT, police="Impact", taille=Taille)
	x2 = x + longueur_texte(msg) + Espacement
	y2 = y + hauteur_texte() + Espacement
	texte(x, y, msg, couleur=couleurTXT, police="Impact", taille=Taille)
	rectangle(
		x - Espacement,
		y - Espacement,
		x2,
		y2,
		couleur=couleurCadre,
		epaisseur=Epaisseur,
	)
	return [x - Espacement, y - Espacement, x2, y2]


def quitte_or_retry(a, coordretry, coordquitte):
	if (
		a[0] < coordretry[2]
		and a[0] > coordretry[0]
		and a[1] < coordretry[3]
		and a[1] > coordretry[1]
	):
		return 2
	if (
		a[0] < coordquitte[2]
		and a[0] > coordquitte[0]
		and a[1] < coordquitte[3]
		and a[1] > coordquitte[1]
	):
		return 1
	return 0


if __name__ == "__main__":
	import doctest

	doctest.testmod()
