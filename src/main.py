import sys
from models.matriz import Matriz
from utils.matriz_utils import validar_matriz, exibir_resumo_matriz
from utils.distancia import calcular_distancia_rota, formatar_rota
from algoritmo.roteamento import calcular_melhor_rota


def main():
    print("=" * 20)
    print("FlyFood - PISI-2")
    print("=" * 20)

    matriz = Matriz(0, 0)
    caminho_entrada = 'input/matriz_entrada.txt'
    print(f"\nCarregando arquivo: {caminho_entrada}")

    if not matriz.carregar_de_arquivo(caminho_entrada):
        print("Falha ao carregar arquivo!")
        return

    print("Arquivo carregado com sucesso!")

    e_valida, mensagem = validar_matriz(matriz)
    print(f"\n{mensagem}")

    if not e_valida:
        print("Não é possível prosseguir, matriz inválida.")
        return

    exibir_resumo_matriz(matriz)

    print("\n--- Calculando Melhor Rota ---")
    melhor_rota, melhor_distancia = calcular_melhor_rota(matriz)
    print(f'Melhor rota: {formatar_rota(melhor_rota)}')
    print(f'Distância: {melhor_distancia} dronômetros')

if __name__ == '__main__':
    main()