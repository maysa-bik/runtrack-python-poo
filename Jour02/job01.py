class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur 

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

mon_rectangle = Rectangle(10, 5)
print(mon_rectangle.get_longueur())
print(mon_rectangle.get_largeur())

# Modification des valeurs
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# Affichage des valeurs modifiées
print("Nouvelle longueur:", mon_rectangle.get_longueur())
print("Nouvelle largeur:", mon_rectangle.get_largeur())

