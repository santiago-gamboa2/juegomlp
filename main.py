#pedir el nombre del usuario 
nb_jugador = input ("HOLA BIENVENIDO, POR FAVAOR INGRESA TU  NOMBRE:")
#imprimir el nombre del jugador 
print(f"BIENVENIDO,{nb_jugador}!")
##tarea 2 
#impoprtar el readchar
import readchar

print("¡Bienvenido al Juego 'Presiona flecha up para Ganar'!")

while True:
    key = readchar.readkey()  # Captura solo el primer carácter

    # Imprimir la tecla presionada
    print(f"Presiona la tecla : '{key}'")

    # Verificar si la tecla presionada es up 
    if key == readchar.key.UP:
        print("¡Felicidades! ¡Presionaste la flacha up y Ganaste!")
        break

print("¡Gracias por jugar!")