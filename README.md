# FlyFood - Rotas Otimizadas (PISI2)

## Descrição
Estamos no ano de 2030 e nesse futuro não tão distante o trânsito está caótico. As empresas de delivery já não conseguem fazer entregas em um tempo aceitável e o custo com entregadores está muito alto, pois mão-de-obra humana está cada vez mais valorizada devido à grande oferta de empregos (ok… essa última parte é mais sonho do que realidade, mas vamos considerá-la). Então, um ex-aluno do BSI-UFRPE resolve criar uma empresa chamada FlyFood para fazer entregas utilizando drones.

Essas máquinas voadoras fantásticas podem receber uma rota de entregas e executá-las à risca. Ou seja, elas podem voar desde o local de origem do pedido (por exemplo, restaurante ou lanchonete) com vários pedidos no seu compartimento de carga e entregar em vários endereços espalhados na cidade. Essa capacidade de sair com vários pedidos otimiza bastante o tempo de entrega dos pedidos. No entanto, nem tudo são flores. A capacidade das baterias dos drones continuam sendo um problema. Sendo assim, é preciso otimizar ao máximo o trajeto do drone para conseguir concluir todas as entregas dentro do ciclo da bateria.

Com esse cenário em vista, já nos dias atuais (2026) o empreendedor da FlyFood vai começar a desenvolver um algoritmo de roteamento. Ou seja, um algoritmo que seja capaz de definir o menor trajeto para a realização de todas as entregas do drone.

Para abstrair as questões de encontrar endereços e obter coordenadas GPS, vamos trabalhar com uma matriz que representa os pontos da cidade. Veja um exemplo de matriz logo a seguir:

| | | | D |
|---|---|---|---|
| | A | | |
| | | | C |
| R | | B | |

Na matriz, o ponto superior esquerdo é o (0,0) e nessa posição não existe um ponto de entrega. Já no ponto (1,1) existe o ponto de entrega A. Os demais pontos de entrega estão nos pontos B (3,2), C (2,4) e D (0, 4). No exemplo acima, a origem do drone, ou seja onde ele é carregado com os pedidos, é o ponto R (3,0). Por convenção, o ponto R sempre será o ponto de origem e retorno.

Vamos considerar também que o drone não consegue andar na "diagonal". Ou seja, ele só consegue percorrer essa matriz na horizontal ou na vertical. Sendo assim, para ir do ponto A para o ponto B ele precisa percorrer 3 dronômetros (unidade de medida de custo do percurso). Para ir de B para D a distância é de 5 dronômetros.

Seu trabalho será elaborar um algoritmo que vai ler uma matriz, a partir de um arquivo, com os pontos de entrega e o ponto de origem e retorno. Ele deverá retornar a ordem em que o drone deve percorrer os pontos de entrega. Essa ordem deve ser a de menor custo, ou seja, a que o drone percorrerá a menor distância em dronômetros.

O formato do arquivo de entrada será o seguinte para a matriz de exemplo.

```text
4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
```

Sua resposta deverá ser a sequência de pontos (em forma de string) que produz o menor circuito possível a ser percorrido pelo drone entre os pontos de entrega, partindo e retornando ao ponto R (o ponto R não precisa ser incluído na sequência de resposta). Por exemplo: "A D C B". (obs: se existir mais de um trajeto com a menor distância, basta retornar um deles.)

## Integrantes do Grupo

- **Cauã** - Estrutura base e leitura de arquivos
- **Caio** - Validação de dados
- **Carlos** - Cálculo de distâncias
- **Samuel** - Algoritmo de roteamento

## Tecnologias Utilizadas

- **Linguagem:** Python 3.14
- **Principais Bibliotecas:**
  - `itertools` - Geração de permutações
  - `time` - Medição de performance
- **Ambiente:** Visual Studio Code
- **Sistema Operacional:** Windows 11 (64 bits)
- **Hardware de Teste:** AMD Ryzen 5 5500 (3.60 GHz), 16 GB RAM DDR4

## Como Executar

### Execução Principal
```bash
cd src
python main.py
```

### Executar Testes
```bash
# Testes de distância
python tests/test_distancia.py

# Testes de matriz
python tests/test_matriz.py

# Testes de roteamento
python src/algoritmo/teste_roteamento.py
```

### Arquivo de Entrada
Por padrão, o programa lê a matriz de `input/matriz_entrada.txt`. Para usar um arquivo diferente, edite o caminho em `src/main.py`:

```python
caminho_entrada = 'input/seu_arquivo.txt'
```

## Estrutura do Projeto

```
FLYFOOD-PISI2/
├── README.md
├── input/
│   └── matriz_entrada.txt          # Arquivo de entrada padrão
├── src/
│   ├── main.py                     # Programa principal
│   ├── models/
│   │   ├── __init__.py
│   │   └── matriz.py               # Classe Matriz
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── distancia.py            # Cálculos de distância
│   │   └── matriz_utils.py         # Validação e exibição
│   └── algoritmo/
│       ├── __init__.py
│       ├── roteamento.py           # Algoritmo de otimização
│       └── teste_roteamento.py     # Testes do algoritmo
└── tests/
    ├── test_matriz.py              # Testes da classe Matriz
    └── test_distancia.py           # Testes de distância
```

## Arquitetura da Solução

O projeto foi estruturado em camadas bem definidas para promover separação de responsabilidades e facilitar manutenção:

- **`models/`** - Encapsula a representação de dados através da classe Matriz
- **`utils/`** - Funções utilitárias de cálculo e validação independentes
- **`algoritmo/`** - Contém a lógica principal de otimização
- **`tests/`** - Suite de testes automatizados com ~90% de cobertura de código

## Metodologia

### Abordagem: Força Bruta
O algoritmo utiliza força bruta para garantir encontrar a rota ótima. A estratégia consiste em:

