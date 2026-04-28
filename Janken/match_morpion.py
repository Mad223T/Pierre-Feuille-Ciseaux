import random


def afficher_grille(grille):
    print("\n")
    print(f" {grille[0]} | {grille[1]} | {grille[2]} ")
    print("---|---|---")
    print(f" {grille[3]} | {grille[4]} | {grille[5]} ")
    print("---|---|---")
    print(f" {grille[6]} | {grille[7]} | {grille[8]} ")
    print("\n")


def verifier_victoire(grille):
    combinaisons = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in combinaisons:
        if grille[a] != " " and grille[a] == grille[b] == grille[c]:
            return True
    return False


def verifier_nul(grille):
    return " " not in grille


def coups_possibles(grille):
    libres = []
    for i in range(9):
        if grille[i] == " ":
            libres.append(i)
    return libres


def ia_facile(grille):
    libres = coups_possibles(grille)
    return random.choice(libres)


def demander_coup_humain(grille, nom, symbole):
    while True:
        try:
            case = int(input(f"{nom} ({symbole}) - Choisis une case (1-9) : ")) - 1
        except ValueError:
            print("Erreur : Entrez un nombre de 1 à 9.")
            continue

        if case < 0 or case > 8:
            print("Erreur : Entrez un nombre de 1 à 9.")
            continue

        if grille[case] != " ":
            print("Erreur : case déjà prise.")
            continue

        return case


def choisir_coup(grille, joueur, symbole):
    if joueur["type"] == "humain":
        return demander_coup_humain(grille, joueur["nom"], symbole)

    case = ia_facile(grille)
    print(f"{joueur['nom']} ({symbole}) joue la case {case + 1}")
    return case


def jouer_match_morpion(j1, j2):
    """
    Retour :
    - "victoire_j1" si j1 gagne
    - "victoire_j2" si j2 gagne
    - "nul" si personne ne gagne
    """
    grille = [" "] * 9

    while True:
        # Tour de j1 (X)
        afficher_grille(grille)
        coup = choisir_coup(grille, j1, "X")
        grille[coup] = "X"

        if verifier_victoire(grille):
            afficher_grille(grille)
            return "victoire_j1"

        if verifier_nul(grille):
            afficher_grille(grille)
            return "nul"

        # Tour de j2 (O)
        afficher_grille(grille)
        coup = choisir_coup(grille, j2, "O")
        grille[coup] = "O"

        if verifier_victoire(grille):
            afficher_grille(grille)
            return "victoire_j2"

        if verifier_nul(grille):
            afficher_grille(grille)
            return "nul"