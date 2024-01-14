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

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.__hauteur * self.surface()




rectangle1 = Rectangle(5, 3)
print("Le périmètre est:", rectangle1.get_longueur())
print("La surface est:", rectangle1.get_largeur())

rectangle1.set_longueur(7)
rectangle1.set_largeur(2)

print("Périmètre:", rectangle1.perimetre())
print("surface:", rectangle1.surface())


parallelepipede = Parallelepipede(2, 4, 3)
print("Longueur:", parallelepipede.get_longueur())
print("Largeur:", parallelepipede.get_largeur())
print("Hauteur:", parallelepipede.get_hauteur())

# Modification des attributs avec les mutateurs
parallelepipede.set_longueur(7)
parallelepipede.set_largeur(4)
parallelepipede.set_hauteur(3)

# Calcul et affichage du périmètre, de la surface et du volume après modification
#print("Périmètre:", parallelepipede.perimetre())
#print("Surface:", parallelepipede.surface())
print("Volume:", parallelepipede.volume())

