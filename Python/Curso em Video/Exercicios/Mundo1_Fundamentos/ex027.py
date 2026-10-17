nome = input('Digite seu nome completo: ').strip()  # Lembrando que strip() remove espaços antes e depois do nome da cidade, caso o usuário digite algum espaço a mais. A função upper() é usado para não termos problemas com a forma que o usuário digitou o nome da cidade

print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu último nome é {nome.split()[-1]}')
