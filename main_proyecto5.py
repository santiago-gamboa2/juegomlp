import os
import random

class Juego:
    def __init__(self, nb_jugador, mapa, posicion_inicial, posicion_final):
        self.nb_jugador = nb_jugador
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def cadena_a_matriz(self, mapa_str):
        filas = mapa_str.strip().split('\n')
        laberinto = []
        for fila in filas:
            caracteres = list(fila)
            laberinto.append(caracteres)
        return laberinto

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_laberinto(self):
        self.limpiar_pantalla()
        for fila in self.mapa:
            print(''.join(fila))
        print("Presiona 'q' en cualquier momento para salir del programa.")

    def main_loop(self):
        px, py = self.posicion_inicial
        
        while (px, py) != self.posicion_final:
            self.mapa[py][px] = 'P'
            self.mostrar_laberinto()
            
            tecla = input("Presiona una tecla: ")

            if tecla == 'q':
                print(f"Saliendo del programa, {self.nb_jugador}...")
                break

            if tecla == 'w':
                if py > 0 and self.mapa[py - 1][px] != '#':
                    self.mapa[py][px] = '.'
                    py -= 1
            elif tecla == 's':
                if py < len(self.mapa) - 1 and self.mapa[py + 1][px] != '#':
                    self.mapa[py][px] = '.'
                    py += 1
            elif tecla == 'a':
                if px > 0 and self.mapa[py][px - 1] != '#':
                    self.mapa[py][px] = '.'
                    px -= 1
            elif tecla == 'd':
                if px < len(self.mapa[0]) - 1 and self.mapa[py][px + 1] != '#':
                    self.mapa[py][px] = '.'
                    px += 1

        print("El juego ha terminado. ¡Gracias por jugar!")

class JuegoArchivo(Juego):
    def __init__(self, nb_jugador, mapa_folder):
        self.mapa_folder = mapa_folder
        super().__init__(nb_jugador, [], (0, 0), (0, 0))  
        self.cargar_mapa_aleatorio()

    def cargar_mapa_aleatorio(self):
        archivos = os.listdir(self.mapa_folder)
        if not archivos:
            raise FileNotFoundError("No se encontraron mapas en la carpeta especificada.")

        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(self.mapa_folder, nombre_archivo)

        with open(path_completo, "r") as archivo_mapa:
            mapa_str = archivo_mapa.read()
            self.mapa = self.cadena_a_matriz(mapa_str)

            inicio, fin = self.encontrar_inicio_y_fin(mapa_str)
            self.posicion_inicial = inicio
            self.posicion_final = fin

    def encontrar_inicio_y_fin(self, mapa_str):
        filas = mapa_str.strip().split('\n')
        inicio = None
        fin = None

        for y, fila in enumerate(filas):
            for x, caracter in enumerate(fila):
                if caracter == 'P':
                    inicio = (x, y)
                elif caracter == '.':
                    fin = (x, y)

        if inicio is None or fin is None:
            raise ValueError("El mapa no contiene coordenadas de inicio o fin válidas.")

        return inicio, fin

if __name__ == "__main__":
    nb_jugador = input("HOLA BIENVENIDO, por favor ingresa tu nombre: ")
    print(f"BIEN HECHO, {nb_jugador}")

    respuesta = input("¿Estás listo para jugar? (responde 'si' o 'no'): ").lower()

    if respuesta == "si":
        print("¡Genial! Comencemos el juego.")
        mapa_folder = "C:/Users/USUARIO/Desktop/mapas"

        juego = JuegoArchivo(nb_jugador, mapa_folder)
        juego.main_loop()
    elif respuesta == "no":
        print(f"Oh, tal vez en otro momento, {nb_jugador}. ¡Hasta luego!")
    else:
        print("No comprendo tu respuesta. Por favor, responde 'si' o 'no'.")
