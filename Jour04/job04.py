class Forme:
    def aire (self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        return self.__hauteur * self.__largeur   
# Instanciation de la classe Rectangle  
rectangle = Rectangle(5, 8)
# Appel de la méthode aire spécifique au rectangle
resultat_aire_rectangle = rectangle.aire()
# Affichage du résultat
print("L'aire du rectangle est:", resultat_aire_rectangle)



            




