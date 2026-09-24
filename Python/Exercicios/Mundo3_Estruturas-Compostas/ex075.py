a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

e = a,b,c,d     # Por questões de didática, vou sempre preferir colocar tuplas entre parênteses, mas nesse deixei assim para conseguir testar se sem também funciona (e funciona, rs)
print(f'Você digitou os valores {e} --- {type(e)}')     # Aqui é a confirmação de que criei uma tupla
print(f'O valor 9 apareceu {e.count(9)} vez(es)')
if e.count(3) > 0:
    print(f'O valor 3 apareceu na {e.index(3) + 1}º posição')
else: 
    print(f'O valor 3 não foi digitado em nenhuma posição')

print(f'O(s) valor(es) par(es) digitado(s) foi/foram:', end='')
p = ()   # necessário definir a variável senão bate em "NameError: name 'p' is not defined"
for indice, item in enumerate(e):
# Para conseguir o print final, precisamos criar uma nova tupla 'p' com apenas os valores pares.
# O 'enumerate' percorre cada elemento com seu índice para podermos testar se o número é par (e[indice] % 2 == 0). 
# Como a tupla é imutável, a forma correta de acrescentar um valor é 'p += (item,)', pois isso gera uma nova tupla contendo só os pares, que pode ser exibida no último print.
    if e[indice] % 2 == 0:
        p += (item,)
        print(f' {p[indice]}', end='')