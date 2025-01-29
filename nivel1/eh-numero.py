# Dizer se um texto é um número ou não

# Passo 1: Criar uma função para tratamento de texto
def alpha_numeric(txt):
    num = txt.split('.')
    if num and all(car.isdigit() for car in num):
        return True
    return False

# Passo 2: Receber uma entrada de texto
txt = input('Digite algo: ').strip()

# Passo 3: Exibir o resultado
if alpha_numeric(txt):
    print('É um número!')
else:
    print('Não é um número...')
# ----------------------------- [Exercício] Aula 8