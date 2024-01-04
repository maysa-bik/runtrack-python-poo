class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commande = {}  # Utilisation du même nom ici
        self.__statut = "en cours"

    def ajouter_plat(self, nom_plat, prix_plate):
        if self.__statut == "en cours":
            self.__plats_commande[nom_plat] = {"prix": prix_plate, "statut": "en cours"}  # Utilisation du même nom ici
            print(f"plat ajouté : {nom_plat} - Prix : {prix_plate}")
        else:
            print("Impossible d'ajouter un plat. La commande est terminée ou annulée.")

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande} - Statut: {self.__statut}", end=" ")
        for plat, info in self.__plats_commande.items():  # Utilisation du même nom ici
            print(f"{plat} - Prix: {info['prix']} - Statut: {info['statut']}", end=" ")
        print()

    def calculer_total(self):
        total = 0
        for plat, info in self.__plats_commande.items():  # Utilisation du même nom ici
            if info["statut"] == "en cours":
                total += info["prix"]
        return total

    def calculer_tva(self, taux_tva=0.20):
        total_tva = self.calculer_total() * taux_tva
        return total_tva

    def annuler_commande(self):
        self.__statut = "annulée"
        print("La commande a été annulée.")

# Exemple d'utilisation
commande1 = Commande(1)

commande1.ajouter_plat("Pizza", 15)
commande1.ajouter_plat("Salade", 8)

commande1.afficher_commande()

total_commande = commande1.calculer_total()
print(f"Total à payer : {total_commande} €")

tva_commande = commande1.calculer_tva()
print(f"TVA à payer : {tva_commande} €")

commande1.annuler_commande()
commande1.afficher_commande()





"""
class ville 


class personne
 def ini
marseille = ville("paris", "100000")
pirre = personne("pierre",marseille)
pierre.ville

"""