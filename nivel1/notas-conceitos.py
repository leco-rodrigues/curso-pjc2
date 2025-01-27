# Converter "notas numéricas" em "notas conceituais" ("A", "B", "C", "D", e "F")
    
    # Função para mensagem de erro
def mensagem_erro(msg = 'Entrada inválida'):
    print(msg)

def sim_não():
    while True:
        continuar = input('Deseja continuar (s/n)? ')
        if continuar.lower().strip() in ['s', 'sim']:
            break
        elif continuar.lower().strip() in ['n', 'não']:
            print('Encerrando o programa')
            exit()
        else:
            mensagem_erro()

    # Função para conversão de notas
def nota_conceitual(nota):
    notas = ['A', 'B', 'C', 'D', 'F']
    if nota > 8:
        nota = notas[0]
        return nota
    elif nota == 8:
        nota = notas[1]
        return nota
    elif nota == 7:
        nota = notas[2]
        return nota
    elif nota == 6:
        nota = notas[3]
        return nota
    else:
        nota = notas[4]
        return nota

    # Função para nota da prova final
def prova_final():
    notas = ['A', 'B', 'C', 'D', 'F']
    while True:
        nota_pf = 'F' # provisória
        if nota_pf in notas:
            if nota_pf in [notas[0], notas[1], notas[2], notas[3]]:
                print('Aprovado na prova final!')
                break
            else:
                return False
        else:
            mensagem_erro()

    # Função para nota de recuperação
def recuperação():
    notas = ['A', 'B', 'C', 'D', 'F']
    while True:
        nota_r = 'A' # provisória
        if nota_r in notas:
            if nota_r == notas[0] or nota_r == notas[1] or nota_r == notas[2] or nota_r == [3]:
                print('Aprovado na recuperação!')
                break
            else:
                print('Reprovado!')
                break
        else:
            mensagem_erro()

   # Nota e médias (provisórias)
nota = 6
media_alta = 8
media_baixa = 6

if 0 <= nota <= 10:
    nota = nota_conceitual(nota)
    print(f'O aluno tirou nota {nota} na prova!')
    notas = ['A', 'B', 'C', 'D', 'F']
    if nota in [notas[0], notas[1]]:
        print('Aprovado direto!')
    elif nota in [notas[2], notas[3]]:
        print('Fazer prova final!')
        sim_não()
        if not prova_final():
            print('Fazer recuperação!')
            sim_não()
            recuperação()
else:
    mensagem_erro()
# ---------------- [Exercício] Aula 3