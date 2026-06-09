# --- PROGRAMA: REPARTIDOR DE CARAMELOS ---

# 1. Pedimos al usuario que ingrese la cantidad total de caramelos.
# Usamos int() para convertir el texto que ingresa el usuario en un número entero.
caramelos_totales = int(input("Ingresá la cantidad de caramelos que tiene el abuelo: "))

# 2. Definimos la cantidad de nietos (en este caso son 3).
nietos = 3

# 3. Calculamos cuántos caramelos le tocan a cada uno.
# Usamos la división entera (//) para que no nos de números con coma.
cada_uno = caramelos_totales // nietos

# 4. Calculamos cuántos caramelos sobran (el resto).
# Para esto usamos el operador Módulo (%), que nos devuelve el resto de la división.
sobran = caramelos_totales % nietos

# 5. Mostramos los resultados por pantalla.
print("--- RESULTADOS DEL REPARTO ---")
print("A cada nieto le tocan:", cada_uno, "caramelos.")
print("En la bolsa sobran:", sobran, "caramelos.")  