var = {
    "dimension_fenetre": 600,
    "nb_cases": 10,
    "bandeau": 100,
    "debug": "d",
    "porte": 1,
    "lumiere": False,
    "pathfinding": False,
    "personnage": None,  # mettre None ou False pour avoir kirby
}

var["taille_case"] = var["dimension_fenetre"] // var["nb_cases"]


_touche = {
	"Right": (1, 0), 
	"Left": (-1, 0), 
	"Up": (0, -1), 
	"Down": (0, 1)
}
