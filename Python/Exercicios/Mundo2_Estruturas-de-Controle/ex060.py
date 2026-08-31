import math

n = int(input('Digite um número para calcular seu fatorial: '))

fatorial = math.factorial(n)

print(f'Calculando {n}! =', end='')
for i in range(n,0,-1):
    if i == 1:
        print(f' {i} = {fatorial}')
    else:
        print(f' {i} x', end='')