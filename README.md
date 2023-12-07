# N-Rainhas com Hill Climbing e Simulated Annealing

## Hill Climbing Estocástico

Implementação do algoritmo Hill Climbing Estocástico para resolver o problema das N-Rainhas. 

### Funções Implementadas:

- `colisoes_linha(tabuleiro)`: Calcula o número de colisões em linhas no tabuleiro.
- `colisoes_diagonal(tabuleiro)`: Calcula o número de colisões diagonais no tabuleiro.
- `gerar_candidatos(atual)`: Gera candidatos fazendo alterações em cada linha individualmente.
- `gerar_estado(n)`: Cria um novo estado aleatório.
- `hill_climbing(inicial)`: Implementação do algoritmo Hill Climbing.
- `nqueens(estado)`: Função principal que utiliza o Hill Climbing para resolver o problema das N-Rainhas.

## Hill Climbing Subida Íngrime:

Implementação do algoritmo Hill Climbing com ramificação SUbida Íngrime para resolver o problema das N-Rainhas. 

### Funções Implementadas:

- `colisoes_linha(tabuleiro)`: Calcula o número de colisões em linhas no tabuleiro.
- `colisoes_diagonal(tabuleiro)`: Calcula o número de colisões diagonais no tabuleiro.
- `gerar_candidatos(atual)`: Gera candidatos fazendo alterações em cada linha individualmente.
- `gerar_estado(n)`: Cria um novo estado aleatório.
- `steepest_ascent_hill_climbing(inicial)`: Implementação do algoritmo Hill Climbing Subida mais Íngrime.
- `nqueens(estado)`: Função principal que utiliza o Hill Climbing Estocástico para resolver o problema das N-Rainhas.

## Simulated Annealing

Implementação do algoritmo Simulated Annealing para resolver o problema das N-Rainhas. 

### Funções Implementadas:

- `colisoes_linha(tabuleiro)`: Calcula o número de colisões em linhas no tabuleiro.
- `colisoes_diagonal(tabuleiro)`: Calcula o número de colisões diagonais no tabuleiro.
- `gerar_candidatos(atual)`: Gera candidatos fazendo alterações em cada linha individualmente.
- `gerar_estado(n)`: Cria um novo estado aleatório.
- `temperatura_atual(iteracao, max_iteracoes, temp_inicial)`: Calcula a temperatura atual no algoritmo Simulated Annealing.
- `probabilidade_aceitar(delta_avaliacao, temperatura)`: Calcula a probabilidade de aceitar um movimento no Simulated Annealing.
- `tempera_simulada(inicial, max_iteracoes=1000, temp_inicial=1.0)`: Implementação do algoritmo Simulated Annealing.
- `nqueens_tempera_simulada(estado)`: Função principal que utiliza o Simulated Annealing para resolver o problema das N-Rainhas.

## Como Usar:

- Execute cada código de maneira individual p/ resolver o problema com os algoritmos.
