import os
import readchar
from readchar import key

def cadena_a_matriz(mapa_str):
    filas = mapa_str.strip().split('\n')
    laberinto = []
    for fila in filas:
        caracteres = list(fila)
        laberinto.append(caracteres)
    return laberinto

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_laberinto(mapa):
    limpiar_pantalla()
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial
    
    while (px, py) != posicion_final:
        mapa[py][px] = 'P'
        mostrar_laberinto(mapa)
        
        tecla = readchar.readkey()
        
        if tecla == key.UP:
            if py > 0 and mapa[py - 1][px] != '#':
                mapa[py][px] = '.'
                py -= 1
        elif tecla == key.DOWN:
            if py < len(mapa) - 1 and mapa[py + 1][px] != '#':
                mapa[py][px] = '.'
                py += 1
        elif tecla == key.LEFT:
            if px > 0 and mapa[py][px - 1] != '#':
                mapa[py][px] = '.'
                px -= 1
        elif tecla == key.RIGHT:
            if px < len(mapa[0]) - 1 and mapa[py][px + 1] != '#':
                mapa[py][px] = '.'
                px += 1
        elif tecla == 'q':
            print("Saliendo del programa...")
            break

print("Presiona 'q' en cualquier momento para salir del programa.")
mapa_str = """
...############################
......#..#.....#..#...........#
####..#..####..#..#..#..#..#..#
#..#...........#.....#..#..#..#
#..####..#..#############..#..#
#........#...........#.....#..#
#..#############..##########..#
#..#..#..#...........#........#
####..#..#..#######..#..#######
#..#..#........#...........#..#
#..#..####..#..####..####..#..#
#..#........#..#.....#........#
#..###################..#..####
#.....#..#.....#..#.....#.....#
#..####..#..####..##########..#
#........#..#..............#..#
####..####..#..#..#######..#..#
#..#..#........#........#..#..#
#..#..#..#..#..####..#######..#
#........#..#..#..............
############################..
"""

matriz_laberinto = cadena_a_matriz(mapa_str)
posicion_inicial = (3, 1)  
posicion_final = (9, 18)   
main_loop(matriz_laberinto, posicion_inicial, posicion_final)
