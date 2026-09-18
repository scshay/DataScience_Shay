import math

n = int(input('Digite um número para calcular seu fatorial: '))
i = n
f = math.factorial(n)

print(f'Calculando {n}! =', end='')
while i > 1:
    i -= 1
    if i == 1:
        print(f' {i} = {f}')
    else:
        print(f' {i} x', end='')