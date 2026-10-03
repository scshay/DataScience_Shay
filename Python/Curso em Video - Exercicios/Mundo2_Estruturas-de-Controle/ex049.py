n = int(input('Digite um número para ver sua tabuada: '))
# cont = 0   - Deixei com contador, mas na resolução vi que o próprio nome que precisamos dar no laço for é a variável que precisamos utilizar para ter o 1,2,3,4,5...

for i in range(1,11):   # Veja que o que colocamos após o for é sempre necessário, independente se utilizamos ou não... e, para esse caso, precisamos, por isso, ele mesmo é utilizado para multiplicar o valor escolhido pela usuário
    # cont += 1
    # print(f'{n} x {cont} = {n*cont}')
    print(f'{n} x {i} = {n*i}')