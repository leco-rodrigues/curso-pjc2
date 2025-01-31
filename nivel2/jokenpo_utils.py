from getpass import getpass


def insert_name(player = 'Insira seu nome: '):
    while True:
        name = input(player).strip()
        if name and all(char.isalpha() or char.isnumeric() or char.isspace() for char in name):
            return name[:10].strip()
        else:
            print('Por favor, utilize apenas letras e números.')

def extra_player():
    while True:
        answer = input('Deseja adicionar mais um(a) jogador(a) (s/n)? ').lower().strip()
        if answer in ['s', 'sim']:
            jogador_extra = insert_name('Jogador 3, insira o seu nome: ')
            return jogador_extra
        elif answer in ['n', 'não']:
            return False
        else:
            print('Por favor, digite "Sim" ou "Não".')

def process_choice(choice):
    while True:
        choice = getpass(f'Jogador - Escolha "pedra", "papel" ou "tesoura": ')
        if choice.lower().strip() in ['pedra', 'papel', 'tesoura']:
            return choice.lower().strip()
        else:
            print('Por favor, escolha "pedra", "papel" ou "tesoura".')

def request_choices():
    choices = []
    choice = None
    players = ['J1' , 'J2']
    J3 = extra_player()
    if J3:
        players.append(J3)
    for i in players:
        choice = process_choice(choice)
        choices.append(choice)
    return choices

def jokenpo_2P(player1, player2):
    if player1 == player2:
        return 0
    elif ((player1 == 'pedra' and player2 == 'tesoura') or
          (player1 == 'papel' and player2 == 'pedra') or
          (player1 == 'tesoura' and player2 == 'papel')):
        return 1
    else:
        return 2

def jokenpo_3P(player1, player2, player3):
    if ((player1 == player2 == player3) or (player1 != player2 != player3)):
        return 0
    elif ((player1 == 'pedra' and player2 == 'tesoura' and player3 == 'tesoura') or
        (player1 == 'papel' and player2 == 'pedra' and player3 == 'pedra') or
        (player1 == 'tesoura' and player2 == 'papel' and player3 == 'papel')):
        return 1
    elif ((player2 == 'pedra' and player1 == 'tesoura' and player3 == 'tesoura') or
        (player2 == 'papel' and player1 == 'pedra' and player3 == 'pedra') or
        (player2 == 'tesoura' and player1 == 'papel' and player3 == 'papel')):
        return 2
    elif ((player3 == 'pedra' and player1 == 'tesoura' and player2 == 'tesoura') or
        (player3 == 'papel' and player1 == 'pedra' and player2 == 'pedra') or
        (player3 == 'tesoura' and player1 == 'papel' and player2 == 'papel')):
        return 3
    else:
        return
# ------------ [Exercício] Aula 14