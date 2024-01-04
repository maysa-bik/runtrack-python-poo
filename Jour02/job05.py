class Voiture:
    def __init__(self, marque, modèle, année, kilométrage, reservoir=50):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque  
    
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modèle(self):
        return self.__modèle

    def set_modèle(self, nouveau_modèle):
        self.__modèle = nouveau_modèle

    def get_année(self):
        return self.__année

    def set_année(self, nouvelle_année):
        self.__année = nouvelle_année 

    def get_kilométrage(self):
        return self.__kilométrage

    def set_kilométrage(self, nouvelle_kilométrage):
        self.__kilométrage = nouvelle_kilométrage  

    def get_en_march(self):
        return self.__en_marche

    def set_en_marche(self, nouvel_etat):
        self.__en_marche = nouvel_etat

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture est démarrée.")
        else:
            print("La voiture ne peut pas démarrer. Le réservoir est trop bas.")        

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

    # Ajout de l'attribut privé reservoir et de la méthode privée verifier_plein
    def __verifier_plein(self):
        return self.__reservoir > 5    
# Exemple d'utilisation
Audi = Voiture("Audi", "A4", 2020, 5000)   

#print(f"{Audi.get_marque()} {Audi.get_modèle()} {Audi.get_année()} {Audi.get_kilométrage()}")

print(f"La marque est :{Audi.get_marque()}")
print(f"La modèle est : {Audi.get_modèle()}")
print(f"L'année est : {Audi.get_année()}")
print(f"La kilométrage est : {Audi.get_kilométrage()}")
#print(f"En march : {Audi.get_en_march()}")

# Modifier les attributs"
Audi.set_kilométrage(6000)
Audi.set_en_marche(True)
# Utiliser les méthodes demarrer et arreter
#Audi.demarrer()
Audi.arreter()

# Modifier le réservoir (cela peut être fait par des mutateurs appropriés)
Audi.set_en_marche(False)
Audi.__reservoir = 3

# Démarrer la voiture à nouveau (le réservoir est trop bas)
Audi.demarrer()

# Vérifier l'état après démarrage et arrêt
print(Audi.get_en_march())

