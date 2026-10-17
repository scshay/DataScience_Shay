import datetime as dt

ano = int(input('Ano de nascimento: '))
alistamento = ano + 18 
atual = dt.date.today().year
print(f'Quem nasceu em {ano}, tem {atual - ano} anos em {atual}.')

if atual > alistamento:
    print(f'Eitaaaa, chama o general! Você já deveria ter se alistado há {atual - alistamento} anos em {alistamento}.')
elif atual == alistamento:
    print(f'CHEGOU SUA HORA! Você tem que se alistar IMEDIATAMENTE nesse ano de {atual}.')
else:
    print(f'Ainda faltam {alistamento - atual} anos para para o seu alistamento. \nSeu alistamento será em {alistamento}.')
