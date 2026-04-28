''' 
    nom1 = "Clavier"
    prix1 = 49.99
    stock1 = 15

    nom2 = "Souris"
    prix2 = 30.99
    stock2 = 20

    nom3 = "Ecran"
    prix3 = 486.99
    stock3 = 17

    nom4 = "Cable"
    prix4 = 14
    stock4 = 45

    def afficher_produit():
        global nom, prix, stock
        print(f"{nom1} - {prix1}€ - Stock : {stock1}")

    def vendre(quantite):
        global stock1
        if quantite <= stock:
            stock1 -= quantite
            print(f"Vendu {quantite} {nom1}(s). Reste: {stock1}")
        else:
            print("Stock insuffisant")

    afficher_produit()
    vendre(3)
'''
'''
#Programmation orientée objet
class Produit:
    tva = 20
    nb_produits = 0

    def __init__(self,reference, nom, prix_ht, stock):
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock
        Produit.nb_produits += 1

    def prix_ttc(self):
        self.prix_ttc = self.prix_ht * (1 + Produit.tva / 100)
        return self.prix_ttc
    
    def afficher(self):
        print(f"Produit : {self.nom} (Référence {self.reference})")
        print(f"Prix HT : {self.prix_ht}€")
        print(f"Prix TTC : {self.prix_ttc}€")
        print(f"Stock disponible : {self.stock}")

    def est_disponible(self):
        return self.stock > 0
    
    def ajouter_stock(self, quantite):
        self.stock += quantite
        print(f"{quantite} {self.nom} ajoutés au stock. Le stock contien {self.stock} {self.nom}")

    def retirer_stock(self, quantite):
        self.stock -= quantite
        print(f"{quantite} {self.nom} retirés du stock.Reste {self.stock} {self.nom}")

    def valeur_stock(self):
        valeur_tva = (self.prix_ttc*self.stock)
        print(f"Valeur du stock : {valeur_tva}€")

p1 = Produit("KB-001", "Clavier", 49.99, 10)
p2 = Produit("KB-002", "Souris", 29.99, 15)
p3 = Produit("KB-003", "Écran", 199.99, 5)

p1.prix_ttc()
p1.afficher()
p1.est_disponible()
p1.ajouter_stock(4)
p1.retirer_stock(3)
p1.valeur_stock()
'''
'''
    def afficher(self):
        print(f"{self.nom} - {self.prix}€ - Stock: {self.stock}")

    def est_disponible(self):
        return self.stock > 0

    def vendre(self, quantite):
        if quantite <= self.stock:
            self.stock -= quantite
            print(f"Vendu {quantite} {self.nom}(s). Reste: {self.stock}")
        else:
            print(f"Stock insuffisant pour {self.nom}")

clavier = Produit("Clavier", 49.99, 3)
clavier.afficher()
print(clavier.est_disponible())
clavier.vendre(3)
print(clavier.est_disponible())
clavier.afficher()
'''
'''
class Produit:
    def __init__(self, nom, prix):
        self._prix = max(prix, 0.01) #Encapsulation

    def afficher(self):
        print(f"{self._prix:2f}€")

class ProduitPromo(Produit):
    def __init__(self, nom, prix, reduc):
        super().__init__(nom, prix)
        self.reduc = reduc

    def afficher(self):
        print(f"PROMO -> {self._prix*(1 - self.reduc/100):.2f}€")

p = Produit("Stylo", 3.50)
pp = ProduitPromo("Cahier", 6.00, 20)

p.afficher()
pp.afficher()
'''
'''
class Personnage:
    pass

Bogdane = Personnage()
Mamadou = Personnage()
print(type(Bogdane))
'''
'''
class Produit:
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

clavier = Produit("Clavier mécanique", 89.99, 12)
souris = Produit("Souris Gaming", 59.99, 20)

print(clavier.nom)
print(souris.prix)
print(clavier.stock)
'''
'''
class Personnage:
    def __init__(self, nom, role):
        self.nom = nom
        self.role = role

Emma = Personnage("Emma", "Vendeuse")
print(Emma.role)
'''
'''
class Livre:
    def __init__(self, titre, auteur, prix, stock):
        self._titre = titre
        self._auteur = auteur
        self._prix = prix
        self.stock = stock

    def afficher(self):
        print(f"{self._titre} par {self._auteur} - {self._prix:2f}€ - {self.stock} exemplaires disponible")

Python = Livre("Python pour Débutant", "Jean Dupont", 29.99, 50)
POO = Livre("POO avancée", "Marie Laurent", 45.50, 30)
Algo = Livre("Algorithmes", "Paul Martin", 39.99, 20)

Python.afficher()
POO.afficher()
Algo.afficher()
'''
'''
class Categorie:
    def __init__(self, nom, description, produits):
        self.nom = nom
        self.description = description
        produits = []
        self.produits = produits
        self.categorie = []

    def ajouter_produit(self, produits):
        produit = input("Ajouter un produit à la catégorie : ")
        self.produits.append(produit)

    def retirer_produit(self, produits):
        produit = input("Retirer un produit de la catégorie : ")
        if produit in self.produits:
            self.produits.remove(produits)
        else:
            print("Produit non trouvé dans la liste.")

    def lister_produits(self):
        print(f"Produits dans la catégorie {self.nom}:")
        for produit in self.produits:
            print(f"- {produit} (Prix: {produit.prix}€)")
    
    def nb_produits(self):
        return len(self.produits)
    
    def valeur_totale(self):
        total = 0
        for produit in self.produits:
            total += produit.prix
        return total
    
class Produit:
    def __init__(self, nom, reference, prix, stock):
        self.nom = nom
        self.reference = reference
        self.prix = prix
        self.stock = stock
    
peripheriques = Categorie("Périphériques", "Claviers, Souris, etc.")
p1 = Categorie.produits("Clavier", "KB-001", 49.99, 10)
peripheriques.ajouter_produit(p1)
peripheriques.lister_produits()
'''
'''
class Produit:
    def __init__(self, reference, nom, prix_ht, stock):
        self.reference = reference
        self.nom = nom
        self._prix_ht = prix_ht
        self.stock = stock

produit = Produit("KB-001", "Clavier", 49.99, 10)
#Danger! Modifications non validées
produit._prix_ht = - 100
print(produit._prix_ht)
'''
'''
class Produit:
    def __init__(self, reference, nom, prix_ht, stock):
        self.reference = reference
        self._nom = nom
        self._prix_ht = max(prix_ht, 0.01)  # Encapsulation avec validation
        self._stock = stock
        self.__marge = 0.3 #Privé

    def get_prix_ht(self):
        """Lecture controlée du prix"""
        return self._prix_ht

    def set_prix_ht(self, nouveau_prix):
        """Modification avec Validation"""
        if nouveau_prix > 0:
            self._prix_ht = nouveau_prix
        else:
            raise ValueError("Le prix doit être positif.")
        
    def get_stock(self):
        return self._stock
    
    def set_stock(self, nouvelle_quantite):
        if nouvelle_quantite >= 0:
            self._stock = nouvelle_quantite
        else:
            raise ValueError("La quantité en stock ne peut pas être négative.")
        
#Utilisation recommendée
produit = Produit("KB-001", "Clavier", 49.99, 10)
print(f"Nombre d'articles en stock : {produit.get_stock()}")    
produit.set_stock(25)
print(f"Nouveau stock : {produit.get_stock()}")

print(produit.get_prix_ht())
produit.set_prix_ht(59.99)
#Pratique déconseillée mais possible
print(produit._prix_ht)

#Ceci déclenche une exception
try:
    produit.set_prix_ht(-10)
except ValueError as e:
    print(e)


try:
    print(f"Changement de valeur de stock :")
    produit.set_stock(-5)
except ValueError as e:
    print(e)
'''
'''
class Produit:
    def __init__(self, reference, nom, prix_ht, stock):
        self._reference = reference
        self._nom = nom
        self._prix_ht = prix_ht
        self._stock = stock

    @property
    def prix_ht(self):
        return self._prix_ht
    
    @prix_ht.setter
    def prix_ht(self, nouvelle_valeur):
        if not isinstance(nouvelle_valeur, (int, float)):
            raise TypeError("Le prix doit etre un nombre.")
        if nouvelle_valeur <= 0:
            raise ValueError("Le prix doit etre positif.")
        self._prix_ht = round(nouvelle_valeur, 2)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nouvelle_quantite):
        if not isinstance(nouvelle_quantite, int):
            raise TypeError("La quantité en stock doit être un entier.")
        if nouvelle_quantite < 0:
            raise ValueError("La quantité en stock ne peut pas être négative.")
        self._stock = nouvelle_quantite

produit = Produit("KB-001", "Clavier", 49.99, 10)
print(f"Prix du produit '{produit._nom}' : {produit.prix_ht}")
print(f"Modification du prix...")
produit.prix_ht = 59.99
print(f"Nouveau prix : {produit.prix_ht}")
print(f"Nombre d'articles en stock : {produit.stock}")
print(f"Modification du stock...")
produit.stock = 25
print(f"Nouveau stock : {produit.stock}")

try:
    print(f"Changement de valeur de prix : -10€")
    produit.prix_ht = -10
except ValueError as e:
    print(f"Erreur capturée : {e}")

try:
    print(f"Changement de valeur de prix : 'abc'")
    produit.prix_ht = "abc"
except TypeError as e:
    print(f"Erreur capturée : {e}")

try:
    print(f"Changement de valeur de stock : -5")
    produit.stock = -5
except ValueError as e:
    print(f"Erreur capturée : {e}")

try:
    print(f"Changement de valeur de stock : 15.5")
    produit.stock = 15.5
except TypeError as e:
    print(f"Erreur capturée : {e}")
'''
'''
class Produit:
    tva = 20  # attribut de classe (%)

    def __init__(self, nom, prix_ht):
        self.nom = nom
        self._prix_ht = prix_ht

    @property
    def prix_ttc(self):
        return round(self._prix_ht * (1 + Produit.tva / 100), 2)

    @property
    def marge_ttc(self):
        """Prix TTC avec 10 % de marge"""
        return round(self.prix_ttc * 1.1, 2)

produit = Produit("Clavier", 50)

print("Prix TTC :", produit.prix_ttc)      # 60.0
print("Marge TTC :", produit.marge_ttc)    # 66.0

print("Changer le prix HT")
produit._prix_ht = 100

print("Prix TTC :", produit.prix_ttc)      # 120.0
print("Marge TTC :", produit.marge_ttc)    # 132.0
'''
'''
class Produit:
    tva = 20
    nb_produits = 0

    def __init__(self, reference, nom, prix_ht, stock):
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock
        Produit.nb_produits += 1

    @property
    def reference(self):
        return self._reference
    
    @reference.setter
    def reference(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("La référence doit être une chaîne de caractères.")
        if len(valeur) < 3:
            raise ValueError("La référence doit contenir au moins 3 caractères.")
        self._reference = valeur.upper()

    @property
    def prix_ht(self):
        return self._prix_ht
    
    @prix_ht.setter
    def prix_ht(self, valeur):
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le prix doit être un nombre.")
        if valeur <= 0:
            raise ValueError("Le prix doit être positif.")
        self._prix_ht = round(valeur, 2)
'''
'''
class Produit:
    tva = 20
    nb_produits = 0

    def __init__(self, reference, nom, prix_ht, stock, categorie=None):
        self._reference = reference
        self._nom = nom
        self._prix_ht = prix_ht
        self._stock = stock
        self._categorie = None
        Produit.nb_produits += 1
        if categorie is not None:
            self.categorie = categorie

    @property
    def reference(self):
        return self._reference
    
    @reference.setter
    def reference(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("La référence doit être une chaîne de caractères.")
        if len(valeur) < 3:
            raise ValueError("La référence doit contenir au moins 3 caractères.")
        self._reference = valeur.upper()

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("Le nom doit être une chaîne de caractères.")
        if len(valeur) < 1:
            raise ValueError("Le nom ne peut pas être vide.")
        self._nom = valeur.lower().capitalize()

    @property
    def prix_ht(self):
        return self._prix_ht
    
    @prix_ht.setter
    def prix_ht(self, valeur):
        print(f"Modification du prix HT de {self._prix_ht}€ à {valeur}€...")
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le prix doit être un nombre.")
        if valeur <= 0:
            raise ValueError("Le prix doit être positif.")
        self._prix_ht = round(valeur, 2)

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, valeur):

        if not isinstance(valeur, int):
            raise TypeError("La quantité en stock doit être un entier.")
        if valeur < 0:
            raise ValueError("La quantité en stock ne peut pas être négative.")
        self._stock = valeur

    @property
    def prix_ttc(self):
        return round(self._prix_ht * (1 + Produit.tva / 100), 2)

    @property
    def marge_ttc(self):
        return round(self.prix_ttc - self._prix_ht, 2)

    @property
    def valeur_stock(self):
        return round(self.prix_ttc * self._stock, 2)
    
    def ajouter_stock(self, quantite):
        print(f"Ajout de {quantite} unités au stock...")
        if quantite <= 0:
            raise ValueError("La quantité à ajouter doit être positive.")
        self._stock += quantite

    def retirer_stock(self, quantite):
        print(f"Retrait de {quantite} unités du stock...")
        if quantite <= 0:
            raise ValueError("La quantité à retirer doit être positive.")
        if quantite > self._stock:
            raise ValueError("Stock insuffisant pour retirer cette quantité.")
        self._stock -= quantite
        print(f"{quantite} unités retirées du stock. Stock restant : {self._stock}")

    def afficher(self):
        cat = self._categorie.nom if self._categorie is not None else "(Aucune)"
        print(f"Produit : {self._nom} (Référence : {self._reference}) | Catégorie : {cat}")
        print(f"Prix HT : {self._prix_ht}€")
        print(f"Prix TTC : {self.prix_ttc}€")
        print(f"Marge TTC : {self.marge_ttc}€")
        print(f"Stock disponible : {self._stock}")
        print(f"Valeur du stock : {self.valeur_stock}€")
        print()

try:
    produit = Produit("KB-001", "Clavier", 49.99, 10)
    produit.afficher()
    produit.retirer_stock(11)
    produit.afficher()
    produit.ajouter_stock(5)
    produit.afficher()
except (ValueError, TypeError) as e:
    print(f"Erreur capturée : {e}")

try:
    produit.prix_ht = -20
    produit.afficher()
except (ValueError, TypeError) as e:
    print(f"Erreur capturée : {e}")


class Categorie:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self._produits = []
    
    @property
    def nb_produits(self):
        return len(self._produits)
    
    @property
    def valeur_totale(self):
        return sum(p.valeur_stock for p in self._produits)
    
    @property
    def produits_disponibles(self):
        return [p for p in self._produits if p.stock > 0]
    
    def ajouter_produit(self, produit):
        self._produits.append(produit) 

    def retirer_produit(self, produit):
        self._produits.remove(produit)

    def lister_produits(self):
        print(f"Produits dans la catégorie '{self.nom}':")
        for produit in self._produits:
            print(f"- {produit.nom} | Prix: {produit.prix_ht}€ , Stock: {produit.stock}")
'''
'''
class Produit:
    """Classe parente (ou classe de base)"""
    tva = 20

    def __init__(self, reference, nom, prix_ht, stock):
        self._reference = reference
        self._nom = nom
        self._prix_ht = prix_ht
        self._stock = stock

    def afficher(self):
        print(f"[{self._reference}]{self._nom} - {self._prix_ht}€ HT")

    @property
    def prix_ttc(self):
        return round(self._prix_ht * (1 + Produit.tva / 100), 2)
    

class ProduitElectronique(Produit):
    """Classe enfant : herite du Produit"""
    def __init__(self, reference, nom, prix_ht, stock, garantie_mois):
        # Appeler le constructeur du parent
        super().__init__(reference, nom, prix_ht, stock)
        # Attribut spécifique à l'enfant
        self._garantie_mois = garantie_mois

    def afficher(self):
        # Surcharge : redéfinit la méthode du parent
        super().afficher() # Appelle la méthode du parent
        print(f"Garantie: {self._garantie_mois} mois")

# Utilisation
clavier = ProduitElectronique("KB-001", "Clavier RGB", 79.99, 15, 24)
clavier.afficher()
#[KB-001] Clavier RGB - 79.99€ HT
# Garantie: 24 mois
print(clavier.prix_ttc) # 95.99 (hérité d'un parent)


class ProduitAlimentaire(Produit):
    """Classe enfant : hérite du produit"""
    def __init__(self, reference, nom, prix_ht, stock, date_peremption):
        #Appeler le constructeur du parent
        super().__init__(reference, nom, prix_ht, stock)
        # Attribut spécifique à l'enfant
        self._date_peremption = date_peremption

    def afficher(self):
        #Surcharge : redéfinit la méthode du parent
        super().afficher() #Appelle la méthode du parent
        print(f"Date de péremption : {self._date_peremption}")

#Utilisation
yaourt = ProduitAlimentaire("KA-001", "Yaourt Complet", 14.99, 12, "22/05/2026")
yaourt.afficher()
print(yaourt.prix_ttc)
'''
'''
class Produit:
    def __init__(self, ref, nom, prix, ):
        self._reference = ref
        self._nom = nom
        self._prix_ht = prix
        print("Constructeur Produit Appelé")

    def caluler_frais_livraison():
        return 5.00 # Frais standart

class ProduitElectronique(Produit):
    def __init__(self, ref, nom, prix, garantie):
        super().__init__(ref, nom, prix)
        self._garantie = garantie
        print("Constructeur ProduitElectronique")

    def calculer_frais_livraison(self):
        return 10.00 #Plus chère car fragile


class ProduitAlimentaire(Produit):
    """Classe enfant : hérite du produit"""
    def __init__(self, reference, nom, prix_ht, stock, date_peremption):
        #Appeler le constructeur du parent
        super().__init__(reference, nom, prix_ht, stock)
        # Attribut spécifique à l'enfant
        self._date_peremption = date_peremption

    def afficher(self):
        #Surcharge : redéfinit la méthode du parent
        super().afficher() #Appelle la méthode du parent
        print(f"Date de péremption : {self._date_peremption}")

    def calculer_frais_livraison(self):
        return 15.00 #PLus chère car refrigéré

    
produits = [Produit("GEN-001", "Claviers", 10),
            ProduitElectronique("KB-001", "Clavier", 79.99, 15, 24),
            ProduitAlimentaire("ALI-001", "Fromage", 12.99, 50, "2025-01-15")
            ]

for p in produits:
    print(f"{p._nom}:{p.calculer_frais_de_livraison()} €")
'''
'''
class Produit:
    def __init__(self, nom, prix):
        self._nom = nom
        self._prix = prix

    def frais_livraison(self):
        return 5.00  # Frais standard
    
    @property
    def frais_totaux(self):
        return self._prix + self.frais_livraison()
       
    def afficher(self):
        print(f"{self._nom} - {self._prix}€")
    
class ProduitFragile(Produit):
    def __init__(self, nom, prix):
        super().__init__(nom, prix)

    def frais_livraison(self):
        return 12.00  # Frais plus élevés pour les produits fragiles
     
    @property
    def frais_totaux(self):
        return self._prix + self.frais_livraison()

    def afficher(self):
        return super().afficher()
    
class ProduitLourd(Produit):
    def __init__(self, nom, prix):
        super().__init__(nom, prix)

    def frais_livraison(self):
        return 20.00  # Frais plus élevés pour les produits lourds
    
    @property
    def frais_totaux(self):
        return self._prix + self.frais_livraison()

    def afficher(self):
        return super().afficher()
    
produits = [Produit("Livre", 15.99),
            ProduitFragile("Vase en verre", 45.00),
            ProduitLourd("Machine à laver", 499.99)
            ]

for p in produits:
    message = (
        f"Nom du produit: {p._nom} "
        f"| Prix: {p._prix}€ "
    )
    print(message)
    print(f"Frais de livraison: {p.frais_livraison()}€")
    print(f"Frais totaux: {p.frais_totaux}€")
    print()
    '''

