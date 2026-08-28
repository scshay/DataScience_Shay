import random 
import time

cont_user = 0
pc = random.randint(0,10)
user = int(input('Adivinhe em qual número estou pensando de 0 a 10: '))
print('1..')
time.sleep(0.5)
print('2..')
time.sleep(0.5)
print('3..')

while pc != user:
    cont_user += 1
    print(f'\nPuuutz, não foi dessa vez... eu pensei no número {pc} e você em {user}!')
    pc = random.randint(0,10)
    user = int(input('Tente novamente, um número de 0 a 10: '))

print(f'Você me venceu! Pensamos em {pc} e {user}; você precisou de {cont_user} tentativa(s) para me vencer!!!')