# Exportas notas de uma lista

disciplinas = ("matemática", "português", "filosofia", "história", "física", "geografia", "química", "biologia")
notas = [7.8, 8.2, 9.5, 5.7, 9.8, 10, 6.4, 7.0]

conteudos = []
for i in range(len(notas)):
    conteudo = f"A nota da {disciplinas[i]} foi {notas[i]}\n"
    conteudos.append(conteudo)

caminho = 'C:/Users/Usuario/Documents/MeusProjetos/pjc2/nivel1/boletim.txt'
with open(caminho, "a") as arq:
    arq.writelines(conteudos)
# --------------------------- [Exercício] Aula 9