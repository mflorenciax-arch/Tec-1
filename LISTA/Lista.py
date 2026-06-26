# Variable normal (una cosa)
nombre = "Ana"

# Lista (varias cosas)
nombres = ["Ana", "Luis", "Carlos", "Maria"]
print([nombres])

# Crear listas
vacia = []
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", 3.14, True]
print([numeros])


# Acceder por índice (¡empieza en 0!)
print(numeros[0]) # 1
print(numeros[2]) # 3
print(numeros[-1]) # 5 (el último)

# Modificar un elemento
numeros[1] = 20
print(numeros) # [1, 20, 3, 4, 5]

#ejemplo
numeros=[3,5,7,8]
#CALCULAR EL PROMEDIO DE ESOS NROS

# lista con FOR IN

nros = [3, 5, 7, 8]

suma = 0
cant = len(nros)

for i in nros:
    suma = suma + i

promedio = suma / cant

print("La suma es:", suma)
print("El promedio es:", promedio)

#posicion en la lista de un nro USANDO INDEX
nros = [3, 5, 7, 8]

posicion = nros.index(7)

print(posicion)

#posicion de un nro en la lista
posicion = nros.index(7)

print("El 7 está en la posición", posicion)

#Si esta el nro en la lista#
nros = [3, 5, 7, 8]

buscar = int(input("Ingrese un número: "))

if buscar in nros:
    print("Está en la posición:", nros.index(buscar))
else:
    print("El número no se encuentra en la lista")
    
    #USANDO FOR#
    nros = [3, 5, 7, 8]

for i in range(len(nros)):
    if nros[i] == 7:
        print("El 7 está en la posición", i)
        nros = [3, 5, 7, 8]

buscar = int(input("Ingrese un número: "))

encontrado = False

for i in range(len(nros)):
    if nros[i] == buscar:
        print("El número está en la posición", i)
        encontrado = True

if encontrado == False:
    print("El número no está en la lista")
    
    
    
    
    
    
    ##AGREGAR UN NRO QUE NO ESTE EN LA LISTA##
    nuevo = int(input("Ingrese un número: "))
nros.append(nuevo)

print(nros)
    