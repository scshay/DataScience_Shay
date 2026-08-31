parada = 999
i = 0
s = 0
n = 0

while n != 999:
    i += 1
    n = int(input(f'Digite o {i}º número inteiro: '))
    s += n
    if n == 999:
        s -= 999
print(f'A soma de todos os números inteiros é de {s}')