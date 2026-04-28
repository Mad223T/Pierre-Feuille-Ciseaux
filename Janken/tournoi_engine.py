import json
import os

from match_morpion import jouer_match_morpion
from match_ppc import jouer_match_ppc


JOUEURS_FILE = "joueurs.json"
TOURNOIS_EN_COURS_FILE = "tournoi_en_cours.json"
HIST_FILE = "historique_tournois.json"


# -------------------------
# Outils JSON (simples)
# -------------------------
def lire_json(path, default):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return default


def ecrire_json(path, data):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except:
        return False


def initialiser_fichiers_si_absents():
    if not os.path.exists(JOUEURS_FILE):
        ecrire_json(JOUEURS_FILE, [])
    if not os.path.exists(TOURNOIS_EN_COURS_FILE):
        # LISTE de tournois en cours (pour pouvoir en avoir plusieurs)
        ecrire_json(TOURNOIS_EN_COURS_FILE, [])
    if not os.path.exists(HIST_FILE):
        ecrire_json(HIST_FILE, [])


# -------------------------
# Matchs : génération
# -------------------------
def generer_matchs_round_robin(participants):
    matchs = []
    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            matchs.append({
                "joueur1": participants[i]["nom"],
                "joueur2": participants[j]["nom"],
                "resultat": None,
                "termine": False
            })
    return matchs


def generer_matchs_elimination(participants):
    matchs = []
    for i in range(0, len(participants), 2):
        matchs.append({
            "joueur1": participants[i]["nom"],
            "joueur2": participants[i + 1]["nom"],
            "resultat": None,
            "termine": False
        })
    return matchs


# -------------------------
# Joueurs : retrouver
# -------------------------
def trouver_joueur(joueurs, nom):
    for j in joueurs:
        if j.get("nom") == nom:
            # sécurité minimale
            if "elo" not in j:
                j["elo"] = 1000
            if "historique" not in j:
                j["historique"] = []
            return j
    return None


# -------------------------
# PONT vers vos deux jeux (NE MODIFIE PAS les matchs)
# -------------------------
def jouer_un_match_selon_jeu(tournoi, j1, j2):
    """
    Appelle la bonne fonction de match selon tournoi["jeu"].
    Retourne toujours :
    - "victoire_j1" / "victoire_j2" / "nul"
    """
    jeu = tournoi["jeu"].strip().lower()

    if jeu == "morpion":
        return jouer_match_morpion(j1, j2)

    # ppc (par défaut)
    return jouer_match_ppc(j1, j2)


# -------------------------
# Tournoi : ajout / liste / sauvegarde
# -------------------------
def charger_tournois_en_cours():
    return lire_json(TOURNOIS_EN_COURS_FILE, [])


def sauvegarder_tournois_en_cours(tournois):
    return ecrire_json(TOURNOIS_EN_COURS_FILE, tournois)


def ajouter_tournoi_en_cours(tournoi):
    tournois = charger_tournois_en_cours()
    tournois.append(tournoi)
    sauvegarder_tournois_en_cours(tournois)


def mettre_a_jour_un_tournoi(tournoi_modifie):
    """
    Remplace le tournoi correspondant (même nom) dans tournoi_en_cours.json
    """
    tournois = charger_tournois_en_cours()
    for i in range(len(tournois)):
        if tournois[i].get("nom") == tournoi_modifie.get("nom"):
            tournois[i] = tournoi_modifie
            break
    sauvegarder_tournois_en_cours(tournois)


def archiver_tournoi(tournoi_termine):
    hist = lire_json(HIST_FILE, [])
    hist.append(tournoi_termine)
    ecrire_json(HIST_FILE, hist)


# -------------------------
# Stats + ELO (simple)
# -------------------------
def ajouter_historique_match(joueur, adversaire_nom, jeu, resultat):
    """
    Ajoute un match dans l'historique d'un joueur.
    resultat attendu : "victoire" / "defaite" / "nul"
    """
    if "historique" not in joueur:
        joueur["historique"] = []

    joueur["historique"].append({
        "jeu": jeu,
        "adversaire": adversaire_nom,
        "resultat": resultat
    })


