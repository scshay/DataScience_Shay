maior = homens = mulheres = 0

while True:
    print('-' * 15)
    print('CADASTRE UMA PESSOA')
    print('-' * 15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
       sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 15)
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
         continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    if continuar == 'N':
        print('===== FIM DO PROGRAMA =====')
        print(f'Total de pessoas com mais de 18 anos: {maior}')
        print(f'Ao todo, temos {homens} homens cadastrados.')
        print(f'E temos {mulheres} mulheres com menos de 20 anos.')
        break