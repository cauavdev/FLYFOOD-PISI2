from itertools import permutations
from utils.distancia import calcular_distancia_rota, formatar_rota


def calcular_melhor_rota(matriz):
    pontos = list(matriz.obter_pontos_entrega().keys())

    if not pontos:
        return [], 0

    melhor_rota = None
    melhor_distancia = float('inf')

    for permutacao in permutations(pontos):
        rota_candidata = list(permutacao)
        distancia = calcular_distancia_rota(matriz, rota_candidata)

        if distancia < melhor_distancia:
            melhor_distancia = distancia
            melhor_rota = rota_candidata

    return melhor_rota, melhor_distancia


if __name__ == '__main__':
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from models.matriz import Matriz

    matriz = Matriz(0, 0)
    matriz.carregar_de_arquivo('input/matriz_entrada.txt')

    rota_otima, dist_otima = calcular_melhor_rota(matriz)
    print(f"Resposta: \"{formatar_rota(rota_otima)}\"")
    print(f"Distância: {dist_otima} dronômetros")