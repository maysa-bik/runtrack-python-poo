class Animal:
    def __init__(self, age=0, prenom=" "):
        self.age = age 
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

    def nommer(self, nouveau_nom) :
        self.prenom = nouveau_nom


mon_animal = Animal()

print(f"L'age de l'animal {mon_animal.prenom}{mon_animal.age} ans ")

mon_animal.vieillir()
print(f"L'age de l'animal {mon_animal.prenom}{mon_animal.age} ans")

mon_animal.nommer("Luna")
print(f"L'animal se nomme {mon_animal.prenom}")
