i = s = n = 0

while n != 999:
    i += 1
    n = int(input(f'Digite o {i}º número inteiro [999 para parar]: '))
    s += n
    if n == 999:
        s -= 999
print(f'A soma de todos os {i-1} números inteiros resulta em {s}')