'''
from abc import ABC, abstractmethod

class Produit(ABC):
    #Classe abstraite: Ne peut pas se faire instancier
    def __init__(self, reference, nom, prix_ht, stock):
        self._reference = reference
        self._nom = nom
        self._prix_ht = prix_ht
        self._stock = stock

    @abstractmethod
    def calculer_frais_livraison(self):
        #Méthode Abstraite: Doit être implémentée dans les sous-classes
        pass

    @abstractmethod
    def afficher_détails(self):
        pass

    def afficher(self):
        #Méthode concrète: Peut être utilisée telle quelle
        print(f"Produit : {self._nom} (Référence : {self._reference})")
        print(f"Prix HT : {self._prix_ht}€")                
        print(f"Stock disponible : {self._stock}")

class ProduitElectronique(Produit):
    def __init__(self, reference, nom, prix_ht, stock, garantie):
        super().__init__(reference, nom, prix_ht, stock)
        self._garantie = garantie

        def calculer_frais_livraison(self):
            return 10.00 #Plus chère car fragile

        def afficher_détails(self):
            print(f"Garantie: {self._garantie} mois")

'''
'''
class Produit:
    def __init__(self, ref, nom, prix):
        self._reference = ref
        self._nom = nom
        self._prix_ht = prix

    def __str__(self):
        return f"{self._nom} ({self._reference}) - {self._prix_ht}€"
    
    def __repr__(self):
        return f"Produit ('{self._reference}', '{self._nom}', {self._prix_ht}€)"
    
clavier = Produit("KB-001", "Clavier RGB", 79.99)
print(clavier)
print(str(clavier))
print(repr(clavier))
'''

