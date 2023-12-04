import random
import math

# JOÃO ÍCARO MOREIRA | 537176
# VERSÃO FUNCIONANDO 100%
# TODAS AS VERSÕES SÃO BASICAMENTE IGUAIS, ACHEI BEM DIVERTIDO

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

def temperatura_atual(iteracao, max_iteracoes, temp_inicial):
    return temp_inicial * (1 - iteracao / max_iteracoes)

def probabilidade_aceitar(delta_avaliacao, temperatura):
    if delta_avaliacao < 0:
        return 1.0
    return math.exp(-delta_avaliacao / temperatura)

def tempera_simulada(inicial, max_iteracoes=1000, temp_inicial=1.0):
    melhor, atual = inicial, inicial
    atual_eval = colisoes_diagonal(inicial) + colisoes_linha(inicial)

    for iteracao in range(max_iteracoes):
        temperatura = temperatura_atual(iteracao, max_iteracoes, temp_inicial)
        atual = melhor if atual != inicial else atual
        candidatos = gerar_candidatos(atual)

        candidato = random.choice(candidatos)
        candidato_eval = colisoes_diagonal(candidato) + colisoes_linha(candidato)

        delta_avaliacao = candidato_eval - atual_eval
        if delta_avaliacao < 0 or random.uniform(0, 1) < probabilidade_aceitar(delta_avaliacao, temperatura):
            atual = candidato
            atual_eval = candidato_eval

        if melhor == atual:
            return melhor

        melhor = atual

    return melhor

def nqueens_tempera_simulada(estado):
    contagem = 1
    estado = tempera_simulada(estado)

    while colisoes_diagonal(estado) + colisoes_linha(estado):
        estado = gerar_estado(len(estado))
        contagem += 1
        estado = tempera_simulada(estado)

    return contagem, estado

n = 8
estado_inicial = gerar_estado(n)
reinicializacoes, resultado = nqueens_tempera_simulada(estado_inicial)

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