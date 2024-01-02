class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ( {self.x}, {self.y})")  

    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")  

    def afficherY(self):
        print(f"La coordonnée y est : {self.y}")  

    def changerX(self, nouvelle_valeur_x): 
        self.x = nouvelle_valeur_x

    def changerY( self, nouvelle_valeur_y):
        self.y =  nouvelle_valeur_y     
point_instance = Point(3, 7)    
point_instance.afficherLesPoints()
point_instance.afficherX()
point_instance.afficherY()
point_instance.changerX(5)
point_instance.changerY(10)
point_instance.afficherLesPoints()

#________________________________________

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})") 

    def get_x(self):
        return self.x

    def set_x(self,nouvelle_valeur_x):
        self.x = nouvelle_valeur_x 

    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")  

    def get_y(self):
        return self.y

    def set_y(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y  

    def afficherY(self):
        print(f"La coordonnée y est : {self.y}")    

point_instance = Point(95, 15)
point_instance.afficherLesPoints()
point_instance.afficherX()
point_instance.afficherY()  

nouvelle_valeur_x = 15

nouvelle_valeur_y = 4

point_instance.set_x(nouvelle_valeur_x)
point_instance.set_y(nouvelle_valeur_y)

print(f"Nouvelle valeur de x : {point_instance.get_x()}")
print(f"Nouvelle valeur de y : {point_instance.get_y()}")

point_instance.afficherLesPoints()