s = 0

for c in range(1,7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        s += n
print(f'A soma de todos os valores pares digitados resulta em {s}.')
