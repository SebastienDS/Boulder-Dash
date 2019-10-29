import fonction
from upemtk import *

dimension_fenetre = 800
nb_cases = 10
assert dimension_fenetre % nb_cases == 0
taille_case = dimension_fenetre // nb_cases


def main():
    print(
        "Made by Uniiiiiifffffay corporation with the collaboration of Natsouuuuuu corporation!!! All right reserved!"
    )


if __name__ == "__main__":
    main()
    cree_fenetre(dimension_fenetre, dimension_fenetre)
    fonction.sortie(0, 0, taille_case)
    fonction.mur(9, 9, taille_case)
    attente_clic()
