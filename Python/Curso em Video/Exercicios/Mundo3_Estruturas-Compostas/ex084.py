pessoas = []
dado = []
peso = []

while True:
    dado.append(input('Nome: ').strip().capitalize())
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    continuar = input('Quer continuar? [S/N] ')[0]
    while continuar not in 'SsNn':
        print('Entrada inválida, tente novamente...')
        continuar = input('Quer continuar? [S/N] ')[0]
    if continuar in 'Nn':
        break

print('-='*20)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
for i in range(0,len(pessoas)):
    peso.append(pessoas[i][1])
print(f'O maior peso foi de {max(peso):.1f}kg. Peso de',end='')
for i in range(0,len(pessoas)):
    if pessoas[i][1] == max(peso):
        print(f' [{pessoas[i][0]}]',end='')
print(f'\nO menor peso foi de {min(peso):.1f}kg. Peso de',end='')
for i in range(0,len(pessoas)):
    if pessoas[i][1] == min(peso):
        print(f' [{pessoas[i][0]}]',end='')
