n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2

print(f'Tirando {n1} e {n2}, a média do aluno é {media:.1f}.')
if media >= 7:
    print(f'O aluno está APROVADO.')
elif 7 > media >= 5:
    print(f'O aluno está em RECUPERAÇÃO.')
else:
    print(f'O aluno está REPROVADO.')
