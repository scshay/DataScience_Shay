print('-=' * 15)
i = 0
p0 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

while i < 10:
    pf = p0+(i*r)
    if i == 9:
        i += 1
        print(f'{pf} → FIM')
    else:
        i += 1
        print(f'{pf} → ', end='')
