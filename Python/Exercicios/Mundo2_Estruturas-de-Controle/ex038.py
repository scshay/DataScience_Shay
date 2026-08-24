n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

if n1 > n2:
    print(f'O PRIMEIRO valor "{n1:.2f}" é maior.')
elif n2 > n1:
    print(f'O SEGUNDO valor "{n2:.2f}" é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
