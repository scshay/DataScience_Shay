import random

a1 = input('Escreva o nome do primeiro aluno: ')
a2 = input('Agora do segundo aluno: ')
a3 = input('Do penúltimo aluno: ')
a4 = input('Por fim, do último aluno: ')

print(f'O aluno sorteado foi o(a)... {random.choice([a1,a2,a3,a4])}!')
