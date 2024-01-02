class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    def afficher(self):
        return f"Nom du produit :{self.nom},PRIX HT: {self.prixHT},TVA : {self.TVA}%"
    def modification_nom(self, nouveauNom):
        self.nom = nouveauNom
    def modification_prixHT(self, nouveauprixHT):
        self.prixHT = nouveauprixHT
    def retourner_nom(self):
        return self.nom
    def retourner_prixHT(self):
        return self.prixHT
    def retourner_TVA(self):
        return self.TVA

produit1 = Produit(nom="Ordinateur", prixHT=1200 , TVA=20)
produit2 = Produit(nom="Smartphone", prixHT=500 , TVA=10)
produit3 = Produit(nom="Casque Audio", prixHT=150 , TVA=30)
produits = [produit1, produit2 , produit3]
# Affichage des informations de chaque produit dans la liste
for produit in produits:
    print(produit.afficher())
    print(f"Prix TTC du produit : {produit.CalculerPrixTTC()}")

# Modification du nom et du prix de chaque produit
produit1.modification_nom("iPad")
produit2.modification_prixHT(350)

# Affichage des nouvelles informations de chaque produit dans la liste
for produit in produits:
    print(produit.afficher())    

