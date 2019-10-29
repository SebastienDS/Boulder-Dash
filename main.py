import fonction
from upemtk import *

from variable import var


def main():
    print(
        "Made by Uniiiiiifffffay corporation with the collaboration of Natsouuuuuu corporation!!! All right reserved!"
    )

    cree_fenetre(var["dimension_fenetre"], var["dimension_fenetre"])

    carte = fonction.creer_map("map1.txt")
    fonction.initialiser_partie(carte)
    while True:
    	efface_tout()
    	fonction.deplacer_perso(carte)
    	fonction.affichage(carte)
    	
    	mise_a_jour()
    	if var["pos_x"] == var["pos_sortie_x"] and var["pos_y"] == var["pos_sortie_y"]:
    		break

    attente_clic()
    ferme_fenetre()


if __name__ == "__main__":
    main()
