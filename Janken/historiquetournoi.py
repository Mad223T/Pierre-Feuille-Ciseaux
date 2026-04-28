import json


def charger_historique():
    try:
        with open("historique_tournois.json", "r") as fichier:
            return json.load(fichier)
    except:
        return []


def tournois_termines(historique):
    resultat = []
    for tournoi in historique:
        if tournoi.get("termine") is True:
            resultat.append(tournoi)
    return resultat


def verifier_historique(tournois):
    if len(tournois) == 0:
        print("\nAucun tournoi terminé pour le moment.\n")
        return False
    return True


def afficher_liste_historique(tournois):
    print("\nHistorique des tournois : ")

    numero = 1
    for tournoi in tournois:
        print(numero, ".", tournoi["nom"], "(" + tournoi["jeu"] + " - " + tournoi["format"] + ")")
        numero += 1


def demander_details():
    while True:
        print("\n" + "-" * 50)
        choix = input("\nSouhaitez-vous consulter les détails d'un tournoi ? (o/n) : ").strip().lower()
        print("\n" + "-" * 50)
        if choix in ("o", "n"):
            return choix == "o"
        print("\nChoix invalide. Tape o ou n.")


def choisir_tournoi_historique(tournois):
    while True:
        try:
            print("\n" + "-" * 50)
            choix = int(input("\nEntrez le numéro du tournoi : "))
            print("\n" + "-" * 50)
            if 1 <= choix <= len(tournois):
                return tournois[choix - 1]
            print("\nChoix invalide. Veuillez réessayer.")
        except ValueError:
            print("\nVeuillez entrer un nombre.")


def afficher_details_tournoi(tournoi):
    print("\nDétails du tournoi :\n")
    print("Nom du tournoi :", tournoi["nom"])
    print("Jeu :", tournoi["jeu"])
    print("Format :", tournoi["format"])
    print("Nombre de joueurs :", len(tournoi["participants"]))
    print("\nMatchs :")

    for match in tournoi.get("matchs", []):
        print(match["joueur1"], "vs", match["joueur2"], "- Résultat :", match.get("resultat"))


def historique_tournoi():
    print("3- Historique des tournois")
    print("\nAffichage de l'historique des tournois...")

    historique = charger_historique()
    termines = tournois_termines(historique)

    if not verifier_historique(termines):
        input("Appuyez sur Entrée pour revenir au menu...")
        return

    afficher_liste_historique(termines)

    if demander_details():
        tournoi = choisir_tournoi_historique(termines)
        afficher_details_tournoi(tournoi)

    input("\nAppuyez sur Entrée pour revenir au menu principal...")