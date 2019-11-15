import upemtk
from variable import var
import esthetique


def rien(*_):
	pass


dico = {
    "G": esthetique.terre,  # carre marron
    "P": esthetique.pierre,  # rond gris
    "R": esthetique.rockford,  # rond blanc
    "W": esthetique.mur,  # carre noir
    "D": esthetique.diamand,  # carre bleu
    "E": esthetique.sortie,  # carre vert
    ".": rien,
    "P1": esthetique.pierre_eboulement,
    "D1": esthetique.diamand_eboulement,
    "F": esthetique.mur
}


def affiche_map(carte, w_map, h_map):
	esthetique.fond("black")
	for j in range(h_map):
		for i in range(w_map):
			dico[carte[j][i]](i, j)


def save(carte, w_map, h_map):
	file_name = input("Name map: ")
	temps = input("temps limite: ")
	diamand = input("diamand requis pour gagner: ")
	with open("map/" + file_name + ".txt", "w") as f:
		f.write(temps + "s " + diamand + "d\n")
		for j in range(h_map - 1):
			for i in range(w_map - 1):
				f.write(carte[j][i])
			f.write("\n")
	print("Map saved")


def my_input(msg):
	texte = ""
	while True:
		ev = upemtk.donne_evenement()
		if upemtk.type_evenement(ev) == "Touche":
			x = upemtk.touche(ev)  
			if x == "Return":
				print(texte)
				return texte

			elif x == "BackSpace":
				texte = texte[:-1]

			elif len(x) == 1 and len(texte) <= 18:
				texte += x
	
		upemtk.efface("texte_input")
		upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2, texte, couleur="blue", ancrage="center", tag="texte_input")
		upemtk.mise_a_jour()


def test_input(msg, type_retour):
	while True:
		upemtk.rectangle(
			var["dimension_fenetre"] // 2 - 180,
			var["dimension_fenetre"] // 2 - 100,
			var["dimension_fenetre"] // 2 + 180,
			var["dimension_fenetre"] // 2 + 100,
			couleur="white",
			epaisseur=3
		)
		upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2 - 75, msg, couleur="white", ancrage="center", tag="msg")
		_var = my_input(msg)
		if type_retour == "int":
			if _var.isdigit():
				if int(_var) <= 100 and int(_var) > 0:
					upemtk.efface("msg")
					upemtk.efface("msg_erreur")
					upemtk.efface("texte_input")
					return int(_var)
				elif int(_var) == 0:
					upemtk.efface("msg_erreur")
					upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2 + 75, "Valeur trop petite", couleur="red", ancrage="center", tag="msg_erreur")
				else:
					upemtk.efface("msg_erreur")
					upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2 + 75, "Valeur trop grande", couleur="red", ancrage="center", tag="msg_erreur")
			else:
				upemtk.efface("msg_erreur")
				upemtk.texte(var["dimension_fenetre"] // 2, var["dimension_fenetre"] // 2 + 75, "Valeur entiere requis", couleur="red", ancrage="center", tag="msg_erreur")
		else:
			return var 


def main():
	taille_fen = (var["dimension_fenetre"], var["dimension_fenetre"])
	upemtk.cree_fenetre(taille_fen[0], taille_fen[1])

	esthetique.fond("black")
	w_map = test_input("Nombre de colonnes:", "int")
	h_map = test_input("Nombre de lignes:", "int")
	
	var["taille_case"] = int(min(taille_fen) / max([w_map, h_map]))
	carte = [['.' for i in range(w_map)] for i in range(h_map)]
	element = "."

	
	while True:
		affiche_map(carte, w_map, h_map)
		upemtk.mise_a_jour()
		ev = upemtk.attente_clic_ou_touche()
		upemtk.efface_tout()

		print(ev)

		if ev[2] == "ClicGauche":
			print(carte)
			carte[ev[1] // var["taille_case"]][ev[0] // var["taille_case"]] = element
			
		elif ev[2] == "Touche":  
			if ev[1].upper() in dico:
				element = ev[1].upper()
				print(element)
			elif ev[1] == "Escape":
				save(carte, w_map, h_map)
				break
			elif ev[1] == "space":
				break
				upemtk.ferme_fenetre()

		elif ev[2] == "ClicDroit":
			carte[ev[1] // var["taille_case"]][ev[0] // var["taille_case"]] = "."

	upemtk.attente_clic()
	upemtk.ferme_fenetre()


if __name__ == '__main__':
	main()

