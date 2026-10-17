s = 0
cont = 0
for c in range(1,501):   # Outra forma de encontrar direto os ímpares é colocando o passo igual a 2 "range(1,501,2)" porque assim ele ficaria '1 3 5 7 9...'; continua tendo que tratar o divisível por 3
    if c % 2 != 0 and c % 3 == 0:
        s += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é de {s}.')
