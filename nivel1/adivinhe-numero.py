# Jogo de adivinhar o número
from random import randint


    # Mensagem de erro
def error_message(msg = 'Entrada inválida!'):
    print(msg)

# Passo 1: Gerar um número aleatório
    # Gera um número inteiro aleatório entre 1 e 100
n = randint(1, 100)

# Passo 2: Criar um loop que indica se o número escolhido é maior ou menor, até que o número certo seja escolhido
while True:
    try:
        numero = int(input('Qual foi o número sorteado entre 1 e 100? ').strip())
        if numero == n:
            break
        elif 100 > numero > n:
            print('O número correto é menor.')
        elif 0 < numero < n:
            print('O número correto é maior.')
        else:
            error_message()
    except ValueError:
        error_message()

# Passo 3: Exibir o resultado
print('Parabéns! Você acertou!')
# ------------------------------ [Exercício] Aula 7