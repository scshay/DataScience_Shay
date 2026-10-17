nomes = []
idades = []
contF = 0 
maxM = 0
maxMn = ''

for i in range(1,5):
    print(f'----- {i}º PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    nomes.append(nome)
    idades.append(idade)
    if sexo == 'M':
        if idade > maxM:
            maxM = idade
            maxMn = nome
    elif sexo == 'F':
        if idade < 20:
            contF += 1

media_idades = sum(idades) / len(idades)
print(f'A média de idade do grupo é de {media_idades:.1f} anos')
print(f'O homem mais velho tem {maxM} anos e se chama {maxMn}')
print(f'Ao todo, {contF} mulher(es) com menos de 20 anos.')