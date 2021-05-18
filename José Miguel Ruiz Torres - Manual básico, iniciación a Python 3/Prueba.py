# Este programa comprueba si un número es positivo o negativo:
num = int (input('Introduzca un número')) # Pido un número al usuario.
if num < 0:
    print(num, 'es un número negativo.')
elif num > 0:
    print(num, 'es un número positivo.')
elif num == 0:
    print(num, 'no pertenece a ningún grupo.')
input('Pulse INTRO para finalizar...') # Hago una pausa.
