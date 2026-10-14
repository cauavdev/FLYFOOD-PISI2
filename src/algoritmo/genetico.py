import random

from utils.custo import calcular_custo_ciclo, calcular_aptidao_populacao


def inicializar_populacao(instancia, tamanho, rng):
    cidades = instancia.obter_cidades()
    populacao = []
    for _ in range(tamanho):
        individuo = cidades[:]
        rng.shuffle(individuo)
        populacao.append(individuo)
    return populacao


def selecao_torneio(populacao, aptidoes, k, rng):
    candidatos = rng.sample(range(len(populacao)), k)
    melhor = min(candidatos, key=lambda i: aptidoes[i])
    return populacao[melhor]


def cruzamento_ox(pai1, pai2, rng):
    n = len(pai1)
    a, b = sorted(rng.sample(range(n), 2))
    filho = [None] * n
    filho[a:b + 1] = pai1[a:b + 1]
    usados = set(filho[a:b + 1])
    restantes = [cidade for cidade in pai2 if cidade not in usados]
    posicoes = [i for i in range(n) if filho[i] is None]
    for posicao, cidade in zip(posicoes, restantes):
        filho[posicao] = cidade
    return filho


def mutacao_troca(individuo, rng):
    i, j = rng.sample(range(len(individuo)), 2)
    individuo[i], individuo[j] = individuo[j], individuo[i]


def mutacao_inversao(individuo, rng):
    i, j = sorted(rng.sample(range(len(individuo)), 2))
    individuo[i:j + 1] = reversed(individuo[i:j + 1])


def executar_ag(instancia, tam_pop=150, geracoes=1000, p_cruzamento=0.9,
                p_mutacao=0.2, k_torneio=3, n_elite=2, seed=None):
    rng = random.Random(seed)

    populacao = inicializar_populacao(instancia, tam_pop, rng)
    aptidoes = calcular_aptidao_populacao(instancia, populacao)
    historico = []

    for _ in range(geracoes):
        ordem = sorted(range(tam_pop), key=lambda i: aptidoes[i])
        nova_populacao = [populacao[i][:] for i in ordem[:n_elite]]  # elitismo

        while len(nova_populacao) < tam_pop:
            pai1 = selecao_torneio(populacao, aptidoes, k_torneio, rng)
            pai2 = selecao_torneio(populacao, aptidoes, k_torneio, rng)

            if rng.random() < p_cruzamento:
                filho = cruzamento_ox(pai1, pai2, rng)
            else:
                filho = pai1[:]

            if rng.random() < p_mutacao:
                if rng.random() < 0.5:
                    mutacao_inversao(filho, rng)
                else:
                    mutacao_troca(filho, rng)

            nova_populacao.append(filho)

        populacao = nova_populacao
        aptidoes = calcular_aptidao_populacao(instancia, populacao)
        historico.append(min(aptidoes))

    i_melhor = min(range(tam_pop), key=lambda i: aptidoes[i])
    melhor_rota = populacao[i_melhor]
    return melhor_rota, calcular_custo_ciclo(instancia, melhor_rota), historico
