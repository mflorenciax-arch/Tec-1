def CalcularPromocion3x2(precio_unitario):
    return precio_unitario * 2
def CalcularPromocion3x2(precio_unitario):
    return precio_unitario * 2


precio = float(input("Ingrese el precio del producto: "))
combos = int(input("Ingrese la cantidad de combos: "))
monto_final = CalcularPromocion3x2(precio) * combos

precio_normal = precio * 3 * combos

ahorro = precio_normal - monto_final
print("El cliente ahorró:", ahorro)
print("Total a pagar:", monto_final)






    