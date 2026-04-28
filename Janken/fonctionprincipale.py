from creertournoi import creer_tournoi
from classementelo import classement_elo
from statsjoueurs import stats_joueurs
from règles import regles

from tournoi_engine import (
    initialiser_fichiers_si_absents,
    ajouter_tournoi_en_cours,
    lancer_tournoi,
    reprendre_tournoi,
    afficher_historique_tournois
)

print("\n" + "=" * 50)
print(" " * 22 + "Janken")
print("=" * 50 + "\n")
print(" " * 16 + "Welcome to Janken !")


def afficher_menu():
    print("\n" + "=" * 50)
    print("=" + " " * 22 + "MENU" + " " * 22 + "=")
    print("=" * 50)
    print("1- Créer un tournoi")
    print("2- Reprendre un tournoi")
    print("3- Historique des tournois")
    print("4- Classement ELO")
    print("5- Statistiques des joueurs")
    print("6- Règles")
    print("7- Quitter")


def fonction_principale():
    """
    Menu principal de l'application (boucle).
    """
    initialiser_fichiers_si_absents()

    while True:
        afficher_menu()
        print("\n" + "-" * 50 + "\n")

        try:
            choix = int(input("Entrez votre choix : "))
        except ValueError:
            print("\nValeur erronée, entrez un chiffre.")
            continue

        print("\n" + "-" * 50)

        if choix == 1:
            tournoi = creer_tournoi()
            if tournoi:
                ajouter_tournoi_en_cours(tournoi)
                demarrer = input("Commencer le tournoi maintenant ? (o/n) : ").strip().lower()
                if demarrer == "o":
                    lancer_tournoi(tournoi)

        elif choix == 2:
            reprendre_tournoi()

        elif choix == 3:
            afficher_historique_tournois()

        elif choix == 4:
            classement_elo()

        elif choix == 5:
            stats_joueurs()

        elif choix == 6:
            regles()

        elif choix == 7:
            print("\nGOODBYE SIRS AND LADIES\n")
            break

        else:
            print("\nChoix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    fonction_principale()
