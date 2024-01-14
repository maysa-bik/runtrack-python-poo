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
    def __init__(self):
        Personne.__init__(self) 

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.get_age(), "ans") 
      

class Professeur(Personne):
    def __init__(self, matiereEnseignée, age):
        Personne.__init__(self)
        self.matiereEnseignée = matiereEnseignée
        self.modifierAge(age)

    def enseigner(self):
        print("Je suis l'enseignant de ", self.matiereEnseignée, "et le cours va commencer")
    

eleve1 = Eleve()

# Utilisation des méthodes pour l'élève
eleve1.bonjour()
eleve1.modifierAge(15)
eleve1.afficherAge() 
eleve1.allerEnCours()  

professeur1 = Professeur("Mathimathique", 40)
professeur1.bonjour()
professeur1.afficherAge()
professeur1.enseigner()


