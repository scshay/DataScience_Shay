numeros = []

n = int(input('Digite um número: '))
numeros.append(n)
continuar = input('Quer continuar? [S/N] ').strip().upper()
while continuar == 'S':
    n = int(input('Digite um número: '))
    numeros.append(n)
    continuar = input('Quer continuar? [S/N] ').strip().upper()

media = sum(numeros)/len(numeros)
print(f'Você digitou {len(numeros)} números e a média foi {media}')
print(f'O maior valor foi {max(numeros)} e o menor foi {min(numeros)}')
print(numeros)