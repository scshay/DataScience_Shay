import random

# A variável 'a' recebe 5 valores aleatórios entre 0 e 10.
# A função random.choices(...) gera uma lista com esses números,
# e tuple(...) converte essa lista em uma tupla, para que os valores possam ser armazenados em uma estrutura imutável → e também porque era sobre aula de tuplas, rs
a = tuple(random.choices(range(0, 11), k=5))

print(a)
#print(f'Os valores sorteados foram: {a[0]} {a[1]} {a[2]} {a[3]} {a[4]}')     #Eu não gostei dessa forma (precisa saber o tamanho exato da tupla), mas foi a que encontrei sozinha, por isso deixei registrada aqui! 
print(f'Os valores sorteados foram:', end='')
for n in a:
    print(f' {n} ', end='')
print(f'\nO menor valor sorteado foi {min(a)}')
print(f'O maior valor sorteado foi {max(a)}')