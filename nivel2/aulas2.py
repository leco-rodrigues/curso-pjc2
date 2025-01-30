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