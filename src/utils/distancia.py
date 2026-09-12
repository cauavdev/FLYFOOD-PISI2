_cache_distancias = {}


def calcular_distancia_manhattan(ponto1, ponto2):
    linha1, coluna1 = ponto1
    linha2, coluna2 = ponto2

    distancia = abs(linha1 - linha2) + abs(coluna1 - coluna2)

    return distancia

def _chave_distancia(ponto1, ponto2):
    if ponto1 <= ponto2:
        return ponto1, ponto2
    return ponto2, ponto1

def _obter_distancia(matriz, ponto1, ponto2):
    chave = _chave_distancia(ponto1, ponto2)

    if chave not in _cache_distancias:
        coordenada1 = (
            matriz.obter_origem()
            if ponto1 == 'R'
            else matriz.obter_ponto_entrega(ponto1)
        )

        coordenada2 = (
            matriz.obter_origem()
            if ponto2 == 'R'
            else matriz.obter_ponto_entrega(ponto2)
        )

        if coordenada1 is None:
            raise ValueError(f'Ponto {ponto1} não encontrado na matriz')

        if coordenada2 is None:
            raise ValueError(f'Ponto {ponto2} não encontrado na matriz')

        _cache_distancias[chave] = calcular_distancia_manhattan(coordenada1, coordenada2)

    return _cache_distancias[chave]

def calcular_distancia_rota(matriz, sequencia_pontos):
    origem = 'R'
    ponto_atual = origem
    distancia_total = 0

    for proximo_ponto in sequencia_pontos:
        distancia_total += _obter_distancia(matriz, ponto_atual, proximo_ponto)
        ponto_atual = proximo_ponto

    distancia_total += _obter_distancia(matriz, ponto_atual, origem)

    return distancia_total

def formatar_rota(sequencia_pontos):
    return ' '.join(sequencia_pontos)