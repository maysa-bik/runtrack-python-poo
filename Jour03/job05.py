import random
class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie 

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats
        adversaire.subir_degats(degats)

    def subir_degats(self, degats):
        self.vie -= degats
        if self.vie <= 0:
            print(f"{self.nom} a été vaincu !")
        else:
            print(f"{self.nom} a maintenant {self.vie} points de vie.") 


class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté (1-Facile, 2-Difficile) :")
        self.niveau = int(input())

    def lancerJeu(self):
        self.choisirNiveau()
        # Initialisation des points de vie en fonction du niveau
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50

        elif self.niveau == 2:
            vie_joueur = 50
            vie_ennemi = 100
        # Création des personnages    
        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        # Déroulement du jeu
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{joueur.nom} a gagné !")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{ennemi.nom} a gagné !")
                break

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()


   