def mettre_a_jour_elo_simple(j1, j2, resultat):
    """
    +50 au gagnant, -50 au perdant, 0 si nul.
    """
    if "elo" not in j1:
        j1["elo"] = 1000
    if "elo" not in j2:
        j2["elo"] = 1000

    if resultat == "victoire_j1":
        j1["elo"] += 50
        j2["elo"] -= 50
    elif resultat == "victoire_j2":
        j2["elo"] += 50
        j1["elo"] -= 50

    # pas d'elo négatif
    if j1["elo"] < 0:
        j1["elo"] = 0
    if j2["elo"] < 0:
        j2["elo"] = 0


def appliquer_resultat_match(j1, j2, tournoi, resultat):
    """
    Met à jour :
    - historique (stats)
    - ELO
    """
    jeu = tournoi.get("jeu", "inconnu")

    if resultat == "victoire_j1":
        ajouter_historique_match(j1, j2["nom"], jeu, "victoire")
        ajouter_historique_match(j2, j1["nom"], jeu, "defaite")
        mettre_a_jour_elo_simple(j1, j2, resultat)

    elif resultat == "victoire_j2":
        ajouter_historique_match(j1, j2["nom"], jeu, "defaite")
        ajouter_historique_match(j2, j1["nom"], jeu, "victoire")
        mettre_a_jour_elo_simple(j1, j2, resultat)

    else:  # "nul"
        ajouter_historique_match(j1, j2["nom"], jeu, "nul")
        ajouter_historique_match(j2, j1["nom"], jeu, "nul")
        # ELO inchangé


# -------------------------
# Elimination : helpers
# -------------------------
def gagnant_du_match(match):
    if match["resultat"] == "victoire_j1":
        return match["joueur1"]
    if match["resultat"] == "victoire_j2":
        return match["joueur2"]
    return None


def generer_tour_suivant_elimination(gagnants):
    matchs = []
    for i in range(0, len(gagnants), 2):
        matchs.append({
            "joueur1": gagnants[i],
            "joueur2": gagnants[i + 1],
            "resultat": None,
            "termine": False
        })
    return matchs


# -------------------------
# Bracket ASCII "vrai" (élimination directe)
# -------------------------
def afficher_bracket_elimination(tournoi):
    """
    Affiche un "vrai" bracket ASCII avec branches (│ ├── └──),
    basé sur tournoi["tours"] (liste de tours).

    IMPORTANT:
    - tours[0] = premier tour (plus grand)
    - tours[-1] = finale (1 match)
    """

    tours = tournoi.get("tours", [])
    if not tours:
        print("\n[Bracket] Aucun match à afficher.\n")
        return

    def gagnant_match(m):
        if m.get("resultat") == "victoire_j1":
            return m["joueur1"]
        if m.get("resultat") == "victoire_j2":
            return m["joueur2"]
        if m.get("resultat") == "nul":
            return "NUL"
        return "?"

    def etiquette_match(m):
        j1 = m["joueur1"]
        j2 = m["joueur2"]
        g = gagnant_match(m)

        if g == "NUL":
            return f"{j1} vs {j2}  ->  NUL (replay)"
        if g == "?":
            return f"{j1} vs {j2}"
        return f"{j1} vs {j2}  ->  {g}"

    # Racine = finale (dernier tour), match 0
    def afficher_noeud(tour_index, match_index, prefix="", est_dernier=False):
        m = tours[tour_index][match_index]
        branche = "└── " if est_dernier else "├── "
        print(prefix + branche + etiquette_match(m))

        # Si on est au premier tour, on s'arrête
        if tour_index == 0:
            return

        # Parents dans le tour précédent : (2*i) et (2*i+1)
        gauche = 2 * match_index
        droite = 2 * match_index + 1

        nouveau_prefix = prefix + ("    " if est_dernier else "│   ")

        afficher_noeud(tour_index - 1, gauche, nouveau_prefix, est_dernier=False)
        afficher_noeud(tour_index - 1, droite, nouveau_prefix, est_dernier=True)

    print("\n" + "=" * 52)
    print("                 BRACKET (ELIMINATION)")
    print("=" * 52)

    afficher_noeud(len(tours) - 1, 0, prefix="", est_dernier=True)

    print("=" * 52 + "\n")


