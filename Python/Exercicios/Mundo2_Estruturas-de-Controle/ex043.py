m = float(input('Em kg, qual o seu peso? '))
a = float(input('Em metros, qual a sua altura? '))

imc = m/(a**2)
amarelo = '\033[4;33m'
verde = '\033[4;32m'
vermelho = '\033[4;30;41m'
limpa = '\033[m'

print(f'O seu IMC é de {imc:.2f}')
# Note que eu só consigo colocar os intervalos com somente um lado da inequação, pois foi escrito em ordem crescente (decrescente também daria), senão, ao cair no 1º IF, validaria como certo e a mensagem errada seria imprimida
# Exemplo: 1º IF com 25 e o 2º com 18.5, ao digitar (72,1.70) imprimiria "Você está ABAIXO do peso normal, cuidado!" e não "PARABÉNS! Você está na faixa de PESO NORMAL."
if imc < 18.5:
    print(f'Você está {amarelo}ABAIXO{limpa} do peso normal, cuidado!')
elif imc < 25:
    print(f'PARABÉNS! Você está na faixa de {verde}PESO NORMAL{limpa}.')
elif imc < 30:
    print(f'Você está com SOBREPESO.')
elif imc <= 40:
    print(f'Você está com OBESIDADE.')
else: 
    print(f'{vermelho}Cuidado{limpa}! Você está com OBESIDADE MÓRBIDA.')
