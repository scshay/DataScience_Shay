custo = []

print('-' * 15)
print('LOJA CEV')
print('-' * 15)

i = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    custo.append(preco)
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if preco > 1000:
        i += 1
    if preco == min(custo):
        barato = produto
    if continuar == 'N':
        print('===== FIM DO PROGRAMA =====')
        print(f'O total da compra foi de R${sum(custo):.2f}')
        print(f'Temos {i} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi o que custa R${min(custo):.2f} ({barato})')
        break