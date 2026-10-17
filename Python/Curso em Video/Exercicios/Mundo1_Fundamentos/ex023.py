import math

numero = input('Informe um número: ')

print(f'Analisando o número {numero}...')   # Tive que dar esse print para mostrar o número que o usuário digitou, senão, apareceria com todas as manipulações necessárias
numero = str(math.trunc(float(numero))).zfill(4)   # Aqui eu estou primeiro convertendo o número para float, depois para inteiro e por fim para string; O método zfill() preenche a STRING com zeros à esquerda até atingir o comprimento especificado

print(f'Unidade: {numero[-1]}')   # Aqui eu estou pegando o último caractere da string, que é a unidade
print(f'Dezena: {numero[-2]}')   # Aqui eu estou pegando o penúltimo caractere da string, que é a dezena
print(f'Centena: {numero[-3]}')   # Aqui eu estou pegando o antepenúltimo caractere da string, que é a centena
print(f'Milhar: {numero[-4]}')   # Aqui eu estou pegando o quarto caractere da string, que é o milhar
