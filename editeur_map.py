import upemtk
from variable import var
import esthetique
import os


def rien(*args):
	pass


dico = {
    "G": esthetique.terre,  
    "P": esthetique.pierre,  
    "R": esthetique.rockford,  
    "W": esthetique.mur,  
    "D": esthetique.diamand,  
    "E": esthetique.sortie,  
    ".": rien,
    "P1": esthetique.pierre_eboulement,
    "D1": esthetique.diamand_eboulement,
    "F": esthetique.mur
}


def affiche_map(carte):
	esthetique.fond("black")
	for j in range(var["h_map"]):
		for i in range(var["w_map"]):
			dico[carte[j][i]](i, j, 0, 0)


def save_map(carte, file_name, temps, diamand):
	with open("map/{}.txt".format(file_name), "w") as f:
		f.write("{}s {}d\n".format(temps, diamand))
		for j in range(var["h_map"]):
			for i in range(var["w_map"]):
				f.write(carte[j][i])
			f.write("\n")
	test_input("Map sauvegardée", "str")


def save(carte):
	file_name = test_input("Nom de la map:", "str")
	temps = test_input("temps limite:", "int")
	diamand = test_input("diamand requis:", "int")

	if not os.path.isfile("map/{}.txt".format(file_name)):
		save_map(carte, file_name, temps, diamand)
	else:
		test_input("Nom déjà utilisé", "str")
		reponse = test_input("Ecraser ?", "str")
		if reponse.lower() in {"oui", "y", "o", "yes"}:
			save_map(carte, file_name, temps, diamand)
		else:
			test_input("Map non enregistrée", "str")


def my_input(msg):
	texte = ""
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
		elif type_ev == "ClicGauche":
			return texte
	
		upemtk.efface("texte_input")
		upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2, texte, couleur="white", ancrage="center", tag="texte_input")
		upemtk.mise_a_jour()


def test_input(msg, type_retour):
	upemtk.rectangle(
		var["dimension_fenetre"] // 2 - 180,
		var["dimension_fenetre"] // 2 - 100,
		var["dimension_fenetre"] // 2 + 180,
		var["dimension_fenetre"] // 2 + 100,
		couleur="gray28",
		remplissage="gray",
		epaisseur=5,
		tag="cadre"
	)

	while True:
		upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2 - 75, msg, couleur="white", ancrage="center", tag="msg")
		_var = my_input(msg)
		if type_retour == "int":
			if _var.isdigit():
				if int(_var) <= 100 and int(_var) > 0:
					upemtk.efface("msg")
					upemtk.efface("msg_erreur")
					upemtk.efface("texte_input")
					upemtk.efface("cadre")
					return int(_var)
				elif int(_var) == 0:
					upemtk.efface("msg_erreur")
					upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2 + 75, "Valeur trop petite", couleur="red", ancrage="center", police="impact", tag="msg_erreur")
				else:
					upemtk.efface("msg_erreur")
					upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2 + 75, "Valeur trop grande", couleur="red", ancrage="center", police="impact", tag="msg_erreur")
			else:
				upemtk.efface("msg_erreur")
				upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2 + 75, "Valeur entiere requis", couleur="red", ancrage="center", police="impact", tag="msg_erreur")
		else:
			upemtk.efface("msg")
			upemtk.efface("msg_erreur")
			upemtk.efface("texte_input")
			upemtk.efface("cadre")
			return _var 


def main():
	taille_fen = (var["dimension_fenetre"], var["dimension_fenetre"] + 100)
	upemtk.cree_fenetre(taille_fen[0], taille_fen[1])

	esthetique.fond("black")
	var["w_map"] = test_input("Nombre de colonnes:", "int")
	var["h_map"] = test_input("Nombre de lignes:", "int")
	
	var["taille_case"] = int(min(taille_fen) / max([var["w_map"], var["h_map"]]))
	carte = [['.' for i in range(var["w_map"])] for i in range(var["h_map"])]
	element = "."

	
	while True:
		upemtk.efface_tout()
		affiche_map(carte)
		upemtk.mise_a_jour()
		ev = upemtk.attente_clic_ou_touche()

		if ev[2] == "ClicGauche":
			carte[ev[1] // var["taille_case"]][ev[0] // var["taille_case"]] = element
			
		elif ev[2] == "Touche":  
			if ev[1].upper() in dico:
				element = ev[1].upper()
			elif ev[1] == "Escape":
				save(carte)
			elif ev[1] == "space":
				break
				upemtk.ferme_fenetre()

		elif ev[2] == "ClicDroit":
			carte[ev[1] // var["taille_case"]][ev[0] // var["taille_case"]] = "."

	upemtk.attente_clic()
	upemtk.ferme_fenetre()


if __name__ == '__main__':
	main()

