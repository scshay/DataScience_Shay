nome = input('Qual é o seu nome inteiro? ').strip()   # Lembrando que strip() remove espaços antes e depois do nome, caso o usuário digite algum espaço a mais.

maiusculas = nome.upper()
minusculas = nome.lower()
nomeSeparado = nome.split()   # Separa o nome em uma lista, onde cada elemento da lista é uma palavra do nome.
nomeJuntoSemEspaco = ''.join(nomeSeparado)

print(f'Todas as letras maiúsculas: {maiusculas}.')
print(f'Todas as letras minúsculas: {minusculas}.')
print(f'Prazer, {nome}!')
print(f'Seu nome completo tem {len(nomeJuntoSemEspaco)} letras.')
print(f'Seu primeiro nome tem {len(nomeSeparado[0])} letras.')
