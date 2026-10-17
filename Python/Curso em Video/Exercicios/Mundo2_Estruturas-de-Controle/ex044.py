valor = float(input('Preço das compras: R$'))
opcao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA - Dinheiro/Cheque 
[ 2 ] À vista - Cartão 
[ 3 ] 2x - Cartão 
[ 4 ] 3x ou mais - Cartão
Digite sua opção: '''))

# Minha resolução não está errada, mas criei muitas variáveis, devo me lembrar que programador é preguiçoso e não há mal algum em tentar  simplificar o máximo possível 
# Guanabara criou somente uma variável total e foi adequando a conta de acordo com a opção do usuário; isso é bom porque fica mais fácil de fazer manutenção nas mensagens DADO QUE ao cair em um IF não há como cair em outro ao mesmo tempo e a variável "puxar mais de um valor"
if opcao == 1:
    desconto10 = valor - (valor*0.1)
    print(f'Sua compra terá 10% de desconto!')
    print(f'Sua compra de R${valor:.2f} vai custar R${desconto10:.2f} no final')
elif opcao == 2:
    desconto5 = valor - (valor*0.05)
    print(f'Sua compra terá 5% de desconto!')
    print(f'Sua compra de R${valor:.2f} vai custar R${desconto5:.2f} no final')
elif opcao == 3:
    print(f'Sua compra será parcelada em 2x de R${valor/2:.2f} (sem juros).')
elif opcao == 4:
    qtde = int(input('Quantas parcelas? '))
    ctotal = valor * 1.20
    parcela = ctotal/qtde
    print(f'Sua compra será parcelada em {qtde}x de R${parcela:.2f} (com juros).')
    print(f'Sua compra de R${valor:.2f} vai custar R${ctotal:.2f} no final')
else: 
    print(f'Opção inválida, tente novamente!')
