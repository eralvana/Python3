a = int (input("¿Qué calificación tienes? "))
if a < 0:
    print("Hay un error, no puedes tener calificación negativa")
elif a < 5:
    print("Suspenso")
elif a == 5:
    print("Suficiente")
elif a == 6:
    print("Aprobado")
elif a == 7:
    print("Notable")
elif a >= 8:
    print("Sobresaliente")
input("Pulsa ENTER para finalizar")
