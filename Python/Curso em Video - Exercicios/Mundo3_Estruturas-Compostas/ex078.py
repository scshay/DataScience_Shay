valores = []

for i in range(0,5):
    valor = int(input(f'Digite um valor para a posição {i}: '))
    valores.append(valor)

print('=-' * 20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi o {max(valores)} na(s) posição(ões)', end='')
for posicao, item in enumerate(valores):
    if item == max(valores):
        print(f' {posicao}...', end='')
print(f'\nO menor valor digitado foi o {min(valores)} na(s) posição(ões)', end='')
for posicao, item in enumerate(valores):
    if item == min(valores):
        print(f' {posicao}...', end='')