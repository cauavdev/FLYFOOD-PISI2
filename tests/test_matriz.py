import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models.matriz import Matriz
from utils.matriz_utils import validar_matriz


def test_carregar_arquivo_valido():
    matriz = Matriz(0, 0)
    resultado = matriz.carregar_de_arquivo('input/matriz_entrada.txt')
    assert resultado == True, 'Retorna True se carregar o arquivo válido'
    print('test_carregar_arquivo_valido está tudo certo')

def test_matriz_tem_origem():
    matriz = Matriz(0, 0)
    matriz.carregar_de_arquivo('input/matriz_entrada.txt')
    origem = matriz.obter_origem()
    assert origem is not None, 'A matriz deve ter uma origem'
    print(f'test_matriz_tem_origem está tudo certo. Origem: {origem}')

def test_matriz_tem_pontos_entrega():
    matriz = Matriz(0, 0)
    matriz.carregar_de_arquivo('input/matriz_entrada.txt')
    pontos = matriz.obter_pontos_entrega()
    assert len(pontos) > 0, 'A matriz deve ter pelo menos um ponto de entrega'
    print(f'test_matriz_tem_pontos_entrega está tudo certo. Qtd pontos: {len(pontos)}')

def test_validacao_matriz_valida():
    matriz = Matriz(0, 0)
    matriz.carregar_de_arquivo('input/matriz_entrada.txt')
    e_valida, mensagem = validar_matriz(matriz)
    assert e_valida == True, f'A matriz deveria ser válida. Mensagem: {mensagem}'
    print('test_validacao_matriz_valida está tudo certo')

def test_arquivo_nao_existe():
    matriz = Matriz(0, 0)
    resultado = matriz.carregar_de_arquivo('input/nao_existe.txt')
    assert resultado == False, 'Retorna False quando o arquivo é inexistente'
    print('test_arquivo_nao_existe está tudo certo')


if __name__ == '__main__':
    print("\n" + "=" * 20)
    print("EXECUTANDO TESTES DA MATRIZ")
    print("=" * 20 + "\n")

    try:
        test_carregar_arquivo_valido()
        test_matriz_tem_origem()
        test_matriz_tem_pontos_entrega()
        test_validacao_matriz_valida()
        test_arquivo_nao_existe()

        print("\n" + "=" * 20)
        print("TODOS OS TESTES PASSARAM!")
        print("=" * 20)

    except AssertionError as e:
        print(f"\nTESTE FALHOU: {e}")

    except Exception as e:
        print(f"\nERRO: {e}")