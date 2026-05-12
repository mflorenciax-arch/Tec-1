# 1. Declaramos la variable inicial
numero = int(input("Ingrese un número para comenzar el bucle: "))

# 2. El bucle 'Mientras' (while)
# Se lee: "Mientras numero sea menor o igual a 10, hacé lo siguiente"
while numero <= 10 or numero == 0:
    print(f"El número actual es: {numero}")
    
    # 3. El acumulador / contador
    # Le sumamos 1 en cada repetición
    numero = numero + 1

print("¡Llegamos a 10! El bucle terminó.")