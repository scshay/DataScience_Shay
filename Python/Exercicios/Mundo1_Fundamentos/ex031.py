d = float(input(f'Qual é a distância da sua viagem? '))

preco = d*0.5 if d<=200 else d*0.45   # O if ternário é um atalho para escrever a estrutura if/else em apenas uma linha (é da resolução do Guanabara) 
'''if d <= 200:
    preco = d*0.5
else:
    preco = d*0.45'''
print(f'Você está prestes a começar uma viagem de {d:.2f}km\nE o preço da sua passagem será de RS${preco:.2f}.')