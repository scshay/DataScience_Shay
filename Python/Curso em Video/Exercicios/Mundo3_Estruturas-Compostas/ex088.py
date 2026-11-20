import random
import time

print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)

n_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'\n{'-='*3} SORTEANDO {n_jogos} JOGOS {'-='*3}')
for i in range(1,n_jogos+1):
    time.sleep(1.5)
    # Funcionamento do sorteio:
    # 1. range(1, 61) cria a sequência fixa de opções (números inteiros de 1 a 60).
    # 2. random.sample(..., 6) age como o globo de sorteio: recebe essas 60 opções e retira 6 números aleatórios sem repetição, devolvendo uma lista.
    #  .sample() sempre vai retornar uma lista (mesmo que a coleção passada seja de 1 item), independentemente do tipo de coleção que você passar como entrada (lista, tupla, string, etc)
    print(f'Jogo {i}: {random.sample(range(1,61),6)}')
print(f'\n{'-='*3} < BOA SORTE! > {'-='*3}')

'''Resolução completamente diferente do Guanabara e mais performática, o código dele tem 27 linhas.'''