#PUNTO 1
productos = ["Arroz", "Fideos", "Leche", "Aceite"]

print(productos)

#PUNTO 2
print(productos[0])
print(productos[3])

#PUNTO3
precios = [1200, 900, 1500, 3200]
precios[1] = 850
[1200, 850, 1500, 3200]
print(precios)

#PUNTO 4
productos.append("Yerba")
precios.append(2500)
print(productos)
print(precios)

#PUNTO 5 
cantidad = len(productos)
len(productos)
print("El sistema registra", cantidad, "productos en total")

#punto 6
productos.remove("Fideos")
precios. remove(850)
print(productos)
print(precios)

#Punto 7 - Bucle for + input()
nuevos_clientes = ["Juan", "Carlos", "Ernesto", "Gustavo"]
print("clientes")
nuevos_clientes = []

for i in range(4):
    i+1
    nombre = input("Ingrese el nombre del cliente: ")
    nuevos_clientes.append(nombre)
 
    
print(nuevos_clientes)

#PUNTO 8 FOR RANGE INDICES
for i in range(len(precios)):
    print(f"Producto N° {i+1} - Precio: ${precios[i]}")
    
    
    #PUNTO 9 BUCLE WHILE
    marcas_proveedor = {} 

while True:
    marcas = input("Ingrese marca del proveedor (0 para terminar): ")

    if marcas == "0":
        break

    marcas_proveedor.append(marcas)

print(marcas_proveedor)

#PUNTO 10 Alerta: Producto de alto costo

for precio in precios:
    if precio > 1500:
        

