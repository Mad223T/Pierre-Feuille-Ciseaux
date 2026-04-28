import json
from datetime import datetime


def initialiser_tournoi():
    return {
        "nom": "",
        "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "jeu": "",
        "format": "",
        "nb_joueurs": 0,
        "participants": [],
        "matchs": [],
        "index_match_actuel": 0,
        "termine": False
    }


def choisir_jeu():
    while True:
        try:
            print("\nChoisissez le jeu pour le tournoi :\n")
            print("1- Pierre-Papier-Ciseaux")
            print("2- Morpion")
            print("\n" + "-" * 50)
            choix_jeu = int(input("\nEntrez le numéro du jeu (1 ou 2) : "))

            if choix_jeu == 1:
                return "ppc"
            elif choix_jeu == 2:
                return "morpion"
            else:
                print("\nChoix invalide. Veuillez réessayer.")
        except ValueError:
            print("\nEntrée invalide. Veuillez entrer un numéro.")


def choisir_format():
    while True:
        try:
            print("\nChoisissez le format du tournoi :\n")
            print("1- Round Robin")
            print("Explications: Tout le monde affronte tout le monde.")
            print("\n2- Élimination directe")
            print("Explications: Si tu perds un match, tu quittes le tournoi.")
            print("\n" + "-" * 50)

            choix_format = int(input("\nEntrez le numéro du format (1 ou 2) : "))
            if choix_format == 1:
                return "round_robin"
            elif choix_format == 2:
                return "elimination"
            else:
                print("\nChoix invalide. Veuillez réessayer.")
        except ValueError:
            print("\nEntrée invalide. Veuillez entrer un numéro.")


def choisir_nmbr_joueurs(format_du_tournoi):
    while True:
        try:
            print("\nChoisissez le nombre de joueurs pour votre tournoi")
            print("\nRemarque:")
            print("Pour Round-Robin : minimum 2 joueurs.")
            print("Pour élimination directe : 4, 8 ou 16 joueurs.")
            print("\n" + "-" * 50)

            nb = int(input("\nNombre de joueurs : "))

            if format_du_tournoi == "elimination":
                if nb in (4, 8, 16):
                    return nb
                print("\nErreur : en élimination directe, le nombre doit être 4, 8 ou 16.")
            elif format_du_tournoi == "round_robin":
                if nb >= 2:
                    return nb
                print("\nErreur : en round robin, il faut minimum 2 joueurs.")
            else:
                print("\nErreur interne : format non reconnu.")
        except ValueError:
            print("\nErreur : Veuillez entrer un nombre valide.")


def creer_joueur(nom_joueur, type_joueur):
    return {
        "nom": nom_joueur,
        "type": type_joueur,        # "humain" ou "ia"
        "elo": 1000,
        "historique": []
    }


def ajouter_des_participants(nb_joueurs):
    participants = []

    for i in range(nb_joueurs):
        while True:
            try:
                print("\n" + "-" * 50)
                nom = input(f"\nNom du joueur {i + 1} : ").strip()
                print("\n" + "-" * 50)

                if not nom or nom in [p["nom"] for p in participants]:
                    print("\nNom invalide ou déjà utilisé.")
                    continue

                print("\nChoisissez le type de ce joueur")
                print("1. Humain")
                print("2. IA")
                print("\n" + "-" * 50)

                choix_type = int(input("\nType : "))
                if choix_type == 1:
                    type_joueur = "humain"
                elif choix_type == 2:
                    type_joueur = "ia"
                else:
                    print("\nType invalide.")
                    continue

                participants.append(creer_joueur(nom, type_joueur))
                break

            except ValueError:
                print("\nEntrée invalide.")

    return participants


def sauvegarder_participants_dans_joueurs_json(participants):
    # Charge les joueurs existants
    try:
        with open("joueurs.json", "r") as f:
            joueurs_existants = json.load(f)
    except:
        joueurs_existants = []

    noms_existants = [j["nom"] for j in joueurs_existants]

    # Ajoute seulement ceux qui n'existent pas déjà
    for p in participants:
        if p["nom"] not in noms_existants:
            joueurs_existants.append(p)
            noms_existants.append(p["nom"])

    # Sauvegarde
    try:
        with open("joueurs.json", "w") as f:
            json.dump(joueurs_existants, f, indent=4)
    except:
        pass


def creer_tournoi():
    """
    Crée un tournoi et retourne le dictionnaire complet.
    """
    print("1- Créer un tournoi")
    print("\nCréation d'un nouveau tournoi...")
    tournoi = initialiser_tournoi()

    print("\n" + "-" * 50)
    tournoi["nom"] = input("\nNom du tournoi : ").strip()

    print("\n" + "-" * 50)
    tournoi["jeu"] = choisir_jeu()

    print("\n" + "-" * 50)
    tournoi["format"] = choisir_format()

    print("\n" + "-" * 50)
    tournoi["nb_joueurs"] = choisir_nmbr_joueurs(tournoi["format"])

    tournoi["participants"] = ajouter_des_participants(tournoi["nb_joueurs"])

    # Sauvegarde participants dans joueurs.json 
    sauvegarder_participants_dans_joueurs_json(tournoi["participants"])

    tournoi["matchs"] = []
    tournoi["index_match_actuel"] = 0
    tournoi["termine"] = False

    print("\nTournoi créé avec succès !\n")
    return tournoi