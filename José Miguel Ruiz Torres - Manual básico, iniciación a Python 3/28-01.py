numero = int (input("¿Qué tabla de multiplicar te gustaría conocer? "))
k = 0
while numero <= 0:
    print("Debes introducir un número mayor que cero.")
    numero = int (input("¿Qué tabla de multiplicar (de un número positivo) te gustaría conocer? "))
while k <= 10:
    multiplicacion = numero * k
    print("(", numero ,")(", k ,") = ", multiplicacion)
    k += 1
input("Pulsa ENTER para finalizar")
