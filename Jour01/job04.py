class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return  f"Je m'appelle {self.nom} {self.prenom}"    