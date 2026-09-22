import random

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

i = 0
while True:
   pc = random.randint(0, 10)
   n = int(input('Diga um valor (de 0 a 10): '))
   escolha = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
   while escolha not in 'PIÍ':
     escolha = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
   s = n + pc
   print(f'Você jogou {n} e o computador jogou {pc}. Total de {s} deu {'PAR' if s % 2 == 0 else 'ÍMPAR'}')
   print('-' * 15)
   if escolha == 'P' and s % 2 == 0:
      i += 1
      print('Você VENCEU!\nVamos jogar novamente...')
   elif escolha in 'IÍ' and s % 2 != 0:
      i += 1
      print('Você VENCEU!\nVamos jogar novamente...')
   else:
      print(f'Você PERDEU!')
      print('=-' * 15)
      print(f'GAME OVER! Você venceu {i} vez(es).')
      break
