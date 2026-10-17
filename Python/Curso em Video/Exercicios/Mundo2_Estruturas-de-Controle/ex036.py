casa = float(input('Qual o valor do imóvel de interesse? R$'))
salario = float(input('De preferência o líquido, qual o seu salário? R$'))
anos = int(input('Em quantos anos vai pagar o imóvel? '))

parcela = casa / (anos * 12)
condicao = salario * 0.3

print(f'Para pagar um imóvel de R${casa:.2f} em {anos} anos, a parcela será de R${parcela:.2f}')
if parcela >= condicao:
    print('Empréstimo \033[4;30;41mNEGADO\033[m!')   # branco sublinhado com fundo vermelho: \033[4;30;41m e para ele não correr pra linha toda \033[m
else: 
    print('Empréstimo \033[4;34mCONCEDIDO\033[m!')   # azul sublinhado: \033[4;34m e para ele não correr pra linha toda \033[m
