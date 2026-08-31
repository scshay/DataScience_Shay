n = int(input('Quantos termos de Fibonacci você quer ver? '))
i = 3
p0 = 0
p1 = 1
s = 0

print(f'{p0} → {p1} ', end='')
while i <= n:
    i += 1
    s = p0 + p1
    p0 = p1
    p1 = s
    print(f'→ {s} ', end='')
