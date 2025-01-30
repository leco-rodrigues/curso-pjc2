# Criar uma função, com três parâmetros, que diga se é possível formar um triângulo

# Passo 1: Criar a função 
def formar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

# Passo 2: Receber os argumentos
    # Função para otimizar o processo
def lado_triangulo(a = 'Insira um valor para um dos lados do triângulo: '):
    while True:
        try:
            lado = int(input(a).strip())
            if lado > 0:
                return lado
            print('Por favor, insira um valor positivo.')
        except ValueError:
            print('Por favor, insira um número inteiro positivo.')

a = lado_triangulo('Insira um valor para o primeiro lado do triângulo: ')
b = lado_triangulo('Insira um valor para o segundo lado do triângulo: ')
c = lado_triangulo('Insira um valor para o terceiro lado do triângulo: ')

# Passo 3: Chamar a função e exibir o resultado
if formar_triangulo(a, b, c):
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo...')
# ------------------------------------------------ [Exercício] Aula 10


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
# a = float(input("Digite um valor de um lado: "))
# b = float(input("Digite um valor de um lado: "))
# c = float(input("Digite um valor de um lado: "))
#
# if triangulo_valido(a, b, c):
#     print(f"{a}, {b} e {c} formam um triângulo VÁLIDO!")
# else:
#     print(f"{a}, {b} e {c} NÃO formam um triângulo VÁLIDO!")
# ----------------------------------------------------------- (Resolução) [Exercício] Aula 10