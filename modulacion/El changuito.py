#FUNCION PARA CALCULAR IVA
def CalcularIVA(monto):
    return monto * 0.21
#FUNCION PARA APLICAR DESCUENTO
def AplicarDescuento(monto):
    return monto - (monto * 0.10)
def CalcularIVA(monto):
    return monto * 0.21

#EJERCICIO COMPLETO
#CALCULAR IVA#CALCULAR DESCUENTO#DECIR I ES JUBILADO O NO

def CalcularIVA(monto):
    return monto * 0.21

def AplicarDescuento(monto):
    return monto * 0.10

precio1 = float(input("Ingrese el precio del producto 1: "))
precio2 = float(input("Ingrese el precio del producto 2: "))
precio3 = float(input("Ingrese el precio del producto 3: "))

subtotal = precio1 + precio2 + precio3

iva = CalcularIVA(subtotal)

total = subtotal + iva

print("\n--- DETALLE DE COMPRA ---")
print("Subtotal: $", subtotal)
print("IVA (21%): $", iva)

jubilado = input("\n¿Es jubilado? (si/no): ")

if jubilado.lower() == "si":
    descuento = AplicarDescuento(total)
    total = total - descuento
    print("Descuento jubilado (10%): $", descuento)

print("Total a pagar: $", total)