from random import randint
print('#'* 30)
print('JOKENPÔ'.center(30))
print('#' * 30)
itens = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)
#---------------------------------------------------------------------------------------------------------------------
while True:
    player = int(input('''Escolha uma opção:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    : '''))
    if itens[player] == itens[pc]:
        print('Empate!')

    elif itens[player] == 'Pedra' and itens[pc] == 'Tesoura':
        print('Você venceu!')

    elif itens[player] == 'Papel' and itens[pc] == 'Pedra':
        print('Você venceu!')

    elif itens[player] == 'Tesoura' and itens[pc] == 'Papel':
        print('Voce venceu!')

    else:
        print('Você Perdeu!')
    print(f'Voce jogou {itens[player]} e o computador jogou {itens[pc]}')
#----------------------------------------------------------------------------------------------------------------------
    resp = str(input('Deseja jogar novamente? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
