import numpy as np
import math

numeros = [30,4,10,45]

# Proposta do exercício é não ter input, mas se tivesse, eu faria como está digitado abaixo
# while True:
#     numero = float(input('Digite o número que deseja adicionar à lista: '))
#     numeros.append(numero)
#     continuar = input('Deseja continuar [S/N]? ')[0]
#     if continuar not in 'Ss':
#         break

def somarMultiplosNumeros():
    soma = np.sum(numeros)
    return print(f'O total dos itens da lista resulta em {soma}')

def multiplicarMultiplosNumeros():
    multiplicação = math.prod(numeros)
    return print(f'A multiplicação resulta em {multiplicação}')

inteiros = []
def ehInteiro():
    for n in numeros:
        if type(n) == int:
            n == True 
            inteiros.append(n)
    return print(f'Todos os números inteiros são: {inteiros}')

pares = []
def ehPar():
    for i in inteiros:
        if i % 2 == 0:
            pares.append(i)
    return print(f'Os números pares são: {pares}')

def menu():
    print('\n1 - Soma')
    print('2 - Multiplicação')
    print('3 - Quais são os números inteiros')
    print('4 - Quais são os pares')
    print('5 - Sair da calculadora')
    opcao = input(f'Para os seguintes números {numeros}, deseja realizar qual operação? ')

    if opcao == '1':
        somarMultiplosNumeros()
    elif opcao == '2':
        multiplicarMultiplosNumeros()
    elif opcao == '3':
        ehInteiro()
    elif opcao == '4':
        ehPar()
    elif opcao == '5':
        print('Obrigada pela visita, até mais :)')
        return False
    else: 
        print('Entrada inválida! Tente novamente.')
    
    return True

while True:
    continuar = menu()
    if not continuar:
        break
