import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models.matriz import Matriz
from utils.distancia import calcular_distancia_manhattan, calcular_distancia_rota


def test_distancia_simples():
    dist = calcular_distancia_manhattan((0,0), (3,4))
    assert dist == 7, f'Resultado esperado: 7. Obteve {dist}'
    print('test_distancia_simples está tudo certo')

def test_distancia_mesmo_ponto():
    dist = calcular_distancia_manhattan((5, 5), (5, 5))
    assert dist == 0, f'Resultado esperado: 0. Obteve {dist}'
    print('test_distancia_mesmo_ponto está tudo certo')

def test_distancia_horizontal():
    dist = calcular_distancia_manhattan((0, 0), (0, 5))
    assert dist == 5, f'Resultado esperado: 5. Obteve {dist}'
    print('test_distancia_horizontal está tudo certo')

def test_distancia_vertical():
    dist = calcular_distancia_manhattan((0, 0), (3, 0))
    assert dist == 3, f'Resultado esperado: 3. Obteve {dist}'
    print('test_distancia_vertical está tudo certo')

def test_distancia_rota_simples():
    matriz = Matriz(0, 0)
    matriz.carregar_de_arquivo('input/matriz_entrada.txt')

    rota = ['A', 'B', 'C', 'D']
    distancia = calcular_distancia_rota(matriz, rota)

    assert distancia > 0, 'Distância deve ser positiva'
    print(f'test_distancia_rota_simples está tudo certo, distancia = {distancia}')

def test_distancia_rota_um_ponto():
    matriz = Matriz(0, 0)
    matriz.carregar_de_arquivo('input/matriz_entrada.txt')

    rota = ['A']
    distancia = calcular_distancia_rota(matriz, rota)

    origem = matriz.obter_origem()
    ponto_a = matriz.obter_ponto_entrega('A')
    distancia_esperada = calcular_distancia_manhattan(origem, ponto_a) * 2

    assert distancia == distancia_esperada, f'Distância esperada: {distancia_esperada}, distancia obtida: {distancia}'
    print(f'test_distancia_rota_um_ponto está tudo certo')

if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("EXECUTANDO TESTES DE DISTÂNCIA")
    print("=" * 50 + "\n")

    try:
        test_distancia_simples() 
        test_distancia_mesmo_ponto()
        test_distancia_horizontal()
        test_distancia_vertical()
        test_distancia_rota_simples()
        test_distancia_rota_um_ponto()

        print("\n" + "=" * 50)
        print("✓ TODOS OS TESTES PASSARAM!")
        print("=" * 50)

    except AssertionError as e:
        print(f"\n TESTE FALHOU: {e}")

    except Exception as e:
        print(f"\n ERRO: {e}")
        import traceback
        traceback.print_exc()