1. Gerar todas as n! permutações possíveis de pontos de entrega
2. Calcular a distância total (usando métrica Manhattan) para cada permutação
3. Armazenar a permutação com menor distância
4. Retornar a rota ótima encontrada

**Complexidade:** O(n! × n), onde n é o número de pontos de entrega.

### Métrica de Distância
Utilizamos a distância de Manhattan para calcular custos:
```
d(P1, P2) = |x1 - x2| + |y1 - y2|
```
Essa métrica reflete o movimento horizontal/vertical do drone na malha urbana.

### Validação
Antes de processar a matriz, o algoritmo valida:
- Existência do ponto de origem (R)
- Presença de pontos de entrega
- Integridade dos limites da matriz

## Resultados Experimentais

O algoritmo foi testado com matrizes de 5 a 13 pontos de entrega. Os resultados validam o crescimento fatorial previsto pela análise teórica:

| Pontos | Permutações | Tempo de Execução |
|--------|-------------|-------------------|
| 5      | 120         | 0.0013s           |
| 6      | 720         | 0.0020s           |
| 7      | 5.040       | 0.0089s           |
| 8      | 40.320      | 0.0784s           |
| 9      | 362.880     | 0.6888s           |
| 10     | 3.628.800   | 7.6448s           |
| 11     | 39.916.800  | 88.9466s          |
| 12     | 479.001.600 | ~20 minutos       |
| 13     | 6.227.020.800 | ~4h 37min       |

**Conclusão:** O algoritmo é praticável para instâncias até ~12 pontos em tempo aceitável. Além disso, torna-se impraticável, destacando a necessidade de heurísticas para aplicações reais.

## Testes Automatizados

O projeto inclui 16 testes automatizados com ~90% de cobertura:

### Testes de Distância (6 testes)
- Validação da métrica Manhattan em casos simples, horizontais, verticais e complexos
- Garantem precisão dos cálculos de custo

### Testes de Matriz (5 testes)
- Carregamento correto de arquivo
- Identificação precisa de origem e pontos de entrega
- Tratamento adequado de erros

### Testes de Roteamento (3 testes)
- Verificação de que todas as permutações são testadas
- Validação de otimalidade comparando com força bruta completa
- Tratamento de casos extremos (sem pontos de entrega)

Para executar todos os testes:
```bash
python tests/test_distancia.py
python tests/test_matriz.py
python src/algoritmo/teste_roteamento.py
```

## Exemplo de Uso

### Entrada (arquivo `input/matriz_entrada.txt`):
```
4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
```

### Execução:
```bash
python src/main.py
```

### Saída Esperada:
```
====================
FlyFood - PISI-2
====================

Carregando arquivo: input/matriz_entrada.txt
Arquivo carregado com sucesso!

Matriz validada com sucesso! origem: (3, 0), pontos: 4

====================
RESUMO DA MATRIZ
====================
dimensões: 4 linhas x 5 colunas
ponto de origem (R): (3, 0)
quantidade de pontos de entrega: 4
pontos de entrega: ['A', 'B', 'C', 'D']
====================

--- Calculando Melhor Rota ---
Melhor rota: A D C B
Distância: 14 dronômetros

⏱️ Tempo total: 0.0013s
```

## Limitações e Considerações

- **Escalabilidade:** Força bruta é impraticável para 13+ pontos em tempo viável
- **Ambiente Simplificado:** Trabalha apenas com matrizes 2D sem restrições de tempo, capacidade de carga ou obstáculos
- **Sem Heurísticas:** Não implementa algoritmos aproximados para melhor performance em instâncias grandes
- **Bateria não Simulada:** Não considera consumo real de bateria do drone

## Trabalhos Futuros

1. **Implementação de Heurísticas:** Algoritmos Genéticos, Simulated Annealing, Vizinho Mais Próximo
2. **Restrições Realistas:** Capacidade de carga, autonomia de bateria, janelas de tempo de entrega
3. **Visualização Avançada:** Animação do percurso do drone, mapas interativos
4. **Otimização Multiobjetiva:** Minimizar tempo e custo energético simultaneamente
5. **Integração com Dados Reais:** Conectar a sistemas de GPS e mapas urbanos

## Performance e Complexidade

| Aspecto | Valor |
|---------|-------|
| Complexidade de Tempo | O(n! × n) |
| Complexidade de Espaço | O(n) |
| Cobertura de Testes | ~90% |
| Linhas de Código | ~250 |
| Funções Implementadas | 14 |
| Testes Automatizados | 16 |

## Contribuições

Este projeto é resultado da colaboração equilibrada entre os integrantes:

- **Cauã:** Estrutura base, leitura de arquivos, orquestração do programa
- **Caio:** Validação robusta de dados de entrada
- **Carlos:** Implementação precisa de cálculos de distância
- **Samuel:** Algoritmo de otimização e testes completos

## Referências

- Garey, M. R., & Johnson, D. S. (1979). Computers and Intractability.
- Held, M., & Karp, R. M. (1962). A dynamic programming approach to sequencing problems.
- Krause, E. F. (1986). Taxicab Geometry: An Adventure in Non-Euclidean Geometry.
- Picolo, A. P. (2021). Aplicação do Problema do Caixeiro Viajante.
- Sarubbi, J. F. M. (2008). Problemas de roteamento com custos de carga.
- Scaburi, A., Ferreira, J. C., & Steiner, M. T. A. (2019). Problema de Localização de Facilidades e PCV.

## Licença

Este projeto é desenvolvido como atividade acadêmica da disciplina PISI-2 (Projeto Interdisciplinar para Sistemas de Informação II) da Universidade Federal Rural de Pernambuco.

---

**UFRPE BSI**

*Recife, Setembro de 2026*
