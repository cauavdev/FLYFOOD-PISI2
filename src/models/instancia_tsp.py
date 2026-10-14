class InstanciaTSP:
    def __init__(self, nome, qtde_cidades):
        self.nome = nome
        self.qtde_cidades = qtde_cidades
        self.distancias = {}

    def carregar_de_arquivo(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                pesos = [int(valor) for valor in arquivo.read().split()]
        except FileNotFoundError:
            print(f"erro: arquivo '{caminho_arquivo}' não encontrado!")
            return False
        except ValueError as e:
            print(f"erro ao ler pesos do arquivo: {e}")
            return False

        n = self.qtde_cidades
        esperado = n * (n - 1) // 2
        if len(pesos) != esperado:
            print(f"erro: esperado {esperado} pesos, encontrados {len(pesos)}")
            return False

        self.distancias = {}
        posicao = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                peso = pesos[posicao]
                posicao += 1
                self.distancias[(i, j)] = peso
                self.distancias[(j, i)] = peso
        return True

    def obter_distancia(self, a, b):
        return self.distancias[(a, b)]

    def obter_cidades(self):
        return list(range(1, self.qtde_cidades + 1))
