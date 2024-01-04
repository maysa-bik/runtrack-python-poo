class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def augmenter_Population(self):
        self.__nombre_habitants += 1

class Personne:
    def __init__(self, nom, âge, ville):
        self.__nom = nom 
        self.__âge = âge 
        self.__ville = ville

    def ajouter_Population(self):
        self.__ville.augmenter_Population()

Paris = Ville("Paris", 1000000)     
print(f"Population de la ville de Paris: {Paris.get_nombre_habitants()} habitants") 
Marseille = Ville("Marseille", 861635)
print(f"Population de la ville de Marsille: {Marseille.get_nombre_habitants()} habitants")

John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloé = Personne("Chloé", 18, Marseille)


# Ajout des nouvelles personnes
John.ajouter_Population()
Myrtille.ajouter_Population()
Chloé.ajouter_Population()

print(f"Mise à jour de la population de la ville de Paris {Paris.get_nombre_habitants()}, habitants")
print(f"Mise à jour de la population de la ville de Marseille {Marseille.get_nombre_habitants()}, habitants")