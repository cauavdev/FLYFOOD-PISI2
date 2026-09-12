class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.dados = []
        self.pontos_entrega = {}
        self.origem = None

    def carregar_de_arquivo(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                primeira_linha = arquivo.readline().strip().split()
                linhas = int(primeira_linha[0])
                colunas = int(primeira_linha[1])

                self.linhas = linhas
                self.colunas = colunas

                self.dados = []
                self.pontos_entrega = {}
                self.origem = None

                for i, linha in enumerate(arquivo):
                    elementos = linha.strip().split()
                    self.dados.append(elementos)

                    for j, elemento in enumerate(elementos):
                        if elemento == 'R':  
                            self.origem = (i, j)
                        elif elemento != '0': 
                            self.pontos_entrega[elemento] = (i, j)

                return True

        except FileNotFoundError:
            print(f"erro: arquivo '{caminho_arquivo}' não encontrado!")
            return False
        except Exception as e:
            print(f"erro ao carregar arquivo: {e}")
            return False

    def exibir(self):
        print(f"matriz {self.linhas}x{self.colunas}:")
        for linha in self.dados:
            print(' '.join(linha))
        print(f"\norigem (R): {self.origem}")
        print(f"pontos de entrega: {self.pontos_entrega}")
        
    def obter_ponto_entrega(self, letra):
        return self.pontos_entrega.get(letra, None)

    def obter_origem(self):
        return self.origem
    
    def obter_pontos_entrega(self):
        return self.pontos_entrega.copy()
    