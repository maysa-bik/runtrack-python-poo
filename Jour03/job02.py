class CompteBancaire:
    def __init__(self, numéro_compte, nom, prénom, solde, decouvert_autorise):
        self.__numéro_compte = numéro_compte
        self.__nom = nom
        self.__prénom = prénom
        self.__solde = solde
        self.__decouvert_autorise = decouvert_autorise

    def afficher(self):
        print(f"Numéro de compte : {self.__numéro_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prénom}")
        print(f"Solde actuel : {self.__solde} €")
        print(f"Découvert autorisé: {self.__decouvert_autorise}")

    def afficherSolde(self):
        print(f"Le solde du compte est de {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")
       

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert_autorise:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Montant non valide ou solde insuffisant.")
    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print("Application d'agios : {agios} € Nouveau solde : {self.__solde} €")
    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert_autorise:
           self.__solde -= montant
           compte_destinataire.versement(montant)
           print("Virement de {montant} € effectué vers le compte {compte_destinataire.__numéro_compte}.")
        else:
            print("Montant non valide ou solde insuffisant pour effectuer le virement.")   
    


compte = CompteBancaire("24101994", "MOHAMADI", "Kamelia", 300.95, False)
compte2 = CompteBancaire("15042017", "DAG" , "Naro", -150, True)

compte.afficher()
compte2.afficher()
compte.afficherSolde()
compte.versement(1000)
compte.retrait(250)

compte.agios(0.05)

compte.virement(compte2, 200)
compte.afficher()
compte2.afficher()

#compte_avec_decouvert = CompteBancaire("24101994", "MOHAMADI", "Kamelia", 300.95, True)
#compte_avec_decouvert.afficher()
#compte_avec_decouvert.afficherSolde()
#compte_avec_decouvert.retrait(350)
        