def initialiser_tours_elimination(tournoi):
    """
    Crée tournoi["tours"] si absent et met le 1er tour dedans.
    Le tour courant à jouer est toujours : tournoi["matchs"] = dernier tour.
    """
    if "tours" not in tournoi or tournoi["tours"] is None:
        tournoi["tours"] = []

    if len(tournoi["tours"]) == 0:
        premier_tour = generer_matchs_elimination(tournoi["participants"])
        tournoi["tours"].append(premier_tour)

    tournoi["matchs"] = tournoi["tours"][-1]
    tournoi["index_match_actuel"] = 0


def passer_au_tour_suivant_elimination(tournoi, gagnants):
    """
    Ajoute un nouveau tour dans tournoi["tours"] à partir des gagnants
    et le définit comme tour courant.
    """
    nouveau_tour = generer_tour_suivant_elimination(gagnants)
    tournoi["tours"].append(nouveau_tour)
    tournoi["matchs"] = nouveau_tour
    tournoi["index_match_actuel"] = 0


# -------------------------
# Tournoi : lancement (après création ou reprise)
# -------------------------
def lancer_tournoi(tournoi):
    """
    Joue un tournoi, sauvegarde après chaque match.
    - Round-robin joue vraiment les matchs
    - ELO et stats se mettent à jour
    - Elimination enchaîne les tours + bracket ASCII
    """
    joueurs = lire_json(JOUEURS_FILE, [])

    # champs minimum
    if "matchs" not in tournoi or tournoi["matchs"] is None:
        tournoi["matchs"] = []
    if "index_match_actuel" not in tournoi:
        tournoi["index_match_actuel"] = 0
    if "termine" not in tournoi:
        tournoi["termine"] = False

    fmt = tournoi["format"].strip().lower()

    # --------- ROUND ROBIN ---------
    if fmt == "round_robin" or "round" in fmt:
        if len(tournoi["matchs"]) == 0:
            tournoi["matchs"] = generer_matchs_round_robin(tournoi["participants"])
            tournoi["index_match_actuel"] = 0
            tournoi["termine"] = False
            mettre_a_jour_un_tournoi(tournoi)

        while tournoi["index_match_actuel"] < len(tournoi["matchs"]):
            idx = tournoi["index_match_actuel"]
            match = tournoi["matchs"][idx]

            j1 = trouver_joueur(joueurs, match["joueur1"])
            j2 = trouver_joueur(joueurs, match["joueur2"])

            if j1 is None or j2 is None:
                print("Erreur : joueur introuvable dans joueurs.json.")
                return

            print(f"\nMatch {idx + 1}/{len(tournoi['matchs'])} : {match['joueur1']} vs {match['joueur2']}")
            input("Appuie sur Entrée pour jouer...")

            resultat = jouer_un_match_selon_jeu(tournoi, j1, j2)

            match["resultat"] = resultat
            match["termine"] = True

            appliquer_resultat_match(j1, j2, tournoi, resultat)

            tournoi["index_match_actuel"] += 1

            ecrire_json(JOUEURS_FILE, joueurs)
            mettre_a_jour_un_tournoi(tournoi)

            continuer = input("Continuer le tournoi ? (o/n) : ").strip().lower()
            if continuer != "o":
                print("Tournoi sauvegardé. Tu pourras le reprendre plus tard.")
                return

        tournoi["termine"] = True
        mettre_a_jour_un_tournoi(tournoi)
        archiver_tournoi(tournoi)
        print("\n✅ Tournoi Round-Robin terminé et archivé !")
        return

    # --------- ELIMINATION ---------
    if fmt == "elimination":
        # Important : on joue par tours et on garde tout dans tournoi["tours"]
        initialiser_tours_elimination(tournoi)
        tournoi["termine"] = False
        mettre_a_jour_un_tournoi(tournoi)

        while True:
            # Afficher le bracket au début du tour
            afficher_bracket_elimination(tournoi)

            # Jouer tous les matchs du tour courant (tournoi["matchs"])
            while tournoi["index_match_actuel"] < len(tournoi["matchs"]):
                idx = tournoi["index_match_actuel"]
                match = tournoi["matchs"][idx]

                j1 = trouver_joueur(joueurs, match["joueur1"])
                j2 = trouver_joueur(joueurs, match["joueur2"])

                if j1 is None or j2 is None:
                    print("Erreur : joueur introuvable dans joueurs.json.")
                    return

                # Afficher le bracket avant chaque match
                afficher_bracket_elimination(tournoi)

                print(f"\nMatch : {match['joueur1']} vs {match['joueur2']}")
                input("Appuie sur Entrée pour jouer...")

                resultat = jouer_un_match_selon_jeu(tournoi, j1, j2)

                match["resultat"] = resultat
                match["termine"] = True

                appliquer_resultat_match(j1, j2, tournoi, resultat)

                tournoi["index_match_actuel"] += 1

                # sauvegarder joueurs + tournoi (avec l'arbre)
                ecrire_json(JOUEURS_FILE, joueurs)
                mettre_a_jour_un_tournoi(tournoi)

                continuer = input("Continuer ? (o/n) : ").strip().lower()
                if continuer != "o":
                    print("Tournoi sauvegardé. Tu peux reprendre plus tard.")
                    return

            # Fin du tour : récupérer gagnants
            gagnants = []
            match_nul_trouve = False

            for m in tournoi["matchs"]:
                g = gagnant_du_match(m)
                if g is None:
                    match_nul_trouve = True
                    print("\nMatch nul en élimination directe : on rejoue ce match.")
                    tournoi["matchs"] = [{
                        "joueur1": m["joueur1"],
                        "joueur2": m["joueur2"],
                        "resultat": None,
                        "termine": False
                    }]
                    tournoi["tours"][-1] = tournoi["matchs"]
                    tournoi["index_match_actuel"] = 0
                    mettre_a_jour_un_tournoi(tournoi)
                    break
                gagnants.append(g)

            if match_nul_trouve:
                continue

            # Afficher le bracket après le tour
            afficher_bracket_elimination(tournoi)

            # Champion ?
            if len(gagnants) == 1:
                tournoi["termine"] = True
                mettre_a_jour_un_tournoi(tournoi)
                archiver_tournoi(tournoi)
                print("\n✅ Tournoi terminé ! Champion :", gagnants[0])
                return

            # Tour suivant
            passer_au_tour_suivant_elimination(tournoi, gagnants)
            mettre_a_jour_un_tournoi(tournoi)


