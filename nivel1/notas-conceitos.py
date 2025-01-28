# Converter "notas numéricas" em "notas conceituais" ("A", "B", "C", "D", e "F")
    # Mensagem de erro
def mensagem_erro(msg = 'Entrada inválida'):
    print(msg)

    # Continuar executando o programa ou não
def sim_não():
    while True:
        continuar = input('Deseja continuar (s/n)? ')
        if continuar.lower().strip() in ['s', 'sim']:
            break
        elif continuar.lower().strip() in ['n', 'não']:
            raise SystemExit('Encerrando o programa')
        else:
            mensagem_erro('Digite "Sim" ou "Não"')

    # Conversão de notas
def nota_conceitual(nota, notas):
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

    # Nota da prova final
def prova_final(notas):
    while True:
        nota_pf = 'A' # provisória
        if nota_pf in notas:
            if nota_pf in [notas[0], notas[1], notas[2], notas[3]]:
                raise SystemExit('Aprovado na prova final!')
            else:
                return
        else:
            mensagem_erro('Digite uma nota válida')

    # Nota de recuperação
def recuperação(notas):
    while True:
        nota_r = 'A' # provisória
        if nota_r in notas:
            if nota_r == notas[0] or nota_r == notas[1] or nota_r == notas[2] or nota_r == [3]:
                raise SystemExit('Aprovado na recuperação!')
            else:
                SystemExit('Reprovado!')
        else:
            mensagem_erro('Digite uma nota válida')

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
    mensagem_erro('Digite uma nota válida')
# ---------------- [Exercício] Aula 3