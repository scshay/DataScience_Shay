n = int(input('Digite um número: '))

amarelo = '\033[33m'
vermelho = '\033[31m'
limpa = '\033[m'
cont = 0 

for i in range(1,n+1):
    if n % i == 0:
        print(f'{amarelo}{i}{limpa}', end=' ')
        cont += 1
    else:
        print(f'{vermelho}{i}{limpa}', end=' ')

print(f'\nO número {n} foi divisível {cont} vezes.')
if cont == 2:
    print(f'E por isso ele É PRIMO!')
else:
    print(f'E por isso ele NÃO é PRIMO!')