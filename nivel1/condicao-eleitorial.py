# Definir se o voto de uma pessoa é "obrigatório", "facultativo" ou "proibido" baseado na sua idade
idade = 70

if 71 > idade >= 18:
    print("Voto obrigatório")
elif idade == 16 or idade == 17 or idade > 70:
    print("Voto facultativo")
else:
    print("Voto proibido")
# ------------------------ [Exercício] Aula 1