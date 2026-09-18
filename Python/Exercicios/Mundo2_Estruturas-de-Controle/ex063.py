n = int(input('Quantos termos de Fibonacci você quer ver? '))
i = 3     # Variável i é inicializada com 3, pois os dois primeiros termos da sequência de Fibonacci (0 e 1) já foram definidos.
p0 = 0
p1 = 1
s = 0

print('~' * 25)
print(f'{p0} → {p1} ', end='')
while i <= n:
    i += 1
    s = p0 + p1
    p0 = p1
    p1 = s
    if i == n+1:
        print(f'→ {s} → FIM')
    else:
        print(f'→ {s} ', end='')
#print(' → FIM')     (((Na resolução do professor, ele colocou sem o IF e o FIM depois do while, porque o while imprimiria o último termo da sequência e o FIM ficaria na mesma linha.)))
print('~' * 25)
