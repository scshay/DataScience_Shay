print('='*30)
print(f'{'BANCO CEV':^30}')
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))

saque = valor
cinquenta = vinte = dez = um = 0

# Solução que não precisa de while (ex071.1.py), que tem vários while (ex071.2.py) e aque utiliza apenas um while é a apresentada abaixo.
while True:
    if saque == 0:
        break
    if saque >= 50:
        saque -= 50
        cinquenta += 1
    elif saque >= 20:
        saque -= 20
        vinte += 1
    elif saque >= 10:
        saque -= 10
        dez += 1
    elif saque >= 1:
        saque -= 1
        um += 1
print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')