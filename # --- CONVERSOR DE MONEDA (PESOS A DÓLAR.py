# --- CONVERSOR DE MONEDA (PESOS A DÓLARES) ---

# 1. ENTRADA DE DATOS
# Usamos float() porque el dinero tiene decimales (coma)
pesos = float(input("Ingrese la cantidad de Pesos Argentinos: "))
tipo_cambio = float(input("Ingrese el precio del Dólar hoy: "))

# 2. PROCESO (Cálculo matemático)
dolares = pesos / tipo_cambio

# 3. SALIDA DE DATOS
# Usamos f-string para mostrar el resultado de forma prolija
print(f"\nCon ${pesos} pesos, podés comprar: U$D {dolares:.2f}")

# El :.2f sirve para que solo muestre 2 números después de la coma