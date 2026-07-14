#FUNCION 1
def CalcularBruto(horas, valor_hora):
    sueldo_bruto = horas * valor_hora
    return sueldo_bruto
#FUNCION 2
def CalcularRetenciones(sueldo_bruto):
    retenciones = sueldo_bruto * 0.17
    return retenciones
#PROGRAMA PRINCIPAL
nombre = input("Ingrese el nombre del empleado: ")
horas = int(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de la hora: "))
bruto = CalcularBruto(horas, valor_hora)

retenciones = CalcularRetenciones(bruto)

neto = bruto - retenciones
print("===== RECIBO DE SUELDO =====")
print("Empleado:", nombre)
print("Sueldo Bruto:", bruto)
print("Retenciones:", retenciones)
print("Sueldo Neto:", neto)
print("===========================")


