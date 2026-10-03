print('-=' * 15)
i = 0     #(((Declareando a variável i aqui, ela será resetada a cada vez que o usuário pedisse mais termos. O que significa que ao imprimir  os valores, teremos somente os valores dos termos que o usuário pediu, e não todos os termos da PA.)))
p0 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termos = int(input('Quantos termos? '))
continuar = 1 

while continuar != 0:
    while i != termos:
        pf = p0+(i*r)
        if i == termos - 1:
            i += 1
            print(f'{pf} → PAUSA')
        else:
            i += 1
            print(f'{pf} → ', end='')
    continuar = int(input('Quantos termos a mais deseja mostrar? '))
    if continuar != 0:
        termos += continuar
    elif continuar == 0:
        print(f'Obrigada por utilizar o programa!\nProgressão finalizada com {i} termos mostrados.')
