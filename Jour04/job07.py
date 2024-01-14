import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.couleur} {self.valeur}"

class Jeu:
    def __init__(self):
        self.paquet = []
        self.construire_paquet()
        self.joueur = []
        self.croupier = []

    def construire_paquet(self):
        for couleur in ["Cœurs", "Piques", "Trèfles", "Carreaux"]:
            for valeur in range(1, 14):
                self.paquet.append(Carte(valeur, couleur))

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self):
        for _ in range(2):
            self.joueur.append(self.paquet.pop())
            self.croupier.append(self.paquet.pop())

    def calculer_points(self, main):
        points = 0
        as_count = 0
        for carte in main:
            points += carte.valeur
            if carte.valeur == 1:
                as_count += 1
        while points < 12 and as_count > 0:
            points += 10
            as_count -= 1
        return points

    def afficher_cartes(self, main):
        for carte in main:
            print(carte, end=' ')
        print(f"Points : {self.calculer_points(main)}")

    def continuer_jouer(self):
        return input("Voulez-vous prendre une autre carte ? (o/n) ").lower() == "o"

    def jouer(self):
        self.melanger_paquet()
        self.distribuer_cartes()
        print("Carte du joueur :", end=' ')
        self.afficher_cartes(self.joueur)

        while self.calculer_points(self.joueur) < 21 and self.continuer_jouer():
            self.joueur.append(self.paquet.pop())
            print("Carte du joueur :", end=' ')
            self.afficher_cartes(self.joueur)

        print("\nCarte du croupier :", end=' ')
        self.afficher_cartes(self.croupier)

        while self.calculer_points(self.croupier) < 17:
            self.croupier.append(self.paquet.pop())
            print("\nCarte du croupier :", end=' ')
            self.afficher_cartes(self.croupier)

        points_joueur = self.calculer_points(self.joueur)
        points_croupier = self.calculer_points(self.croupier)

        if points_joueur > 21:
            print("\nLe joueur a perdu.")
        elif points_croupier > 21:
            print("\nLe croupier a perdu.")
        elif points_joueur > points_croupier:
            print("\nLe joueur a gagné.")
        elif points_joueur == points_croupier:
            print("\nÉgalité.")
        else:
            print("\nLe croupier a gagné.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()
