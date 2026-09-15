import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models.matriz import Matriz
from utils.distancia import calcular_distancia_rota
from algoritmo.roteamento import calcular_melhor_rota


def test_melhor_rota_visita_todos_os_pontos():
    matriz = Matriz(0, 0)
    matriz.carregar_de_arquivo('input/matriz_entrada.txt')

    rota, _ = calcular_melhor_rota(matriz)
    pontos_esperados = set(matriz.obter_pontos_entrega().keys())

    assert set(rota) == pontos_esperados, f'Rota deveria conter {pontos_esperados}, obteve {set(rota)}'
    print('test_melhor_rota_visita_todos_os_pontos está tudo certo')


def test_melhor_rota_e_a_menor_possivel():
    matriz = Matriz(0, 0)
    matriz.carregar_de_arquivo('input/matriz_entrada.txt')

    rota, distancia = calcular_melhor_rota(matriz)

    # A rota ótima não pode ser pior que nenhuma outra ordem testada manualmente
    from itertools import permutations
    for permutacao in permutations(matriz.obter_pontos_entrega().keys()):
        dist_alternativa = calcular_distancia_rota(matriz, list(permutacao))
        assert distancia <= dist_alternativa, 'Encontrada rota melhor que a retornada como ótima'

    print(f'test_melhor_rota_e_a_menor_possivel está tudo certo, distancia = {distancia}')


def test_rota_sem_pontos_de_entrega():
    matriz = Matriz(0, 0)
    matriz.dados = [['R']]
    matriz.linhas = 1
    matriz.colunas = 1
    matriz.origem = (0, 0)
    matriz.pontos_entrega = {}

    rota, distancia = calcular_melhor_rota(matriz)
    assert rota == [], 'Rota deveria ser vazia sem pontos de entrega'
    assert distancia == 0, 'Distância deveria ser 0 sem pontos de entrega'
    print('test_rota_sem_pontos_de_entrega está tudo certo')


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("EXECUTANDO TESTES DE ROTEAMENTO")
    print("=" * 50 + "\n")

    try:
        test_melhor_rota_visita_todos_os_pontos()
        test_melhor_rota_e_a_menor_possivel()
        test_rota_sem_pontos_de_entrega()

        print("\n" + "=" * 50)
        print("✓ TODOS OS TESTES PASSARAM!")
        print("=" * 50)

    except AssertionError as e:
        print(f"\n TESTE FALHOU: {e}")

    except Exception as e:
        print(f"\n ERRO: {e}")
        import traceback
        traceback.print_exc()