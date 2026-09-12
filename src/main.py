import sys
from models.matriz import Matriz
from utils.matriz_utils import validar_matriz, exibir_resumo_matriz


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

if __name__ == '__main__':
    main()