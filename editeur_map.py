import upemtk

w_map = 10
h_map = 10
taille_fen = (800, 700)
t = int(min(taille_fen) / max([w_map, h_map]))

dico = {
	"G": lambda x, y: upemtk.rectangle(x * t, y * t, x * t + t - 1, y * t + t - 1, "sienna4", "sienna4"),  # carre marron
	"P": lambda x, y: upemtk.rectangle(x * t, y * t, x * t + t - 1, y * t + t - 1, "grey", "grey"),  # rond gris
	"R": lambda x, y: upemtk.rectangle(x * t, y * t, x * t + t - 1, y * t + t - 1, "pink", "pink"),  # rond blanc
	"W": lambda x, y: upemtk.rectangle(x * t, y * t, x * t + t - 1, y * t + t - 1, "black", "black"),  # carre noir
	"D": lambda x, y: upemtk.rectangle(x * t, y * t, x * t + t - 1, y * t + t - 1, "blue", "blue"),  # carre bleu
	"E": lambda x, y: upemtk.rectangle(x * t, y * t, x * t + t - 1, y * t + t - 1, "green", "green"),  # carre vert
	".": lambda x, y: upemtk.rectangle(x * t, y * t, x * t + t - 1, y * t + t - 1, "white", "white"), #rien
}
carte = [['.' for i in range(w_map)] for i in range(h_map)]

def affiche_map(carte):
	for j in range(h_map - 1):
		for i in range(w_map - 1):
			dico[carte[j][i]](i, j)

def save(carte):
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

def main():
	upemtk.cree_fenetre(taille_fen[0], taille_fen[1])
	element = "."


	while True:
		ev = upemtk.donne_evenement()
		type_ev = upemtk.type_evenement(ev)
		if type_ev == "ClicGauche":
			carte[upemtk.clic_y(ev) // t][upemtk.clic_x(ev) // t] = element
			
		elif type_ev == "Touche":
			touche = upemtk.touche(ev)  
			if touche.upper() in dico:
				element = touche.upper()
				print(element)
			elif touche == "Escape":
				save(carte)
				break

		elif type_ev == "ClicDroit":
			carte[upemtk.clic_y(ev) // t][upemtk.clic_x(ev) // t] = "."


		affiche_map(carte)
		upemtk.mise_a_jour()

	affiche_map(carte)
	upemtk.mise_a_jour()
	upemtk.attente_clic()
	upemtk.ferme_fenetre()


if __name__ == '__main__':
	main()

