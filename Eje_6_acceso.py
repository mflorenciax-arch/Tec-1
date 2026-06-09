# --- PROGRAMA: CONTROL DE ACCESO ---

# 1. Pedimos el año de nacimiento. 
# Recordá que input() recibe texto, por eso usamos int() para pasarlo a número.
anio_nacimiento = int(input("Por favor, ingresá tu año de nacimiento: "))

# 2. Calculamos la edad.
# Como el enunciado asume que estamos en 2026, restamos el año ingresado.
anio_actual = 2026
edad = anio_actual - anio_nacimiento

# 3. Estructura Condicional (IF / ELSE)
# Evaluamos si la edad es mayor o igual a 18.
if edad >= 18:
    # Si la condición es VERDADERA, entra acá:
    print("Tu edad es:", edad)
    print("Acceso Permitido")
else:
    # Si la condición es FALSA, entra acá:
    print("Tu edad es:", edad)
    print("Acceso Denegado")