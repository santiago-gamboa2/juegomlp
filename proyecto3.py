import os
import readchar

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    numero = 0

    while numero <= 50:
        clear_terminal()
        print(f"Número actual: {numero}")
        print("Presiona la tecla 'n' para incrementar el número hasta 50.")

        key = readchar.readkey()[0]  # Captura solo el primer carácter

        if key == 'n':
            numero += 1
        else:
            break

    if numero == 51:
        print("¡Llegaste a 50!")

if __name__ == "__main__":
    main()
