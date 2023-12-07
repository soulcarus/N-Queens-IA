# TRABALHO EXTRA I.A - JOAO ÍCARO MOREIRA | 537176
# HILL CLIMBING ESTOCÁSTICO
# PROBLEMA DAS N RAINHAS

# Busca local ou de melhor iterativa opera em um único estado e move-se para a vizinhança deste estado.
# A ideia é começar com o melhor estado inicial (ou aleatório) e melhorá-lo iterativamente.

# Em relação ao estado corrente com nossa função heurística (F'(n)):
# - Planícies
# - Máximo Global
# - Máximo Local (objetivo)
# - Máximo Local (plano)

# Tentei abordar com temperatura simulada, mas não consegui criar uma função objetivo que piora e depois melhora o estado.
# Talvez seja mais eficaz permitir apenas pioras e simplificar o processo.

# IMPLEMENTAÇÃO DO HILL CLIMBING ESTOCÁTICO:
# - Colisões em linha e diagonal são usadas como heurísticas para avaliar a qualidade de um estado.
# - A função hill_climbing é responsável por encontrar o máximo local, onde avalia os vizinhos gerados por movimentos
#   aleatórios e escolhe o que melhora a avaliação.
# - O processo é repetido até que um máximo local seja atingido.

# Função Heurística (F'(n)): respectivamente colisao_dig(estado) e colisao_dig(estado)
# Função de Avaliação (eval) (H'(n)): colisao_dig(estado) + colisao_linha(estado)

import random

def colisoes_linha(tabuleiro):
    colisoes = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if j != i:
                if tabuleiro[i] == tabuleiro[j]:
                    colisoes += 1
    return colisoes

def colisoes_diagonal(tabuleiro):
    colisoes = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if i != j:
                diferenca = abs(i - j)
                if tabuleiro[i] == tabuleiro[j] + diferenca or tabuleiro[i] == tabuleiro[j] - diferenca:
                    colisoes += 1
    return colisoes / 2

def gerar_candidatos(atual):
    candidatos = [atual[:i] + [random.randint(1, len(atual))] + atual[i + 1:] for _ in range(1, len(atual) + 1) for i in range (len(atual))]
    # não gosto do formato de retornar uma list comp. diretamente
    return candidatos

def gerar_estado(n):
    estado = [random.randint(1, n) for _ in range(n)]
    return estado

def hill_climbing(inicial):
    melhor, atual = inicial, inicial
    atual_eval = colisoes_diagonal(inicial) + colisoes_linha(inicial)

    while True:
        atual = melhor if atual != inicial else atual
        candidatos = gerar_candidatos(atual)
        for candidato in candidatos:
            candidato_eval = colisoes_diagonal(candidato) + colisoes_linha(candidato)
            if candidato_eval < atual_eval:
                atual = candidato
                atual_eval = candidato_eval

        if melhor == atual:
            return melhor

        melhor = atual

def nqueens(estado):
    contagem = 1
    estado = hill_climbing(estado)

    while colisoes_diagonal(estado) + colisoes_linha(estado):
        # print("ESTADO ATUAL: ", estado)
        estado = gerar_estado(len(estado))
        contagem += 1
        estado = hill_climbing(estado)
        # print("ESTADO ATUAL: ", estado)

    return contagem, estado

n = 32
estado_inicial = gerar_estado(n)
reinicializacoes, resultado = nqueens(estado_inicial)

print("\n")
print(f"Número de reinicializações: {reinicializacoes}")
print(f"Solução encontrada: {resultado}\n")

tabuleiro = []
for i in range(n):
    tabuleiro.append([0] * n)

for i in range(len(resultado)):
    tabuleiro[i][resultado[i] - 1] = 1

    print(f"linha: {i + 1} | conteudo: {tabuleiro[i]} | posicao: {resultado[i]}")

print("\nRESULTADO: \n")
for i in tabuleiro:
    print(i)

# CRIAÇÃO DE ARQUIVO PARA VALIDAR SOLUÇÃO

with open("entrada.txt", "w") as arquivo:
    arquivo.writelines(f"{n}\n")
    for row in tabuleiro:
        for elem in row:
            arquivo.write(f"{elem} ")
        arquivo.write("\n")