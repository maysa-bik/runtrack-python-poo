class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon 

    def afficherInfos(self):
        print(f"Rayon du cercle : {self.rayon}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Aire : {self.aire()}")    

    def circonference(self):
        return 2 * 3.14159 * self.rayon

    def aire(self):
        return 3.14159 * (self.rayon ** 2)
    
    def diametre(self):
        return 2 * self.rayon
    
cercle = Cercle(5)
cercle.afficherInfos()    

# Créer deux cercles avec des rayons 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Afficher les informations pour chaque cercle
#print("Cercle 1:")
#cercle1.afficherInfos()

#print("\nCercle 2:")
#cercle2.afficherInfos()
# Afficher les informations pour chaque cercle
print("Informations pour Cercle 1:")
cercle1.afficherInfos()

print("\nInformations pour Cercle 2:")
cercle2.afficherInfos()
