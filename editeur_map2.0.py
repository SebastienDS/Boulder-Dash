import pygame
import sys



class editeur_map:
	def __init__(self, taille_fenetre, w_map, h_map):
		pygame.init()
		self.ecran = pygame.display.set_mode(taille_fenetre)
		self.w_map = w_map +1
		self.h_map = h_map +1
		self.taille = int(min(taille_fenetre) / max([w_map, h_map]))
		self.carte = [['.' for i in range(self.w_map)] for i in range(self.h_map)]

		self.dico = {
			"G": lambda x, y: self.rectangle(x * self.taille, y * self.taille, (128,64,64)),  # carre marron
			"P": lambda x, y: self.rectangle(x * self.taille, y * self.taille, (128,128,128)),  # rond gris
			"R": lambda x, y: self.rectangle(x * self.taille, y * self.taille, (255,0,128)),  # rond blanc				
			"W": lambda x, y: self.rectangle(x * self.taille, y * self.taille, (0,0,0)),  # carre noir
			"D": lambda x, y: self.rectangle(x * self.taille, y * self.taille, (0,128,192)),  # carre bleu
			"E": lambda x, y: self.rectangle(x * self.taille, y * self.taille, (0,255,0)),  # carre vert
			".": lambda x, y: self.rectangle(x * self.taille, y * self.taille, (192,192,192)), #rien
		}
		self.key = {
			str(pygame.K_g): "G",
			str(pygame.K_p): "P",
			str(pygame.K_r): "R",
			str(pygame.K_z): "W",
			str(pygame.K_d): "D",
			str(pygame.K_e): "E"
		}

		self.element = "."

	def rectangle(self, x, y, couleur):
		pygame.draw.rect(self.ecran, couleur, [x, y, self.taille, self.taille])

	def affiche_map(self):
		for j in range(self.h_map - 1):
			for i in range(self.w_map - 1):
				self.dico[self.carte[j][i]](i, j)

	def poser_element(self, pos):
		self.carte[pos[1] // self.taille][pos[0] // self.taille] = self.element

	def set_element(self, elem):
		if elem in self.dico:
			self.element = elem
		else:
			print("l'element n'est pas dans le dico")


	def save(self):
		file_name = input("Nom map: ")
		temps = input("temps limite: ")
		diamand = input("diamand requis pour gagner: ")
		with open("map/" + file_name + ".txt", "w") as f:
			f.write(temps + "s " + diamand + "d\n")
			for j in range(self.h_map - 1):
				for i in range(self.w_map - 1):
					f.write(self.carte[j][i])
				f.write("\n")
		print("Map saved")


def main():
	editeur = editeur_map((800, 700), int(sys.argv[1]), int(sys.argv[2]))
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					editeur.poser_element(event.pos)
				elif event.button == 3:
					editeur.set_element(".")
					editeur.poser_element(event.pos)

			elif event.type == pygame.KEYDOWN:
				if str(event.key) in editeur.key:
					editeur.set_element(editeur.key[str(event.key)])
				elif event.key == pygame.K_ESCAPE:
					editeur.save()

		editeur.ecran.fill((255,255,255))
		editeur.affiche_map()
		pygame.display.flip()


if __name__ == '__main__':
	main()

