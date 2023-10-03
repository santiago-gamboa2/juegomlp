import os
import random
import readchar
from readchar import key
from functools import reduce

class Juego:
    def __init__(self, nb_jugador, mapa, posicion_inicial, posicion_final):
        self.nb_jugador = nb_jugador
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def cadena_a_matriz(self, mapa_str):
        filas = list(map(list, mapa_str.strip().split('\n')))
        return filas

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_laberinto(self):
        self.limpiar_pantalla()
        for fila in self.mapa:
            fila_sin_coordenadas = ' '.join(['.' if c.isdigit() else c for c in fila])
            print(fila_sin_coordenadas)
        print("Presiona 'q' en cualquier momento para salir del programa.")

    def main_loop(self):
        px, py = self.posicion_inicial
        mapa_alto = len(self.mapa)
        mapa_ancho = len(self.mapa[0])

        while True:
            self.mapa[py][px] = 'P'
            self.mostrar_laberinto()
            tecla = readchar.readkey()

            if tecla == 'q':
                print(f"Saliendo del programa, {self.nb_jugador}...")
                return

            if tecla == key.UP:
                if py > 0 and self.mapa[py - 1][px] != '#':
                    self.mapa[py][px] = '.'
                    py -= 1
            elif tecla == key.DOWN:
                if py < mapa_alto - 1 and self.mapa[py + 1][px] != '#':
                    self.mapa[py][px] = '.'
                    py += 1
            elif tecla == key.LEFT:
                if px > 0 and self.mapa[py][px - 1] != '#':
                    self.mapa[py][px] = '.'
                    px -= 1
            elif tecla == key.RIGHT:
                if px < mapa_ancho - 1 and self.mapa[py][px + 1] != '#':
                    self.mapa[py][px] = '.'
                    px += 1

            if (px, py) == self.posicion_final:
                print("¡Ganaste!")
                self.mostrar_laberinto()
                return

class JuegoArchivo(Juego):
    def __init__(self, nb_jugador, mapa_folder, posicion_inicial, posicion_final):
        self.mapa_folder = mapa_folder
        super().__init__(nb_jugador, [], posicion_inicial, posicion_final)
        self.cargar_mapa_aleatorio()

    def cargar_mapa_aleatorio(self):
        archivos = os.listdir(self.mapa_folder)
        if not archivos:
            raise FileNotFoundError("No se encontraron mapas en la carpeta especificada.")
        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(self.mapa_folder, nombre_archivo)
        
        with open(path_completo, "r") as archivo_mapa:
            lineas = archivo_mapa.readlines()
            mapa_str = reduce(lambda x, y: x + y, lineas)
            
            self.mapa = self.cadena_a_matriz(mapa_str)
            inicio, fin = self.encontrar_inicio_y_fin(mapa_str)
            self.posicion_inicial = inicio
            self.posicion_final = fin

    def encontrar_inicio_y_fin(self, mapa_str):
        filas = list(map(list, mapa_str.strip().split('\n')))
        inicio = (0, 0)
        fin = (len(filas[0]) - 1, len(filas) - 1)

        if inicio is None or fin is None:
            raise ValueError("El mapa no contiene coordenadas de inicio o fin válidas.")
        return inicio, fin

if __name__ == "__main__":
    nb_jugador = input("HOLA BIENVENIDO, por favor ingresa tu nombre: ")
    print(f"BIEN HECHO, {nb_jugador}")

    while True:
        respuesta = input("¿Estás listo para jugar? (responde 'si' o 'no'): ").lower()
        if respuesta == "si":
            break
        elif respuesta == "no":
            print(f"Oh, tal vez en otro momento, {nb_jugador}. ¡Hasta luego!")
            exit()
        else:
            print("Respuesta no válida. Por favor, responde 'si' o 'no'.")

    mapa_folder = "mapas/"

    posicion_inicial_mapa1 = (0, 0)
    posicion_final_mapa1 = (20, 20)
    juego_mapa1 = JuegoArchivo(nb_jugador, mapa_folder, posicion_inicial_mapa1, posicion_final_mapa1)
    juego_mapa1.main_loop()

    print(f"¡Felicidades, {nb_jugador}! Has completado el primer mapa.")
