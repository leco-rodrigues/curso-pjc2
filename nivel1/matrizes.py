# Exibir matrizes com base em dados enviados pelo usuário
from numpy import random


    # Mensagem de erro
def mensagem_erro(msg = 'Entrada inválida'):
    print(msg)

# Passo 1: Receber o número de linhas, colunas e elementos para montar a matriz
    # Dados a serem recebidos do usuário
def matriz_linhas():
    while True:
        try:
            linhas = int(input('Número de linhas: ').strip())
            if linhas > 0:
                return linhas
            mensagem_erro()
        except ValueError:
            mensagem_erro()

def matriz_colunas():
    while True:
        try:
            colunas = int(input('Número de colunas: ').strip())
            if colunas > 0:
                return colunas
            mensagem_erro()
        except ValueError:
            mensagem_erro()

linhas = matriz_linhas()
colunas = matriz_colunas()
elements = linhas * colunas # O número de elementos deve ser proporcional a ordem da matriz (n * m = a)

# Passo 2: Montar a matriz com base nos dados recebidos no "Passo 1"
    # Exibindo resultados
print(f' Matriz A{linhas}x{colunas}:\n')
    # Gera uma matriz A com números (inteiros >= 0) aleatórios de ordem nxm
rgn = random.default_rng()
matrix = rgn.integers(int(elements), size = (int(linhas), int(colunas)))

# Passo 3: Exibir a matriz
print(matrix)
# ----------- [Exercício] Aula 6