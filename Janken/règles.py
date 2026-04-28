def pause_retour():
    while True:
        choix = input("\nTapez 'retour' pour revenir au menu des règles : ").strip().lower()
        if choix == "retour":
            return
        print("\nErreur : tapez exactement 'retour'.")


def regles_generales():
    print("\nREGLES GENERALES :")
    print("\n- Cette application fonctionne uniquement dans le terminal.")
    print("- Lisez attentivement les messages avant de faire un choix.")
    print("- Si une mauvaise valeur est saisie, un message d'erreur s'affiche.")
    print("- Les données importantes sont sauvegardées automatiquement.")
    pause_retour()


def regles_des_tournois():
    print("\nREGLES DES TOURNOIS :")
    print("\n- Un tournoi est une suite de matchs entre plusieurs joueurs.")
    print("- Deux formats sont disponibles :")
    print("  1) Round-Robin (tous les joueurs s'affrontent)")
    print("  2) Elimination directe (le perdant est éliminé)")
    print("- Un tournoi peut être interrompu et repris plus tard.")
    print("- Un tournoi terminé ne peut plus être modifié.")
    print("- Tous les tournois terminés sont enregistrés dans l'historique.")
    pause_retour()


def regles_des_jeux():
    print("\nREGLES DES JEUX")
    print("\nPierre - Feuille - Ciseaux")
    print("- Pierre bat Ciseaux")
    print("- Ciseaux bat Feuille")
    print("- Feuille bat Pierre")
    print("- Même choix = égalité")

    print("\nMorpion")
    print("- Grille 3x3")
    print("- 3 symboles alignés = victoire (ligne/colonne/diagonale)")
    print("- Grille pleine sans gagnant = nul")
    pause_retour()


def regles_joueurs_ia():
    print("\nREGLES DES JOUEURS")
    print("\n- Chaque joueur a un nom, un type et un ELO.")
    print("- Types : humain / ia_facile")
    pause_retour()


def regles_classement_elo():
    print("\nREGLES DU CLASSEMENT ELO :")
    print("\n- Tous les joueurs commencent à 1000.")
    print("- Victoire = ELO augmente")
    print("- Défaite = ELO diminue")
    pause_retour()


def regles_sauvegarde_et_reprise():
    print("\nSAUVEGARDE ET REPRISE :")
    print("\n- Les tournois en cours sont sauvegardés.")
    print("- Un tournoi non terminé peut être repris plus tard.")
    print("- Les stats et ELO sont conservés.")
    pause_retour()


def regles():
    while True:
        print("\n" + "-" * 50)
        print("=== REGLES ET UTILISATION ===")
        print("-" * 50)
        print("\n1. Règles générales")
        print("2. Règles des tournois")
        print("3. Règles des jeux")
        print("4. Joueurs et IA")
        print("5. Classement ELO")
        print("6. Sauvegarde et reprise")
        print("7. Retour au menu principal")

        try:
            choix = int(input("\nEntrez votre choix : "))
        except ValueError:
            print("\nErreur : entre un nombre.")
            continue

        if choix == 1:
            regles_generales()
        elif choix == 2:
            regles_des_tournois()
        elif choix == 3:
            regles_des_jeux()
        elif choix == 4:
            regles_joueurs_ia()
        elif choix == 5:
            regles_classement_elo()
        elif choix == 6:
            regles_sauvegarde_et_reprise()
        elif choix == 7:
            return
        else:
            print("\nChoix invalide.")