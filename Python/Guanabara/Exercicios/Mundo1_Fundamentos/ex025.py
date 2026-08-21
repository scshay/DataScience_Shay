nome = input('Qual o seu nome completo? ').strip().upper()   # Lembrando que strip() remove espaços antes e depois do nome da cidade, caso o usuário digite algum espaço a mais. A função upper() é usado para não termos problemas com a forma que o usuário digitou o nome da cidade

print(f'Seu nome tem Silva? {'SILVA' in nome}')
