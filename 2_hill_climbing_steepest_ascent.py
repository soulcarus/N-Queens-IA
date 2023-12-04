import random
import math

# JOÃO ÍCARO MOREIRA | 537176
# links de estudo: 
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjMv8nKsPWCAxUPCbkGHd9BDhIQFnoECBAQAw&url=https%3A%2F%2Fijistech.org%2Fijistech%2Findex.php%2Fijistech%2Farticle%2Fdownload%2F153%2F153&usg=AOvVaw3cKHEOHydMq2ULqerHKZSc&opi=89978449

# CRITÉRIOS DE POLÍTICAS DE VIZINHANÇA:
# 1 - MOVIMENTO EM LINHA NA FUNÇÃO gerar_candidatos(atual) -> ALTERAMOS A LINHA MOVENDO A RAINHA PARA UMA POS ALEAT.
# 2 - MOVIMENTAÇÃO ALEATÓRIA GERAL NA FUNÇÃO gerar_estado(n) -> CRIAMOS UM ESTADO DE MANEIRA ALEATÓRIA

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
    return 1.0 if delta_avaliacao < 0 else math.exp(-delta_avaliacao / temperatura) 

def steepest_ascent_hill_climbing(inicial):
    melhor, atual = inicial, inicial
    melhor_eval = colisoes_diagonal(inicial) + colisoes_linha(inicial)

    while True:
        atual = melhor if atual != inicial else atual
        candidatos = gerar_candidatos(atual)

        melhor_candidato = min(candidatos, key=lambda x: colisoes_diagonal(x) + colisoes_linha(x))
        melhor_candidato_eval = colisoes_diagonal(melhor_candidato) + colisoes_linha(melhor_candidato)

        if melhor_candidato_eval >= melhor_eval:
            return melhor

        melhor = melhor_candidato
        melhor_eval = melhor_candidato_eval

def nqueens(estado):
    estado = steepest_ascent_hill_climbing(estado)

    while colisoes_diagonal(estado) + colisoes_linha(estado):
        # print("ESTADO ATUAL: ", estado)
        estado = gerar_estado(len(estado))
        estado = steepest_ascent_hill_climbing(estado)
        # print("ESTADO ATUAL: ", estado)

    return estado

n = 8
estado_inicial = gerar_estado(n)
resultado = nqueens(estado_inicial)

print("\n")
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