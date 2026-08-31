print('-=' * 15)
i = 0
p0 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termos = int(input('Quantos termos? '))

while i != termos:
    pf = p0+(i*r)
    if i == termos - 1:
        i += 1
        print(f'{pf} → FIM')
    else:
        i += 1
        print(f'{pf} → ', end='')

# continuar = input('Deseja continuar? [S/N] ').strip().upper()
