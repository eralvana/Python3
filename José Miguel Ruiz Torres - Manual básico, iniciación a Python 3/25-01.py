a = float (input("Dame un número real "))
b = float (input("Dame otro número real "))
if a < b:
    print("El segundo número que indicaste es mayor; es decir, ", a , "es menor que ", b)
elif a > b:
    print("El primer número que indicaste es mayor; es decir, ", b , "es menor que ", a)
else :
    print("Cualquier número que indicaste es mayor, pues diste dos números iguales")
input("Pulsa ENTER para finalizar")
