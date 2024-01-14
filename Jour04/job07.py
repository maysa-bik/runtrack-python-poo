class Carte:
    def __init__(self, valeur, couleur, type):
        self.__valeur = valeur
        self.__couleur = couleur
        self.__type = type
    def __str__(self):
        return f"{self.__valeur} de {self.__couleur} de {self.__type}"
    def get_valeur(self):
        return self.__valeur
import random

class Jeu:
    def __init__(self):
        self.cartes = []
        self.couleur = ["Cœur", "Carreau", "Trèfle", "Pique"]
        self.valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]

        # Initialisez le jeu avec toutes les cartes possibles
        self.initialiser_cartes()

    def initialiser_cartes(self):
        self.cartes = [Carte(valeur, couleur, "Normal") for valeur in self.valeurs for couleur in self.couleur]

    def get_couleur(self):
        return self.couleur
    
        
    def melanger_cartes(self):
        random.shuffle(self.cartes)
        #La fonction shuffle garantit un mélange aléatoire des cartes, rendant le jeu plus imprévisible et plus équitable pour tous les joueurs.
    
    def distribuer_cartes(self, nombre):
        return [self.cartes.pop() for _ in range(nombre)]
    #La méthode distribuer_cartes permet de donner un nombre spécifié de cartes au joueur (ou au croupier). Elle utilise la méthode pop pour retirer ces cartes de l'ensemble de cartes du jeu.

    def calculer_total_points(self, main):
        total = 0
        as_present = False

        for carte in main:
            if carte.get_valeur.isdigit():
                total += int(carte.get_valeur)
            elif carte.valeur in ["J", "Q", "K"]:
                total += 10
            elif carte.get_valeur == "A":
                total += 11
                as_present = True

        while total > 21 and as_present:
            total -= 10
            as_present = False

        return total
# Exemple d'utilisation
jeu_blackjack = Jeu()
main_joueur = jeu_blackjack.distribuer_cartes(2)
total_joueur = jeu_blackjack.calculer_total_points(main_joueur)

print(f"Main du joueur : {[str(carte) for carte in main_joueur]}, Total : {total_joueur}")

"""
class Jeu:
    def __init__(self):
        self.cartes = self.initialiser_cartes()
        self.melanger_cartes()

    def initialiser_cartes(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  
        types = ["Pique", "Cœur", "Carreau", "Trèfle"]
        return [Carte(valeur, type) for valeur in valeurs for type in types]
    
    def melanger_cartes(self):
        random.shuffle(self.cartes)
        #La fonction shuffle garantit un mélange aléatoire des cartes, rendant le jeu plus imprévisible et plus équitable pour tous les joueurs.
"""    
