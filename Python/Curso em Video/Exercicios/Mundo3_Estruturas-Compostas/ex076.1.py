tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*30)
print(f'{'LISTAGEM DE PREÇOS':^30}')
print('-'*30)

#Versão utilizando zip(); no ex076.2.oy tento fazer somente acessando os itens via índice
for item, preco in zip(tupla[::2], tupla[1::2]):
    print(f'{item:.<21}R${preco:>7.2f}')   #Sintaxe f-string= :[alinhamento][largura].[casas][tipo] -> :>7.2f (f = float/decimal)
