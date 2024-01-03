#Créer la classe Livre qui prend en attributs privés un titre, un auteur et un nombre de
#pages.
# les assesseurs et mutateurs nécessaires afin de pouvoir modifier et afficher les
#attributs. Pour changer le nombre de pages, Ce dernier doit être un nombre entier
#positif, sinon la valeur n’est pas changée et un message d’erreur est affiché.

class Livre:
    def __init__(self, un_titre, un_auteur, un_nombre_de_pages):
        self.__un_titre = un_titre
        self.__un_auteur = un_auteur
        self.__un_nombre_de_pages = un_nombre_de_pages

    def get_un_titre(self):
        return self.__un_titre
    
    def set_un_titre(self, nouveau_titre):
        self.__un_titre = nouveau_titre

    def get_un_auteur(self):
        return self.__un_auteur
    
    def set_un_auteur(self, nouveau_auteur):
        self.__un_auteur = nouveau_auteur

    def get_un_nombre_de_pages(self):
        return self.__un_nombre_de_pages

    def set_un_nombre_de_pages(self, nouveau_nombre_de_pages):
        if isinstance(nouveau_nombre_de_pages, int) and nouveau_nombre_de_pages > 0:
            self.__un_nombre_de_pages = nouveau_nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")
            
livre = Livre("Le Nom du Vent", "Patrick Rothfuss", 500)       
print(livre.get_un_titre()) 
print(livre.get_un_auteur())   
print(livre.get_un_nombre_de_pages()) 

livre.set_un_titre("La Peur du Sage")
livre.set_un_auteur("Patrick Rothfuss et Ollivier Pourriol")

# Tentative de modification du nombre de pages avec une valeur invalide
livre.set_un_nombre_de_pages(-100)

# Affichage des valeurs modifiées
print("Nouveau titre:", livre.get_un_titre())
print("Nouvel auteur:", livre.get_un_auteur())
print("Nouveau nombre de pages:", livre.get_un_nombre_de_pages())