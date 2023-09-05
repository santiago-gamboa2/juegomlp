#pedir el nombre del usuario 
nb_jugador = input ("HOLA BIENVENIDO, POR FAVAOR INGRESA TU  NOMBRE:")
#imprimir el nombre del jugador 
print(f"BIENVENIDO,{nb_jugador}!")
##tarea 2 
#impoprtar el readchar
import readchar

print("¡Bienvenido al Juego 'Presiona w para Ganar'!")

while True:
    key = readchar.readkey()[0]  # Captura solo el primer carácter

    # Imprimir la tecla presionada
    print(f"Presiona la tecla : '{key}'")

    # Verificar si la tecla presionada es "w"
    if key == 'w':
        print("¡Felicidades! ¡Presionaste 'w' y Ganaste!")
        break

print("¡Gracias por jugar!")
