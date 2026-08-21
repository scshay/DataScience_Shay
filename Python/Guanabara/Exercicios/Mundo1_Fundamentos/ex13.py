sal = float(input('Salário bruto: '))
aumento = float(input('Em número inteiro, qual a porcentagem do aumento? '))
print(f'De RS${sal:.2f}, com o aumento de {aumento}%, o salário aumenta para RS${sal*(1+(aumento/100)):.2f}.')
