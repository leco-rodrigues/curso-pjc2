# Definir se um aluno está aprovado ou não, baseado em sua nota
    # Mensagem de erro
def mensagem_erro(msg = 'Entrada inválida'):
    print(msg)

    # Continuar executando o programa ou não
def sim_não():
    while True:
        continuar = input('Deseja continuar (s/n? ')
        if continuar.lower().strip() in ['s', 'sim']:
            break
        elif continuar.lower().strip() in ['n', 'não']:
            raise SystemExit('Encerrando o programa')
        else:
            mensagem_erro('Digite "Sim" ou "Não"')

    # Nota da prova final
def prova_final(media_baixa):
    while True:
        try:
            nota_pf = float(input('Nota da prova final: '))
            if 0 <= nota_pf <= 10:
                if nota_pf >= media_baixa:
                    raise SystemExit('Aprovado na prova final!')
                else:
                    return
            else:
                mensagem_erro('Digite uma nota válida')
        except ValueError:
            mensagem_erro('Digite uma nota válida')

    # Nota da recuperação
def recuperação(media_baixa):
    while True:
        try:
            nota_r = float(input('Nota da recuperação: '))
            if 0 <= nota_r <= 10 and all():
                if nota_r >= media_baixa:
                    raise SystemExit('Aprovado na recuperação!')
                else:
                    raise SystemExit('Reprovado!')
            else:
                mensagem_erro('Digite uma nota válida')
        except ValueError:
            mensagem_erro(mensagem_erro('Digite uma nota válida'))

    # Nota; Média alta; Média baixa
while True:
    try:
        nota = float(input('Nota: '))
        if 0 <= nota <= 10:
            break
        else:
            mensagem_erro('Digite uma nota válida')
    except ValueError:
        mensagem_erro('Digite uma nota válida')

while True:
    try:
        media_alta = int(input('Média alta: '))
        if 7 <= media_alta < 10:
            break
        else:
            mensagem_erro('Digite uma média alta válida')
    except ValueError:
        mensagem_erro('Digite uma média alta válida')

while True:
    try:
        media_baixa = int(input('Média baixa: '))
        if media_baixa < media_alta:
            break
        else:
            mensagem_erro('Digite uma média baixa válida')
    except ValueError:
        mensagem_erro('Digite uma média baixa válida')

if nota >= media_alta:
    print('Aprovado direto!')
elif nota >= media_baixa:
    print('Fazer prova final!')
    sim_não()
    if not prova_final(media_baixa):
        print('Fazer recuperação!')
        sim_não()
        recuperação(media_baixa)
else:
    print('Fazer recuperação!')
    sim_não()
    recuperação(media_baixa)
# -------------------[Exercício] Aula 3