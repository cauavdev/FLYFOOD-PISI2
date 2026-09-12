import sys
from models.matriz import Matriz

def main():
    print("=" * 20)
    print("FlyFood - PISI-2")
    print("=" * 20)
    
    matriz = Matriz(0, 0)
    
    caminho_entrada = "input/matriz_entrada.txt"
    print(f"\ncarregando arquivo: {caminho_entrada}")
    
    if not matriz.carregar_do_arquivo(caminho_entrada):
        print("falha ao carregar arquivo!")
        return
    
    print("arquivo carregado!")
    
    print("\nMatriz Carregada")
    matriz.exibir()



if __name__ == "__main__":
    main()