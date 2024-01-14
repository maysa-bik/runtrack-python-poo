class Joueur:
    def __init__(self, nom, numéro, position, nombre_buts_marqués, passes_décisives_effectuées, cartons_jaunes, carton_rouges):
        self.nom = nom 
        self.numéro = numéro
        self.position = position
        self.nombre_buts_marqués = nombre_buts_marqués
        self.passes_décisives_effectuées = passes_décisives_effectuées
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = carton_rouges

    def marquerUnBut(self):
        self.nombre_buts_marqués += 1
    def effectuerUnePasseDecisive(self):
        self.passes_décisives_effectuées += 1
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    def afficherStatistiques(self):
        print(f"Joueur: {self.nom}")
        print("Nombre de buts marqués: {self.nombre_buts_marqués}")
        print(f"Nombre de passes décisives effesctuées: {self.passes_décisives_effectuées}")
        print(f"Nombre de cartons jaunes reçus:{self.cartons_jaunes}")
        print(f"Nombre de cartons rouges reçus: {self.cartons_rouges}")

class équipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, nombre_buts_marqués, passes_décisives_effectuées, cartons_jaunes, cartons_rouges):
        joueur.nombre_buts_marqués = nombre_buts_marqués
        joueur.passes_décisives_effectuées = passes_décisives_effectuées
        joueur.cartons_jaunes = cartons_jaunes
        joueur.carton_rouges = cartons_rouges


# Créez plusieurs joueurs avec les paramètres de votre choix
joueur1 = Joueur("John Doe", 10, "Ailier", 0, 0, 0, 0)
joueur2 = Joueur("Jane Smith", 20, "Centre", 0, 0, 0, 0)
joueur3 = Joueur("Alice Johnson", 7, "Milieu", 0, 0, 0, 0)
joueur4 = Joueur("Bob Brown", 15, "Défenseur", 0, 0, 0, 0)


# Créez une équipe et ajoutez-y des joueurs
equipe1 = équipe("Les Alouettes")
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)

# Afficher les statistiques des joueurs de l'équipe
equipe1.AfficherStatistiquesJoueurs()

# Simulez un match et mettez à jour les statistiques des joueurs
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur1.recevoirUnCartonJaune()
joueur2.recevoirUnCartonRouge()

# Afficher à nouveau les statistiques des joueurs de l'équipe
equipe1.AfficherStatistiquesJoueurs()
