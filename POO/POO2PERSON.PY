#PERSONA"
class Persona:
    
    def __init__(self, nombre, ciudad, edad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.edad = edad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def mostrar_ciudad(self):
        print(f"{self.nombre} vive en {self.ciudad}")

    def mostrar_edad(self):
        print(f"{self.nombre} tiene {self.edad} años")


persona = Persona("Flor", "Bahía Blanca", 48)
persona1 = Persona("Abby", "Bahía Blanca", 15)
persona2 = Persona("Rocco", "Bahía Blanca", 15)

persona.hablar()
persona.mostrar_ciudad()
persona.mostrar_edad()

persona1.hablar()
persona1.mostrar_ciudad()
persona1.mostrar_edad()

persona2.hablar()
persona2.mostrar_ciudad()
persona2.mostrar_edad()


      
            
            
            
            
            
            
            
            
            
            
            
            
    

    