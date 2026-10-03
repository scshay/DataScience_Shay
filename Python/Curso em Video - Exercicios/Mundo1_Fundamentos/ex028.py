import random 
from time import sleep   # É uma função explicada na resolução para dar 'suspense' no processamento do  bloco condicional

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

numero = random.randint(0,5)
aposta = int(input(f'Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)   # Vai aguardar 2 segundos para seguir com a próxima linha de código
if numero == aposta:
    print(f'VOCÊ ME VENCEU! Tu leu minha mente quando pensei no número {numero}!')
else:
    print(f'GANHEI! Eu pensei no número {numero} e não no {aposta}!')
