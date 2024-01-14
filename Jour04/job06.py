class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__prix = prix

    def informationsVehicule(self):
        print("La marque:", self.__marque) 
        print("Le modèle:", self.__modèle)
        print("L'année:", self.__année)
        print("Le prix du véhicule:", self.__prix)

    def demarrer(self):
        print("Attention, je roule")    

class Voiture(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        Vehicule.__init__(self, marque, modèle, année, prix)
        self.__portes = 4

    def get_portes(self):
        return self.__portes
    def set_age(self, portes):
        self.__portes = portes  

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nomber de port:", self.__portes)

    def demarrer(self):
        print("La voiture démarre !!")    
        
class Moto(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        Vehicule.__init__(self, marque, modèle, année, prix) 
        self.__roue = 2
    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de roue", self.__roue)

    def demarrer(self):
        print("La moto démarre !!! ")   


# Exemple d'utilisation
vehicule1 = Vehicule("Toyota", "Camry", 2022, 25000)
vehicule1.informationsVehicule()

voiture1 = Voiture("Mercedes", "classe A", 2020, 18500)
voiture1.informationsVehicule() 
voiture1.demarrer()   

# Instancier un objet Moto
moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
# Faire appel à la méthode informationsVehicule
moto1.informationsVehicule()
moto1.demarrer()
