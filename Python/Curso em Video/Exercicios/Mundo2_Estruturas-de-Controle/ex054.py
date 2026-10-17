import datetime as dt

atual = dt.date.today().year
maior = 0
menor = 0

for i in range(1,8):
    ano = int(input(f'Em que ano a {i}º pessoas nasceu? '))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')