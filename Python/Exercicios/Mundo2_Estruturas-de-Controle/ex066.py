i = s = n = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    i += 1
print(f'A soma dos {i} valores resultou em {s}.')