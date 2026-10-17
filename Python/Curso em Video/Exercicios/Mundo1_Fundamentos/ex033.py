v1 = float(input(f'Primeiro valor: '))
v2 = float(input(f'Segundo valor: '))
v3 = float(input(f'Terceiro valor: '))

# Verificando o maior números dos 3 digitados
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

# Verificando o menor número dos 3 digitados
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3

print(f'O menor valor digitado foi o {menor}')
print(f'O maior valor digitado foi o {maior}') 
