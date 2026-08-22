frase = input('Digite uma frase: ').strip().upper()   # Lembrando que strip() remove espaços antes e depois do nome da cidade, caso o usuário digite algum espaço a mais. A função upper() é usado para não termos problemas com a forma que o usuário digitou o nome da cidade

print(f'A letra A aparece {frase.count('A')} vez(es) na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('A') + 1}.')
print(f'A última letra A apareceu na posição {frase.rfind('A') + 1}.')
