import json


def charger_joueurs():
    try:
        with open("joueurs.json", "r") as fichier:
            return json.load(fichier)
    except:
        return []


def verifier_joueurs(joueurs):
    if len(joueurs) == 0:
        print("\nAucun joueur enregistré pour le moment.")
        return False
    return True


def trier_joueurs_par_elo(joueurs):
    joueurs_tries = joueurs.copy()
    joueurs_tries.sort(key=lambda joueur: joueur.get("elo", 1000), reverse=True)
    return joueurs_tries


def afficher_classement(joueurs):
    print("\nClassement ELO des joueurs :")
    for rang, joueur in enumerate(joueurs, start=1):
        print(rang, ".", joueur["nom"], "(" + joueur.get("type", "?") + ")", "- ELO :", joueur.get("elo", 1000))


def classement_elo():
    print("4- Classement ELO")
    print("\nAffichage du classement ELO...")

    joueurs = charger_joueurs()
    if not verifier_joueurs(joueurs):
        input("\nAppuyez sur Entrée pour revenir au menu...")
        return

    joueurs_tries = trier_joueurs_par_elo(joueurs)
    afficher_classement(joueurs_tries)

    input("\nAppuyez sur Entrée pour revenir au menu principal...")