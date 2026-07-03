# -------------------------------------
# BLOQUE DE LÓGICA / CÁLCULO
# -------------------------------------

def calcular_total_con_descuento(precio_base, descuento):
    total_final = precio_base - (precio_base * descuento / 100)
    return total_final


# -------------------------------------
# BLOQUE DE INTERFAZ / PRESENTACIÓN
# -------------------------------------

def mostrar_ticket(precio_original, precio_final):

    print("=" * 35)
    print("       COMERCIO LOCAL")
    print("=" * 35)

    print(f"Subtotal:      ${precio_original:.2f}")
    print(f"Total a pagar: ${precio_final:.2f}")

    print("=" * 35)
    print("¡Gracias por su compra!")
    print("=" * 35)


# -------------------------------------
# BLOQUE PRINCIPAL / ORQUESTADOR
# -------------------------------------

def ejecutar_sistema():

    precio = float(input("Ingrese el monto de la compra: $"))
    descuento = float(input("Ingrese el descuento (%): "))

    total = calcular_total_con_descuento(precio, descuento)

    mostrar_ticket(precio, total)


# Inicio del programa
ejecutar_sistema()# -------------------------------------
# BLOQUE DE LÓGICA / CÁLCULO
# -------------------------------------

def calcular_total_con_descuento(precio_base, descuento):
    total_final = precio_base - (precio_base * descuento / 100)
    return total_final


# -------------------------------------
# BLOQUE DE INTERFAZ / PRESENTACIÓN
# -------------------------------------

def mostrar_ticket(precio_original, precio_final):

    print("=" * 35)
    print("       COMERCIO LOCAL")
    print("=" * 35)

    print(f"Subtotal:      ${precio_original:.2f}")
    print(f"Total a pagar: ${precio_final:.2f}")

    print("=" * 35)
    print("¡Gracias por su compra!")
    print("=" * 35)


# -------------------------------------
# BLOQUE PRINCIPAL / ORQUESTADOR
# -------------------------------------

def ejecutar_sistema():

    precio = float(input("Ingrese el monto de la compra: $"))
    descuento = float(input("Ingrese el descuento (%): "))

    total = calcular_total_con_descuento(precio, descuento)

    mostrar_ticket(precio, total)


# Inicio del programa
ejecutar_sistema()# -------------------------------------
# BLOQUE DE LÓGICA / CÁLCULO
# -------------------------------------

def calcular_total_con_descuento(precio_base, descuento):
    total_final = precio_base - (precio_base * descuento / 100)
    return total_final


# -------------------------------------
# BLOQUE DE INTERFAZ / PRESENTACIÓN
# -------------------------------------

def mostrar_ticket(precio_original, precio_final):

    print("=" * 35)
    print("       COMERCIO LOCAL")
    print("=" * 35)

    print(f"Subtotal:      ${precio_original:.2f}")
    print(f"Total a pagar: ${precio_final:.2f}")

    print("=" * 35)
    print("¡Gracias por su compra!")
    print("=" * 35)


# -------------------------------------
# BLOQUE PRINCIPAL / ORQUESTADOR
# -------------------------------------

def ejecutar_sistema():

    precio = float(input("Ingrese el monto de la compra: $"))
    descuento = float(input("Ingrese el descuento (%): "))

    total = calcular_total_con_descuento(precio, descuento)

    mostrar_ticket(precio, total)


# Inicio del programa
ejecutar_sistema()