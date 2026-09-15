def calcular_distancia_manhattan(ponto1, ponto2):
    linha1, coluna1 = ponto1
    linha2, coluna2 = ponto2
    
    distancia = abs(linha1 - linha2) + abs(coluna1 - coluna2)
    return distancia

def calcular_distancia_rota(matriz, sequencia_pontos):
    origem = matriz.obter_origem()
    coordenada_atual = origem
    distancia_total = 0
    
    for letra_ponto in sequencia_pontos:
        proxima_coordenada = matriz.obter_ponto_entrega(letra_ponto)
        
        if proxima_coordenada is None:
            raise ValueError(f"Ponto {letra_ponto} não encontrado na matriz")
        
        distancia = calcular_distancia_manhattan(coordenada_atual, proxima_coordenada)
        distancia_total += distancia

        coordenada_atual = proxima_coordenada

    distancia_retorno = calcular_distancia_manhattan(coordenada_atual, origem)
    distancia_total += distancia_retorno
    
    return distancia_total

def formatar_rota(sequencia_pontos):
    return ' '.join(sequencia_pontos)