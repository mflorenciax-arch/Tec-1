def ValidarStock(actual, minimo):
    if actual <= minimo:
        return True
    else:
        return False
    # completar


producto = input("Ingrese el nombre del producto: ")
stock_actual = int(input("Ingrese el stock actual: "))
stock_minimo = int(input("Ingrese el stock mínimo: "))

#validar funcion
if ValidarStock(stock_actual, stock_minimo):
    print("¡ATENCIÓN! Es hora de pedir más", producto)
else:
    print("Stock seguro de", producto)


# completar mensajes