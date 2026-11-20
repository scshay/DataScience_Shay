import numpy as np

alunos = list()

while True:
    # nome = []   --- Comentei esse código porque achei o código do Guanabra muito mais performático com a sintaxe abaixo de inserir as variáveis direto na lista 
    nome = input('Nome: ').strip().capitalize()
    notas = []
    for i in range(1,3):
         notas.append(float(input(f'Nota {i}: ')))
    alunos.append([nome,notas,float(np.mean(notas))])
    continuar = input('Quer continuar? [S/N] ')[0]
    if continuar not in 'Ss':
        break

print('-='*25)
print(f'{'Nº':<5}{'Nome':<15}{'Média':<5}')
print('-'*len(f'{'Nº':<5}{'Nome':<15}{'Média':<5}'))
for aluno in alunos:
     print(f'{alunos.index(aluno):<5}{aluno[0]:<15}{aluno[2]:<5}')
print('-'*len(f'{'Nº':<5}{'Nome':<15}{'Média':<5}'))

while True:
    i = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
    if i == 999:
            print('FINALIZANDO...')
            print('<<<  VOLTE SEMPRE >>>')
            break
    print(f'Notas de {alunos[i][0]} são {alunos[i][1]}')
    print('-'*len(f'Notas de {alunos[i][0]} são {alunos[i][1]}'))
