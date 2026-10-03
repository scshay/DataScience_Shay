import datetime as dt

ano = int(input('Ano de nascimento: '))
idade = dt.date.today().year - ano

print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Classificação: MIRIM.')
elif 14 >= idade > 9:   # Se não cair no 1º IF, já testa o segundo, por isso que o Guanabara explicou que seria mais vantajoso colocar "idade <= 14" (mais légivel)
    print(f'Classificação: INFANTIL.')
elif 19 >= idade > 14:   # "idade <= 19"
    print(f'Classificação: JÚNIOR.')
elif 25 >= idade > 19:   # "idade <= 25"
    print(f'Classificação: SÊNIOR.')
else:
    print(f'Classificação: MASTER.')
