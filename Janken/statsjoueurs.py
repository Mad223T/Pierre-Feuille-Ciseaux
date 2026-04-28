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


def afficher_liste_joueurs(joueurs):
    print("\nListe des joueurs :")
    for i, joueur in enumerate(joueurs, start=1):
        print(i, ".", joueur["nom"])


def choisir_joueur(joueurs):
    while True:
        try:
            print("\n" + "-" * 50)
            choix = int(input("\nChoisissez un joueur : "))
            print("\n" + "-" * 50)
            if 1 <= choix <= len(joueurs):
                return joueurs[choix - 1]
            print("\nChoix invalide, veuillez réessayer.")
        except ValueError:
            print("\nVeuillez entrer un nombre.")


def calculer_stats(joueur):
    parties = 0
    victoires = 0
    defaites = 0
    adversaires_battus = []

    for match in joueur.get("historique", []):
        parties += 1

        if match.get("resultat") == "victoire":
            victoires += 1
            adversaires_battus.append(match.get("adversaire"))
        elif match.get("resultat") == "defaite":
            defaites += 1

    return parties, victoires, defaites, adversaires_battus


def afficher_stats(joueur, parties, victoires, defaites, adversaires):
    print("\nStatistiques de", joueur["nom"])
    print("Type :", joueur.get("type"))
    print("ELO actuel :", joueur.get("elo"))

    print("\nParties jouées :", parties)
    print("Victoires :", victoires)
    print("Défaites :", defaites)

    if parties > 0:
        ratio = (victoires / parties) * 100
        print("Ratio de victoires :", int(ratio), "%")
    else:
        print("Ratio de victoires : N/A")

    if victoires > 0:
        print("\nAdversaires battus :")
        for nom in adversaires:
            if nom:
                print("-", nom)
    else:
        print("\nAucun adversaire battu pour le moment.")


def stats_joueurs():
    print("5- Statistiques des joueurs")
    print("\nAffichage des statistiques...\n")

    joueurs = charger_joueurs()
    if not verifier_joueurs(joueurs):
        input("\nAppuyez sur Entrée pour revenir au menu...")
        return

    afficher_liste_joueurs(joueurs)
    joueur = choisir_joueur(joueurs)

    parties, victoires, defaites, adversaires = calculer_stats(joueur)
    afficher_stats(joueur, parties, victoires, defaites, adversaires)

    input("\nTapez Entrée pour revenir au menu principal...")