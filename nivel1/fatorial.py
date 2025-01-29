# Exibir o fatorial de um número
    # Mensagem de erro
def mensagem_erro(msg = 'Entrada inválida'):
    print(msg)

# Passo 1: Receber um número (inteiro > 1)
while True:
    try:
        number = int(input('Digite um número: '))
        if number > 1:
            break
        mensagem_erro()
    except ValueError:
        mensagem_erro()
   # Váriável cópia para o valor original não ser alterado
number_f = number

# Passo 2: Criar uma variável para efetuar o cálculo (n! = n * (n -1)...* 1)
factorial = number * (number - 1)
print(factorial)

# Passo 3: Criar um loop até que o número seja fatorado
while number_f > 1:
    number_f = number_f - 1
    if number_f > 1:
        factorial = factorial * (number_f - 1)
        print(factorial)
    else:
        break

# Passo 4: Exibir o resultado
print(f'O fatorial de {number}! é igual a {factorial}.')
# ------------------------------------------------------ [Exercício] Aula 7