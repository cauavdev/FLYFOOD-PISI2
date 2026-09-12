def validar_matriz(matriz):
    if matriz.obter_origem() is None:
        return False, 'não há o ponto R na matriz'

    pontos = matriz.obter_pontos_entrega()
    if len(pontos) == 0:
        return False, 'não há pontos de entrega na matriz'

    linha_origem, coluna_origem = matriz.obter_origem()
    if not (0 <= linha_origem < matriz.linhas and 0 <= coluna_origem < matriz.colunas):
        return False

    for ponto, (linha, coluna) in pontos.items():
        if not (0 <= linha < matriz.linhas and 0 <= coluna < matriz.colunas):
            return False, f'o ponto {ponto} está fora dos limites da matriz'

    return True, f'matriz validada com sucesso! origem: {matriz.obter_origem()}, pontos: {len(pontos)}'

def exibir_resumo_matriz(matriz):
    print("\n" + "=" * 20)
    print("RESUMO DA MATRIZ")
    print("=" * 20)
    print(f"dimensões: {matriz.linhas} linhas x {matriz.colunas} colunas")
    print(f"ponto de origem (R): {matriz.obter_origem()}")
    print(f"quantidade de pontos de entrega: {len(matriz.obter_pontos_entrega())}")
    print(f"pontos de entrega: {list(matriz.obter_pontos_entrega().keys())}")
    print("=" * 20)