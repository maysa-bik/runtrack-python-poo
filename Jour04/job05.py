class Forme:
    def aire (self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        return self.__hauteur * self.__largeur
        
class Cercle(Forme):
    def __init__(self, radius):
        Forme.__init__(self)
        self.__radius = radius

    def aire(self):
        return  3.14159 * self.__radius ** 2    
        
cercle1 = Cercle(5)
print("L'aire du cercle est:", cercle1.aire())

# Créez une instance de Rectangle
rectangle_instance = Rectangle(5, 8)
print("Aire du Rectangle:", rectangle_instance.aire())

# Créez une instance de Cercle
cercle_instance = Cercle(3)
print("Aire du Cercle:", cercle_instance.aire())