import fonction
from upemtk import *

from variable import var


def main():
    print(
        "Made by Uniiiiiifffffay corporation with the collaboration of Natsouuuuuu corporation!!! All right reserved!"
    )

    cree_fenetre(var["dimension_fenetre"], var["dimension_fenetre"])

    carte = fonction.creer_map("map1.txt")
    fonction.affichage(carte)

    attente_clic()
    ferme_fenetre()


if __name__ == "__main__":
    main()
