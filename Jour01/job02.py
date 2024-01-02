class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

Operation_instance = Operation(12, 3)

print(Operation_instance)

print("Le nombre1 est  :", Operation_instance.nombre1)
print("Le nombre2 est  :", Operation_instance.nombre2)


