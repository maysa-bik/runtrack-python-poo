#Récupérer la classe Livre.
#Ajouter l'attribut privé suivant :
#- disponible est initialisé par défaut à True.

#Créer une méthode nommée vérification qui vérifie si le livre est disponible, c'est-à-dire
#que la valeur de son attribut disponible est égale à True. Cette méthode doit retourner
#True ou False.

#Ajouter une méthode emprunter qui rend le livre indisponible, autrement dit la valeur de
#disponible devient False. Bien sûr, pour pouvoir emprunter un livre, il faut que celui-ci
#soit disponible, vérifiez donc que celui-ci soit disponible sans utiliser l’attribut
#disponible.

#Après avoir emprunté un livre, il faut pouvoir le rendre. Créer une méthode rendre qui
#dans un premier temps vérifie si le livre a bien été emprunté ( sans utiliser l’attribut
#disponible), puis change la valeur de l’attribut disponible.

class Livre:
    def __init__(self, un_titre, un_auteur, un_nombre_de_pages):
        self.__un_titre = un_titre
        self.__un_auteur = un_auteur
        self.__un_nombre_de_pages = un_nombre_de_pages
        self.__disponible = True

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

    def set_disponible(self, valeur):
        self.__disponible = valeur        

    def verification(self):
        return self.__disponible 

    def emprunter(self):
        if self.verification(): # Vérifie si le livre est disponible
            self.set_disponible(False)   
            print("Livre emprunté avec succès.")

        else:
            print("Le livre n'est pas disponible pour l'emprunt.")    
    
    def rendre(self):
        if not self.verification():  # Vérifie si le livre a été emprunté
            self.set_disponible(True)
            print("Livre rendu avec succès.")

        else:
            print("Le livre n'a pas été emprunté.") 


livre = Livre("Le Nom du Vent", "Patrick Rothfuss", 500)       
print(livre.get_un_titre()) 
print(livre.get_un_auteur())   
print(livre.get_un_nombre_de_pages()) 
print(livre.verification())  # Devrait afficher True 
# Emprunter le livre
livre.emprunter()
# Tentative d'emprunter à nouveau (le livre n'est plus disponible)
livre.emprunter()

# Rendre le livre
livre.rendre()

# Tentative de rendre à nouveau (le livre n'a pas été emprunté)
livre.rendre()

livre.set_un_titre("La Peur du Sage")
livre.set_un_auteur("Patrick Rothfuss et Ollivier Pourriol")

livre.set_disponible(False)

# Affichage des valeurs modifiées
print("Nouveau titre:", livre.get_un_titre())
print("Nouvel auteur:", livre.get_un_auteur())
print("Nouveau nombre de pages:", livre.get_un_nombre_de_pages())
print("Disponible:",livre.verification())