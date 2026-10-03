import datetime as dt

ano = int(input(f'Que ano quer analisar? Para o ano atual, digite 0. '))
if ano == 0:
    ano = dt.date.today().year

# A minha solução abaixo ficou com muito IF/ELSE
if ano % 4 != 0:
    print(f'O ano {ano} NÃO é bissexto!')
else:
    if str(ano).endswith('00'):
        if ano % 400 == 0:
            print(f'O ano {ano} é BISSEXTO!')
        else: 
            print(f'O ano {ano} NÃO é bissexto!')
    else: 
       print(f'O ano {ano} é BISSEXTO!')

# Por isso, considero a resolução do Guanabara melhor; no entanto, vou deixar comentado porque não cheguei nesse ponto sem apoio de explicações e comentários
'''
# Por conta do OR, não precisa dos 2 lados serem True somente um lado serve, por isso que mesmo 2024 não tendo resto igual a 0 quando dividido por 400, ele é bissexto. Lembrando que... um ano é bissexto se for divisível por 4 e não por 100, OUUUUUUU se for diretamente divisível por 400.
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é bissexto!')
'''