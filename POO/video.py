#EJEMPLO VIDEO#
class Camiseta:
    
    def __init__(self, marca, precio, talla, color):
        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color


camiseta = Camiseta("Gucci", 99, "M", "Negro")
camiseta1 = Camiseta("Nike", 22, "L", "Verde")

print(camiseta.marca, camiseta.precio, camiseta.talla, camiseta.color)
print(camiseta1.marca, camiseta1.precio, camiseta1.talla, camiseta1.color)
