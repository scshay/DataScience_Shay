vTotal = []
vPar = []
vImpar = []

while True:
    valor = int(input('Digite um valor: '))
    vTotal.append(valor)
    if valor % 2 == 0:
        vPar.append(valor)
    else: 
        vImpar.append(valor)
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print(f'A lista completa é {vTotal}')
print(f'A lista de pares é {vPar}')
print(f'A lista de ímpares é {vImpar}')
