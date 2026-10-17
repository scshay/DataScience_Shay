velocidade = float(input(f'Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print(f'MULTADO! Você excedeu o limite permitido de 80km/h\nVocê deve pagar uma multa de RS${multa:.2f}!')
print(f'Tenha um bom dia! Dirija com segurança!')