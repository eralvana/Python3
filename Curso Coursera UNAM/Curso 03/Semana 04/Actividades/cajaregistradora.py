productos = []
nombre_producto = input("Ingrese el nombre del producto: >")
productos.append(nombre_producto)
precios = []
precio_producto = int(input("Ingrese el precio del producto: >"))
precios.append(precio_producto)
cantidad = []
cantidad_producto = int(input("Ingrese la cantidad de piezas compradas de este producto: >"))
cantidad.append(cantidad_producto)

continuar = True

def calcular_monto():
    valor_monto = 0
    for index in range(len(productos)):
        valor_monto += int(cantidad[index])*int(precios[index])
    return valor_monto

def calcular_subtotal():
    print("SubTotal: $", calcular_monto())

def calcular_total():
    print("Total: $", calcular_monto())

def ingreso():
    nombre_producto = input("Ingrese el nombre del producto: >")
    productos.append(nombre_producto)
    precio_producto = int(input("Ingrese el precio del producto: >"))
    precios.append(precio_producto)
    cantidad_producto = int(input("Ingrese la cantidad de piezas compradas de este producto: >"))
    cantidad.append(cantidad_producto)

def resumen():
    for index in range(len(productos)):
        print(cantidad[index], "pieza(s) de", productos[index], "con un precio unitario de", precios[index], "forman un monto de $",int(cantidad[index])*int(precios[index]))
    calcular_subtotal()
   
def total():
    for index in range(len(productos)):
        print(cantidad[index], "pieza(s) de", productos[index], "con un precio unitario de", precios[index], "forman un monto de $",int(cantidad[index])*int(precios[index]))
    calcular_total()

def descuento():
    resumen()
    print("El monto del descuento es $", valor_descuento)
    print("El monto total a pagar es de $", calcular_monto() - valor_descuento)    


while continuar == True:
    
    try:
        orden = input("¿Desea añadir más articulos? (Indique 'S' para SÍ, 'N' para NO ó 'R' para mostrar un RESUMEN): >")
        
        if orden.upper() == "S":
            ingreso()
        elif orden.upper() == "R":
            resumen()
            continuar = True
        elif orden.upper() == "N":
            continuar = False

    except:
        print("No es una instrucción válida. Intente de nuevo.")

try:
    pregunta_descuento = input("¿Tiene algún descuento? ('S' para SÍ ó 'N' para NO): >")

    if pregunta_descuento.upper() == "S":
        tipo_descuento = input("¿Qué tipo de descuento tiene? (Indique 'M' para ingresar un monto ó 'P' para ingresar un porcentaje): >" )
        try:
            if tipo_descuento.upper() == "M":
                valor_descuento = int(input("Ingrese el monto del descuento: >"))
                descuento()
            elif tipo_descuento.upper() == "P":
                valor_descuento = int(input("Ingrese el porcentaje del descuento: >")) * calcular_monto() / 100
                descuento()
        except:
            print("No es una instrucción válida. Intente de nuevo.")
    elif pregunta_descuento.upper() == "N":
        valor_descuento = 0
        total()
    else:
        print("No es una instrucción válida. Intente de nuevo.")
except:
    print("No es una instrucción válida. Intente de nuevo.")

valor_total = calcular_monto() - valor_descuento

pagado = False

while pagado != True:
    
    try:
        pago = int(input("Ingrese la cantidad de efectivo recibido: >"))
        cambio = pago - valor_total

        if cambio < 0:
            print("El monto indicado no es suficiente.")
        elif cambio == 0:
            print("Traansacción completa, no hay cambio que devolver. Gracias por su compra.")
            pagado = True
        elif cambio >= 0:
            print("Traansacción completa, se debe devolver $", cambio, ". Gracias por su compra.")
            pagado = True
    except ValueError:
        print("El monto indicado no es un valor válido.")