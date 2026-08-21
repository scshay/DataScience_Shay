print('Vamos descobrir quanto de tinta é necessário para pintar a sua parede!')
largura = float(input('Em metros, qual a largura da sua parede? '))
comprimento = float(input('O comprimento, em metros? '))
print(f'Para pintar {largura*comprimento} m², {largura} m por {comprimento} m, você precisa de {((largura*comprimento)/2):.2f} litros de tinta (a tinta rende 2 m² por litro).')
