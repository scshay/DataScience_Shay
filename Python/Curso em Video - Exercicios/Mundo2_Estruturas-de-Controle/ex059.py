numeros = []

for n in range(1,3):
    numero = float(input(f'Digite o {n}º número: '))
    numeros.append(numero)

i = int(input('''Escolha uma das opções a seguir:
[ 1 ] Somar
[ 2 ] Multiplicar 
[ 3 ] Maior 
[ 4 ] Novos números 
[ 5 ] Sair do programa 
'''))

while i != 5:
    if i == 1:
        soma = sum(numeros)
        print(f'A soma dos números {numeros[0]} e {numeros[1]}, resulta em {soma}.')
        i = int(input('''\nEscolha uma das opções a seguir:
    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa 
    '''))
    
    if i == 2:
        multiplicacao = numeros[0] * numeros[1]
        print(f'A multiplicação entre os números {numeros[0]} e {numeros[1]}, resulta em {multiplicacao}.')
        i = int(input('''\nEscolha uma das opções a seguir:
    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa 
    '''))

    if i == 3:
        maior = max(numeros)
        print(f'O maior número entre {numeros[0]} e {numeros[1]} é o {maior}.')
        i = int(input('''\nEscolha uma das opções a seguir:
    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa 
    '''))

    if i == 4:
        numeros = []
        for n in range(1,3):
            numero = float(input(f'Digite o {n}º número: '))
            numeros.append(numero)

        i = int(input('''\nEscolha uma das opções a seguir:
    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa 
    '''))

print('Obrigada e volte sempre!')
