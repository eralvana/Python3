respuesta = "S"
jugada = 0
juego = False
resultado = ""
matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]

def dibuja_tablero():
    print(" %c | %c | %c " % (matriz[0][0],matriz[0][1],matriz[0][2]))
    print("___|___|___")
    print(" %c | %c | %c " % (matriz[1][0],matriz[1][1],matriz[1][2]))
    print("___|___|___")
    print(" %c | %c | %c " % (matriz[2][0],matriz[2][1],matriz[2][2]))

def valida(turno):
    global resultado
    for i in range(0,3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] or matriz[0][i] == matriz[1][i] == matriz[2][i]:
            resultado="Ha ganado " + turno + "."
            return True
        if matriz[0][0] == matriz[1][1] == matriz[2][2] or matriz[0][2] == matriz[1][1] == matriz[2][0]:
            resultado="Ha ganado " + turno + "."
            return True
        if matriz[0][i] not in {"1","2","3"} and matriz[1][i] not in {"4","5","6"} and matriz[2][i] not in {"7","8","9"}:
            resultado="El juago ha quedado en empate."
            return True
        return False

def nuevo_juego():
    for i in range(9):
        matriz[int(i/3)][i%3] = str(i+1)

while respuesta.upper() != "N":
    # respuesta=""
    # resultado=""
    # try:
    #     Turno = "X"
    #     nuevo_juego()
    #     juego = False
        
    #     if respuesta.upper()=="S":
    #         while juego==False:
    #             dibuja_tablero()
    #             print("Juega ",Turno," ",end=":")
    #             try:
    #                 jugada = input("¿Dónde tiras? (Puedes terminar el juego pulsando 'T'):")
    #                 tiro = int(jugada)
    #             except jugada.upper() == "T":
    #                     print("Juego terminado.")
    #                     break
    #             except ValueError:
    #                 print("No es un número.")
    #             else:
    #                 if tiro<=0 or tiro>=10:
    #                     print("Lugar fuera de rango, intente en otro espacio.")
    #                     continue
    #                 elif tiro <=9 and tiro >=1:
    #                         tiro = tiro-1
    #                 if matriz[int(tiro/3)][tiro%3] in {"1","2","3","4","5","6","7","8","9"}:
    #                     matriz[int(tiro/3)][tiro%3] = Turno
    #                     juego=valida(Turno)
    #                     if Turno == "X":
    #                         Turno = "O"
    #                     else:
    #                         Turno = "X"
    #                 else:
    #                     print("Lugar ocupado, intente en otro espacio.")
    #     if resultado != "":
    #         print("¡Fin del juego!")
    #         print(resultado)
    #         dibuja_tablero()
    #     respuesta=input("¿Quieres jugar otra vez? (S/N)>")
print("Juego terminado.")