class Produit:
    """Produit minimal pour tester Categorie"""
    def __init__(self, reference, nom, prix, stock):
        self.reference = reference
        self.nom = nom
        self.valeur_stock = prix * stock


class Categorie:
    def __init__(self, nom, description=""):
        self.nom = nom
        self.description = description
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def nb_produits(self):
        return len(self.produits)

    def valeur_totale(self):
        return sum(p.valeur_stock for p in self.produits)

    # Version jolie pour print(cat)
    def __str__(self):
        return (
            f"Catégorie {self.nom} "
            f"({self.nb_produits()} produit(s) – "
            f"valeur totale {self.valeur_totale():.2f} €)"
        )

    # Version technique (console / repr(cat))
    def __repr__(self):
        refs = [p.reference for p in self.produits]
        refs_str = ", ".join(refs) if refs else "aucun"
        return f"Categorie('{self.nom}', {self.nb_produits()} produits, refs=[{refs_str}])"
    
class Inventaire:
    def __init__(self):
        self._produits = []
    def ajouter(self, produit):
        self._produits.append(produit)
    def __len__(self):
        return len(self._produits)
    
    def __bool__(self):
        return len(self._produits) > 0
    
    def __getitem__(self, index):
        return self._produits[index]
    
    def __setitem__(self, index, produit):
        self._produits[index] = produit

inv = Inventaire()
print(len(inv))
print(bool(inv))

inv.ajouter(Produit("MS-001", "Souris", 49.99))
print(inv[0])
inv[1] = Produit("MS-002", "Souris Gaming", 99.99)
print(inv[1])

# ───────────────────────────────────────────────
# Test simple et autonome
# ───────────────────────────────────────────────

if __name__ == "__main__":
    # Création catégorie
    cat = Categorie("Périphériques", "Matériel informatique")

    # Un seul produit pour rester simple
    clavier = Produit("KB-001", "Clavier RGB", 79.99, 10)
    cat.ajouter_produit(clavier)

    print("Avec print(cat) :")
    print(cat)
    # → Catégorie Périphériques (1 produit(s) – valeur totale 799.90 €)

    print("\nAvec repr(cat) ou juste cat dans la console :")
    print(repr(cat))
    # → Categorie('Périphériques', 1 produits, refs=[KB-001])