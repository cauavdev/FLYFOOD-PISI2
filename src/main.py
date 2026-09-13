import sys
from models.matriz import Matriz
from utils.matriz_utils import validar_matriz, exibir_resumo_matriz
from utils.distancia import calcular_distancia_rota, formatar_rota


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

    print("\n--- Testando Cálculo de Distância ---")
    rota_teste = list(matriz.obter_pontos_entrega().keys())
    print(f'Rota de teste: {formatar_rota(rota_teste)}')
    dist_teste = calcular_distancia_rota(matriz, rota_teste)
    print(f'Distância: {dist_teste} dronômetros')

if __name__ == '_main__':
    main()