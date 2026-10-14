def calcular_custo_ciclo(instancia, permutacao):
    """Custo total do ciclo: soma das distancias consecutivas + volta ao primeiro no."""
    soma = 0
    for i in range(len(permutacao) - 1):
        soma += instancia.distancias[(permutacao[i], permutacao[i + 1])]
    soma += instancia.distancias[(permutacao[-1], permutacao[0])]
    return soma


def calcular_aptidao_populacao(instancia, populacao):
    """Lista de custos na mesma ordem da populacao (menor = melhor)."""
    return [calcular_custo_ciclo(instancia, individuo) for individuo in populacao]


def e_permutacao_valida(instancia, individuo):
    return sorted(individuo) == instancia.obter_cidades()
