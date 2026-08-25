print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

p0 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
pf = p0+(10*r)   # Esse aqui Guanabara ajudou porque não cheguei na fórmula final

for c in range(p0,pf,r):
    print(f'{c} →', end=' ')
print('FIM!!!')