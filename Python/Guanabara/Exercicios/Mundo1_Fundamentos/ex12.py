valor = float(input('Valor original do produto: '))
desconto = float(input('Qual a porcentagem do desconto? '))
print(f'De RS${valor:.2f}, com o desconto de {desconto}%, o produto passa a custar RS${valor-(valor*(desconto/100)):.2f}.')
