import upemtk
from variable import var
from fonction import dico, my_input
import esthetique
import os



def affiche_map(carte):
    esthetique.fond("white")
    upemtk.rectangle(
        0,
        0,
        var["w_map"] * var["taille_case"],
        var["h_map"] * var["taille_case"],
        remplissage="black",
    )
    for j in range(var["h_map"]):
        for i in range(var["w_map"]):
            dico[carte[j][i]](i, j, var["taille_case"], 0, 0)


def affiche_tools(tools):
    for i, elem in enumerate(tools):
        dico[elem](i, 6, var["bandeau"], 0, 0)


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
        reponse = test_input("Nom déjà utilisé\n      Ecraser ?", "str")
        if reponse.lower() in {"oui", "y", "o", "yes", "ye", "ui", "certainement", "absolument"}:
            save_map(carte, file_name, temps, diamand)
        else:
            test_input("Map non enregistrée", "str")


def main():
    taille_fen = (var["dimension_fenetre"], var["dimension_fenetre"] + var["bandeau"])
    tools = ["G", "P", "W", "D", "R", "E"]
    upemtk.cree_fenetre(taille_fen[0], taille_fen[1])

    esthetique.fond("black")
    var["w_map"] = my_input("Nombre de colonnes:", "int")
    var["h_map"] = my_input("Nombre de lignes:", "int")

    var["taille_case"] = int(min(taille_fen) / max([var["w_map"], var["h_map"]]))
    carte = [["." for i in range(var["w_map"])] for i in range(var["h_map"])]
    element = "."

    while True:
        upemtk.efface_tout()
        affiche_map(carte)
        affiche_tools(tools)

        upemtk.mise_a_jour()
        ev = upemtk.attente_clic_ou_touche()

        if ev[2] == "ClicGauche":
            x = ev[0] // var["taille_case"]
            y = ev[1] // var["taille_case"]

            if x < var["w_map"] and y < var["h_map"]:
                carte[y][x] = element
            elif ev[1] // var["bandeau"] == 6:
                element = tools[ev[0] // var["bandeau"]]

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


if __name__ == "__main__":
    main()
