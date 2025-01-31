"""!!!CONTEÚDO COPIADO DIRETAMENTE DOS VÍDEOS DO CURSO Python do Jeito Certo 2.0,
 DO CANAL Programação Dinâmica!!!"""


# "funcoes.py"
# num = int(input("Digite um número: "))
# num = num + 3
# print(num)
#
# def multiplicar_por_7(n):
#     res = 7 * n
#     return res
#
# def media_simples(a, b):
#     return (a + b) / 2
#
# r = multiplicar_por_7(10)
# print("Resultado é", r)
# print(media_simples(10, 8))
# res = multiplicar_por_7(6)
# print(res)
# a = 8
# b = 32
# print(media_simples(b, a))
#
# def pedir_inscricao():
#     print("Inscreva-se no canal Programação Dinâmica")
#
# pedir_inscricao()
# ----------------- Aula 10


# "lados.txt"
# 3 4 5
# 10 4 5
# 1 8 7
# 6 8 7
#
#
# "escrevertriangulo.py"
# def triangulo_verdadeiro(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return False
#     if a > (b + c):
#         return False
#     if b > (a + c):
#         return False
#     if c > (a + b):
#         return False
#     return True
#
# with open("data/lados.txt", "r") as arq:
#     linhas = arq.readlines()
# respostas = []
# for linha in linhas:
#     partes = linha.strip().split()
#     # convertendo cada parte para float
#     for i in range(len(partes)):
#         partes[i] = float(partes[i])
#     resposta = triangulo_valido(partes[0], partes[1], partes[2])
#     if resposta:
#         respostas.append("SIM")
#     else:
#         respostas.append("NÃO")
#
# with open("resposta-triangulos.txt", "w") as arq:
#     for resp in respostas:
#         arq.write(f"{resp}\n")
# ------------------------------ Aula 11


# "triangulos.py"
# def triangulo_verdadeiro(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return False
#     if a > (b + c):
#         return False
#     if b > (a + c):
#         return False
#     if c > (a + b):
#         return False
#     return True
#
#
# "escrevertriangulo.py"
# import triangulos as tri
#
# with open("data/lados.txt", "r") as arq:
#     linhas = arq.readlines()
# respostas = []
# for linha in linhas:
#     partes = linha.strip().split()
#     # convertendo cada parte para float
#     for i in range(len(partes)):
#         partes[i] = float(partes[i])
#     resposta = triangulos.triangulo_valido(partes[0], partes[1], partes[2])
#     if resposta:
#         respostas.append("SIM")
#     else:
#         respostas.append("NÃO")
#
# with open("resposta-triangulos.txt", "w") as arq:
#     for resp in respostas:
#         arq.write(f"{resp}\n")
#
#
# "respondetriangulo.py"
# from triangulos import triangulo_valido
#
# a = float(input("Digite um valor de um lado: "))
# b = float(input("Digite um valor de um lado: "))
# c = float(input("Digite um valor de um lado: "))
#
# if triangulo_valido(a, b, c):
#     print(f"{a}, {b} e {c} formam um triângulo VÁLIDO!")
# else:
#     print(f"{a}, {b} e {c} NÃO formam um triângulo VÁLIDO!")
# ------------------------------------------------------------ Aula 12


# "caminhos.py"
# import os
# absoluto = "/Users/Usuario/Documents/MeusProjetos/pjc2/nivel2/aulas2.py"
# relativo = "nivel2/aulas2.py"
#
# DATA_DIR = "data"
# print(os.path.abspath(DATA_DIR))
#
# caminho = os.path.join(os.path.abspath(DATA_DIR)), "lados.txt")
# print(caminho)
#
# print(os.listdir("nivel2"))
#
# modulos_python = []
# for nome in os.listdir("nivel2"):
#     if nome.endwith(".py")
#         modulos_python.append(nome)
# print(modulos_python)
#
# print(os.path.join(os.path.abspath('.'), 'data', 'lados.txt))
#
# OUTPUT_DIR = "saidas"
# nomearquivos "mensagem.txt"
#
# if not os.path.exists(OUTPUT_DIR):
#     os.makedirs(OUTPUT_DIR)
#
# with open(os.path.join(OUTPUT_DIR, nomearquivo), 'w') as arq:
#     arq.write("Inscreva-se no canal Programação Dinâmica")
# ---------------------------------------------------------- Aula 13