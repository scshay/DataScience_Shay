s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

maior = max(s1,s2,s3)
resultado = sum([s1,s2,s3]) - maior
verde = '\033[4;32m'
vermelho = '\033[4;30;41m'
limpa = '\033[m'

if resultado > maior: 
    print(f'Os segmentos acima {verde}PODEM FORMAR{limpa} um triângulo ',end='')
    if s1 != s2 != s3 != s1:
        print(f'{verde}ESCALENO{limpa}.')
    elif s1 == s2 == s3:
        print(f'{verde}EQUILÁTERO{limpa}.')
    else: 
        print(f'{verde}ISÓSCELES{limpa}.')
else:
    print(f'Os segmento acima {vermelho}NÃO FORMAM{limpa} um triângulo.')