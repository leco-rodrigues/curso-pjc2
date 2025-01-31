import jokenpo_utils as jkp


DRAW = 0
VICTORY_1 = 1
VICTORY_2 = 2
VICTORY_3 = 3
J1 = jkp.insert_name('Jogador 1, insira o seu nome: ')
J2 = jkp.insert_name('Jogador 2, insira o seu nome: ')
choices = jkp.request_choices()

if range(len(choices)) == range(2):
    result = jkp.jokenpo_2P(choices[0], choices[1])
    for i, choice in enumerate(choices):
        print(f'Jogador {i + 1}: {choice}.')
    if result == DRAW:
        print('Empate!')
    elif result == VICTORY_1:
        print('Jogador 1 venceu!')
    else:
        print('Jogador 2 venceu!')        
else:
    result = jkp.jokenpo_3P(choices[0], choices[1], choices[2])
    for i, choice in enumerate(choices):
        print(f'Jogador {i + 1}: {choice}.')
    if result == DRAW:
        print('Empate!')
    elif result == VICTORY_1:
        print('Jogador 1 venceu!')
    elif result == VICTORY_2:
        print('Jogador 2 venceu!')
    elif result == VICTORY_3:
        print('Jogador 3 venceu!')
    else:
        print('Ninguém venceu!')
# ------------------------------ [Exercício] Aula 14