opcoes = ['F','M']

sexo = input('Qual o seu sexo? [F/M] ').strip().upper()
while sexo not in opcoes:
    print('Entrada inválida, tente novamente!')
    sexo = input('Qual o seu sexo? [F/M] ').strip().upper()