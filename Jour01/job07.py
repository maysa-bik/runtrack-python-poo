class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1     

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return(self.x, self.y)

Personnage = Personnage()

print("Position initiale :", Personnage.position())
# Déplacer vers la droite
Personnage.droite()
print("Position après déplacement à droite :", Personnage.position())

# Déplacer vers le bas
Personnage.bas()
print("Position après déplacement vers le bas :", Personnage.position())

# Déplacer vers la gauche
Personnage.gauche()
print("Position après déplacement à gauche :", Personnage.position())

# Déplacer vers le haut
Personnage.haut()
print("Position après déplacement vers le haut :", Personnage.position())
        