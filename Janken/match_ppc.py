import getpass
import random


def demander_choix_humain(nom_joueur):
    correspondance = {"p": "pierre", "f": "feuille", "c": "ciseaux"}
    while True:
        choix = getpass.getpass(f"{nom_joueur}, choisis [p] / [f] / [c] : ").lower()
        if choix in correspondance:
            return correspondance[choix]
        print("Choix invalide. Tape p, f ou c.")


def ia_facile_ppc():
    return random.choice(["pierre", "feuille", "ciseaux"])


def choix_joueur_ppc(joueur):
    if joueur["type"] == "humain":
        return demander_choix_humain(joueur["nom"])

    choix = ia_facile_ppc()
    print(f"{joueur['nom']} choisit : {choix}")
    return choix


def resultat_manche_ppc(choix1, choix2):
    if choix1 == choix2:
        return 0

    gagne = {
        "pierre": "ciseaux",
        "ciseaux": "feuille",
        "feuille": "pierre"
    }

    if gagne[choix1] == choix2:
        return 1
    return 2


def jouer_match_ppc(j1, j2):
    """
    Retour :
    - "victoire_j1"
    - "victoire_j2"
    - "nul"
    """
    choix1 = choix_joueur_ppc(j1)
    choix2 = choix_joueur_ppc(j2)

    print(f"\n{j1['nom']} a joué : {choix1}")
    print(f"{j2['nom']} a joué : {choix2}")

    result = resultat_manche_ppc(choix1, choix2)

    if result == 0:
        print("Résultat : égalité")
        return "nul"
    if result == 1:
        print(f"Résultat : victoire de {j1['nom']}")
        return "victoire_j1"

    print(f"Résultat : victoire de {j2['nom']}")
    return "victoire_j2"