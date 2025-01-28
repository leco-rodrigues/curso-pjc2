# "ola.py"
# print("Olá Mundo")
# ------------------ Aula 0


# "aprovado.py"
# nota = 7
# media = 5
#
# if nota >= media:
#    print("aprovado")
# else:
#    print("reprovado")
# --------------------- Aula 1


# "Valores, Memória, Tipos de Dados e Variáveis"
# print(7)
# print(7.8)
# print("texto")
# print('palavra')
# print(True)
# print(False)
# print(type(7))
# print(type(7.8))
# print(type("bola"))
# print(type(True))
# print(7 + 5)
# print(type(7 + 5))
# print(type(7 + 5.7654))
# print(type(9.0))
# print(type(9.0 + 1))
# print(8 + "bola")
# print("bisc" + "8")
# print("bisc" + "8" + "s")
# print(7 > 5)
# print(7 < 4)
# print(7 / 2)
# print(7 // 2)
# print(7 % 2)
# print(7 % 4)
# print(7 // 4)
# print(7 * 2)
# print(7 ** 2)
# print("3" * 3)
# palavra1 = "bola"
# palavra2 = "mouse"
# print(palavra1)
# print(palavra2)
# a = 7
# b = 5
# print(a + b)
# resultado = a + b
# print(resultado)
# print(resultado * 2)
# print(a ** 5)
# print(a / b)
# ------------ Aula 2


# "condicoes.py"
# numero = 10
# if numero > 15 or numero < 30:
#     print("Olá Mundo")
#     print("também estou no if")
# else:
#     print("Xau Mundo")
#     print("Mais uma pra você entender")
#
# print("Continuação...")
#
#
# "colegionaval.py"
# nota = 6.0
# media_alta = 7
# media_baixa = 5
#
# if nota >= media_alta:
#     print("Aprovado direto!😎")
# elif nota >= media_baixa:
#     print("Fazer prova final!")
#     nota_pf = 4.0
#     if nota_pf >= media_baixa:
#         print("Aprovado na Prova Final")
#     else:
#         print("Precisa fazer a recuperação final")
#         nota_rf = 5.0
#     if nota_rf >= media_baixa:
#         print("Aprovado na recuperação")
#     else:
#         print("REPROVADO!")
# else:
#     print("Fazer recuperação final 😱")
#     nota_rf = 5.0
#     if nota_rf >= media_baixa:
#         print("Aprovado na recuperação")
#     else:
#         print("REPROVADO!")
# --------------------------- Aula 3


# "io.py"
# palavra = input("Digite uma palvra: ")
# print(palavra)
#
# nota = input("Digite uma nota: ")
# nota = float(nota)
# media = float(input("Digite a média: "))
#
# if nota >= media:
#    print("Aprovado com nota", nota, "(média é", media, ")")
# else:
#    print(f'Reprovado com a nota {nota} (média é {media})')
# ---------------------------------------------------------- Aula 4


# "agregados.py"
# nota_matematica = 7.8
# nota_portugues = 8.2
# nota_filosofia = 9.5
#
# nomes = ("Maria", "João", "Paula")
# print(nomes[0], nomes[-1])
# nomes[1] = "Marcelo"
#
# notas = [7.8, 8.2, 9.5]
# disciplinas = ["matemática", "português", "filosofia"]
# disciplinas.append("história")
# notas[0] = notas[0] + 1
# notas.append(9)
# print(notas, type(notas), type(notas[0]))
# print(f"A nota de {disciplinas[0]} foi {notas[0]})
# print(f"A nota de {disciplinas[-2]} foi {notas[-2]})
# print(disciplinas[3])
# print(notas[3])
# --------------- Aula 5


# "repeticoes.py"
# alunos = ("Hallison", "Maria", "José", "Ana")
# for nome in alunos:
#     print(nome)
#     print("----------")
# print("Acabaram as repetições")
#
# for numero in range(3, 10, 2)
#     print(numero)
#
# for idx in range(len(alunos)):
#     print(alunos[idx])
#
#
# "disciplinas.py"
# disciplinas = ("matemática", "português", "filosofia", "história", "física", "geografia", "química", "biologia")
# notas = [7.8, 8.2, 9.5, 5.7, 9.8, 10, 6.4, 7.0]
#
# for i in (len(notas)):
#     print(f"A nota da {disciplinas[i]} foi {notas[i]}")
# ------------------------------------------------------- Aula 6


# "enquanto.py"
# nota = float(input("Digite um valor de nota: "))
# if nota >= 0 and nota <= 10:
#     print(nota)
# else:
#     print("nota inválida")
# while nota < 0 or nota > 10:
#     nota = float(input("Digite um valor VÁLIDO de nota: "))
#     print("vou repetir")
# print(nota)
#
#
# "exenquanto.py"
# n = 10
# while n >= 0:
#     if n % 2 == 1:
#         n = n - 1
#         continue
#     print(n)
#     n = n - 1
# 
# n = 10
# while n >= 0:
#     print(n)
#     n = n - 1
#     if n == 5:
#         break
# ------------- Aula 7