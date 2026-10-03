print('='*30)
print(f'{'BANCO CEV':^30}')
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))

resto = valor
cinquenta = vinte = dez = um = 0

while True:   # Essa solução foi a que realmente pensei sem ajuda, mas não precisa do while de verdade (só deixando registrada mesmo). A solução que o while é realmente necessário está no arquivo ex071.2.py
    if valor % 50 > 0 or valor % 50 == 0:
        cinquenta = valor // 50
        resto = valor - (50 * (valor // 50))
    if resto % 20 > 0 or resto % 20 == 0:
        vinte = resto // 20
        resto = resto - (20 * (resto // 20))
    if resto % 10 > 0 or resto % 10 == 0:
        dez = resto // 10
        resto = resto - (10 * (resto // 10))
    if resto % 1 == 0:
        um = resto // 1
        resto = resto - (1 * (resto // 1))
    break
print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')