# Resolução OG minha está no arquivo ex075.1.py
# Gostei mais da do Guanabara (criar tupla desde o input do usuário) e por isso, refiz abaixo.

numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vez(es)')
if numeros.count(3) >= 1:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print('O valor 3 apareceu em posição nenhuma')
print('Os valores pares digitados foram:', end='')
for n in numeros:
    if n % 2 == 0:
        print(f' {n}', end='')