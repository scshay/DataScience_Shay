maior = 0 
menor = 0 

for i in range(1,6):
    peso = float(input(f'Peso da {i}º pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:.2f}kg.')
print(f'O menor peso lido foi de {menor:.2f}kg.')
