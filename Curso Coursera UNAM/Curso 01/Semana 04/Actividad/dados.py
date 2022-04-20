import random
def tirardados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print("Tu primer dado obtuvo el valor", dado1, "y tu segundo dado tuvo el valor", dado2)
    print("De esta manera la suma de los valores de tus dados es", dado1 + dado2)

comando = input("¿Quieres tirar los dados? (Presiona 0 para terminar y 1 para tirar)>")
while comando != "0":
    if comando == "1":
        tirardados()
        comando = input("¿Quieres tirar los dados? (Presiona 0 para terminar y 1 para tirar)>")
    else :
        print("Tu elección no es válida")
        comando = input("¿Quieres tirar los dados? (Presiona 0 para terminar y 1 para tirar)>")

print("¡Perfecto!, nos vemos luego.")