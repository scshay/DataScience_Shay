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
    return print(soma)
somarMultiplosNumeros()

def multiplicarMultiplosNumeros():
    multiplicação = math.prod(numeros)
    return print(multiplicação)
multiplicarMultiplosNumeros()

inteiros = []
def ehInteiro():
    for n in numeros:
        if type(n) == int():
            n == True 
            inteiros.append(n)
ehInteiro()
print(inteiros)

# def ehPar():
#     for n in numeros:
#         if n % 2 == 0 and type(n) == int:
#             return True
#         else:
#             return False
# ehPar()

# def ehInteiro():
