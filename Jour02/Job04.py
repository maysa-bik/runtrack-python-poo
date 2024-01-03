class Student:
    def __init__(self, nom, prénom, numéro_étudiants, crédits=0):
        self.__nom = nom 
        self.__prénom = prénom
        self.__numéro_étudiants = numéro_étudiants
        self.__crédits = crédits
        self.__level = self.__student_eval()

    def get_nom(self):
        return self.__nom

    def get_prénom(self):
        return self.__prénom

    def get_numéro_étudiants(self):
        return self.__numéro_étudiants

    def get_crédits(self):
        return self.__crédits 

    def get_level(self):
        return self.__level

    def add_credits(self,nomber_credits):
        if nomber_credits > 0:
            self.__crédits += nomber_credits   
            #print(f"{nomber_credits} crédits ajoutés avec succès.")
            self.__level = self.__student_eval()
        else:
            print(f"Errreur : Le nombre de crédits doit être supérieur à zéro.") 

    def __student_eval(self):
        if self.__crédits >= 90:
            return "Excellent"
        elif self.__crédits >= 80:
            return "Très bien"
        elif self.__crédits >= 70:
            return "Bien"
        elif self.__crédits >= 60:
            return "Passable" 
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prénom}")
        print(f"Id = {self.__numéro_étudiants}")
        print(f"Niveau = {self.__level}")            

John_Doe = Student("Doe", "John", 145)            

# Exemple d'utilisation
John_Doe.add_credits(8)
John_Doe.add_credits(15)
John_Doe.add_credits(7)


print(f"Le nombre de crédits de {John_Doe.get_prénom()} {John_Doe.get_nom()} est de {John_Doe.get_crédits()} points")


John_Doe.add_credits(75)  # Ajout de crédits
John_Doe.student_info()  # Affichage des informations de l'étudiant
