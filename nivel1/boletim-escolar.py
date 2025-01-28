# Exibir o boletim escolar de um aluno
    # Mensagem de erro
def mensagem_erro(msg = 'Entrada inválida'):
    print(msg)

    # Para inserir textos
def inserir_texto(pergunta = ''):
    while True:
        nome = input(pergunta).strip()
        if nome and all(letra.isalpha() or letra.isspace() for letra in nome):
            return nome
        mensagem_erro()

    # Para inserir números
def inserir_numero(pergunta = 'Texto: '):
    while True:
        num = input(pergunta).strip()
        if num and all(char.isnumeric() or char.isspace() for char in num):
            return num
        mensagem_erro()

    # Dados do boletim
ano = inserir_numero('Ano: ')
escola = inserir_texto('Escola: ')
nome = inserir_texto('Nome: ')
disciplinas = ('Português', 'Matemática', 'Ciências', 'Estudos Sociais')
notas = [
    [8, 10, 9, 7], # 1° Bimestre
    [8, 10, 9, 7], # 2° Bimestre
    [7, 10, 8, 6], # 3° Bimestre
    [6, 9, 7, 6] # 4° Bimestre
    ]

faltas = [
    [0, 0, 0, 0], # 1° Bimestre
    [0, 0, 0, 0], # 2° Bimestre
    [4, 0, 4, 4], # 3° Bimestre
    [5, 4, 5, 4] # 4° Bimestre
]

    # Exibição do Boletim
print(f'\tBoletim Escolar {ano}, escola {escola}\n')
print(f'O aluno {nome} obteve o seguinte desempenho:\n')
for bimestre in range(4):
    print(f' {bimestre + 1}° Bimestre:')
    for i, disciplina in enumerate(disciplinas):
        print(f'{disciplina} - Nota: {notas[bimestre][i]}, Faltas: {faltas[bimestre][i]}')
    print() # Linha em branco para separar os bimestres
# --------- [Exercício] Aula 5