# -------------------------
# Reprise : choisir quel tournoi continuer
# -------------------------
def reprendre_tournoi():
    tournois = charger_tournois_en_cours()
    actifs = []
    for t in tournois:
        if t.get("termine") is False:
            actifs.append(t)

    if len(actifs) == 0:
        print("Aucun tournoi en cours.")
        return

    print("\nTournois en cours :")
    for i, t in enumerate(actifs, start=1):
        joues = t.get("index_match_actuel", 0)
        total = len(t.get("matchs", []))
        print(f"{i}. {t['nom']} ({t['jeu']} - {t['format']}) [{joues}/{total}]")

    while True:
        try:
            choix = int(input("Choisis un tournoi : ")) - 1
            if 0 <= choix < len(actifs):
                lancer_tournoi(actifs[choix])
                return
            print("Choix invalide.")
        except:
            print("Entre un nombre.")


# -------------------------
# Historique : afficher tournois terminés
# -------------------------
def afficher_historique_tournois():
    hist = lire_json(HIST_FILE, [])
    if len(hist) == 0:
        print("Aucun tournoi terminé.")
        return

    print("\nHistorique des tournois :")
    for i, t in enumerate(hist, start=1):
        total = len(t.get("matchs", []))
        print(f"{i}. {t['nom']} ({t['jeu']} - {t['format']}) - {total} matchs")

    input("\nAppuie sur Entrée pour revenir au menu...")
