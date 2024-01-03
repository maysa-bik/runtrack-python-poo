class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def get_longueur(self):
        return self.longueur

    def set_longueur(self, longueur):
        self.longueur = longueur 

    def get_largeur(self):
        return self.largeur

    def set_largeur(self, largeur):
        self.largeur = largeur

mon_rectangle = Rectangle(10, 5)
print(mon_rectangle.get_longueur())
print(mon_rectangle.get_largeur())

# Modification des valeurs
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# Affichage des valeurs modifiées
print("Nouvelle longueur:", mon_rectangle.get_longueur())
print("Nouvelle largeur:", mon_rectangle.get_largeur())

