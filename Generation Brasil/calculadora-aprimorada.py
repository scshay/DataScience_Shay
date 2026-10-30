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
somarMultiplosNumeros()

def multiplicarMultiplosNumeros():
    multiplicação = math.prod(numeros)
    return print(f'Já a multiplicação resulta em {multiplicação}')
multiplicarMultiplosNumeros()

inteiros = []
def ehInteiro():
    for n in numeros:
        if type(n) == int:
            n == True 
            inteiros.append(n)
    return print(f'Todos os números inteiros são: {inteiros}')
ehInteiro()

pares = []
def ehPar():
    for i in inteiros:
        if i % 2 == 0:
            pares.append(i)
    return print(f'Os pares são: {pares}')
ehPar()
