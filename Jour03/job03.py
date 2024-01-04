class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{titre}' supprimée.") 
                return
        print(f"Tâche '{titre}' non trouvée.")
    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
            print(f"Tâche '{titre}' non trouvée.")
    def afficherListe(self):
        for tache in self.taches:
            print(tache)
        
    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list
    

# Exemple d'utilisation
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes", "À faire")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 5", "À faire")
tache3 = Tache("Rédiger le rapport", "Analyse des résultats", "À faire")  

liste_taches = ListeDeTaches()
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

liste_taches.afficherListe()

# Supprimer une tâche
liste_taches.supprimerTache("Réviser pour l'examen")

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie("Faire les courses")

# Afficher toutes les tâches
liste_taches.afficherListe()

# Afficher les tâches à faire
taches_a_faire = liste_taches.filterListe("À faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)

        





