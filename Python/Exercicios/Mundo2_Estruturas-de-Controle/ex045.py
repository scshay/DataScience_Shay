import random
import time

usuario = int(input('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura
Qual a sua jogada? '''))

if usuario not in (0,1,2):
    print('Opção inválida, tente novamente!')
else: 
    opcoes = ['Pedra','Papel','Tesoura']
    pc = int(random.choice('012'))
    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PÔ!!!')

    print('-='*15)
    print(f'Computador jogou {opcoes[pc]}')
    print(f'Usuário jogou {opcoes[usuario]}')
    print('-='*15)

    if usuario == pc:
        print('Vocês jogaram igual. Tente novamente!')
    elif usuario == 0:
        if pc == 2:
            print('Usuário VENCE')
        else:
            print('Computador VENCE')
    elif usuario == 1:
        if pc == 0:
            print('Usuário VENCE')
        else:
            print('Computador VENCE')
    elif usuario == 2:
        if pc == 1:
            print('Usuário VENCE')
        else:
            print(f'Computador VENCE')
    else: 
        print(f'Combinação não mapeada')