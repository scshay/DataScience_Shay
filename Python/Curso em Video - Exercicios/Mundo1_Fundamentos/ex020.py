import random

a1 = input('Escreva o nome do primeiro aluno: ')
a2 = input('Agora do segundo aluno: ')
a3 = input('Do penúltimo aluno: ')
a4 = input('Por fim, do último aluno: ')

lista = [a1,a2,a3,a4]
random.shuffle(lista)

print(f'A ordem de apresentação será: {lista}')
