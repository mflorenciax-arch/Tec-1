#PERRO#
class Perro:
    
    def __init__(self, raza, nombre, ciudad, edad):
        self.raza = raza
        self.nombre = nombre
        self.ciudad = ciudad
        self.edad = edad

perro = Perro("Golden Retriever", "Viko", "Bahía Blanca", 9)
perro1 = Perro("Galgo", "Rita", "Bahía Blanca", 2)

print(perro.raza, perro.nombre, perro.ciudad, perro.edad)
print(perro1.raza, perro1.nombre, perro1.ciudad, perro1.edad)

        
