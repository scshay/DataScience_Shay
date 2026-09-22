while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * len('Quer ver a tabuada de qual valor?'))
    if n <= 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    i = 1
    while i <= 10:
        print(f'{n} x {i} = {n*i}')
        i += 1  
    print('-' * len('Quer ver a tabuada de qual valor?'))
