import fonction
from upemtk import *
from variable import var


def main():
    print(
        "Made by Uniiiiiifffffay corporation with the collaboration of Natsouuuuuu corporation!!! All right reserved!"
    )
    cree_fenetre(var["dimension_fenetre"], var["dimension_fenetre"])
    fonction.terre(0, 0)
    fonction.pierre(1, 1)
    fonction.rockford(2, 2)
    attente_clic()
    ferme_fenetre()


if __name__ == "__main__":
    main()
