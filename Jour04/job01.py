class Personne:
    def __init__(self):
        self._age = 14

    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age     

    def afficherAge(self):
        print("J'ai:", self._age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouveau_age):
        self._age = nouveau_age
        

class Eleve(Personne):
    def __init__(self,):
        Personne.__init__(self) 

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.get_age(), "ans")  

class Professeur(Personne):
    def __init__(self, matiereEnseignée):
        self.matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("le cours va commencer" )



Kamelia = Eleve()

Kamelia.bonjour()
Kamelia.modifierAge(29)
Kamelia.afficherAge()
Kamelia.allerEnCours()

professeur1 = Professeur("Histoire")
professeur1.bonjour()
professeur1.enseigner()


