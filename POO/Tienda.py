class producto:
    
    def __init__(self, nombre, precio, stock):

        self.nombre = nombre
        self.precio = precio
        self.stock = stock

producto1 = producto("Camiseta", 15.99, 20)
producto2 = producto("Pantalón", 25.50, 15)

print("Producto 1:")
print("Nombre:", producto1.nombre)
print("Precio:", producto1.precio)
print("Stock:", producto1.stock)

print()

print("Producto 2:")
print("Nombre:", producto2.nombre)
print("Precio:", producto2.precio)
print("Stock:", producto2.stock)


            