valores = []
continuar = 'S'

while continuar == 'S':
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar ;)')
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Entrada inválida, tente novamente. Quer continuar? [S/N] ').strip().upper()[0]
valores.sort()   #Não é possível printar direto a lista em ordem crescente, porque o método lista.sort() altera a lista original "no mesmo lugar" e retorna None (nada). Se eu fizer print(lista.sort()), a tela vai exibir apenas a palavra None
print('-=' * 20)
print(f'Você digitou os valores {valores}')