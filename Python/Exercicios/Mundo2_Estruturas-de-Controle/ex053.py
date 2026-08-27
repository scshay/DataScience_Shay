frase = input('Digite uma frase: ').strip().upper().split()

semEspaco = ''.join(frase)
inverso = semEspaco[::-1]

print(f'O inverso de {semEspaco} é {inverso}.')
if semEspaco == inverso:
    print('Por isso, temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É um palíndromo.')

# Resolução do Guanabara com for! 
'''
# 1. Lê a frase, remove espaços nas pontas (.strip()) e deixa tudo em maiúsculo (.upper())
frase = input('Digite uma frase: ').strip().upper()

# 2. Corta a frase nos espaços, criando uma lista de palavras separadas
palavras = frase.split()

# 3. Junta as palavras da lista em um bloco único de texto, sem nenhum espaço
junto = ''.join(palavras)

# 4. Cria uma variável de texto (string) vazia para guardar a frase invertida depois
inverso = ''

# 5. O laço FOR vai andar de trás para frente usando os índices (posições) das letras:
#    - Início: len(junto) - 1  -> Começa exatamente na posição da ÚLTIMA letra.
#    - Fim: -1                -> Vai até a posição 0 (o range para um número antes do limite).
#    - Passo: -1              -> Faz a contagem regredir de 1 em 1 (andar para trás).
for letra in range(len(junto) - 1, -1, -1):
    # Pega a letra da posição atual e gruda (concatena) no final da variável 'inverso'
    inverso += junto[letra]

# 6. Exibe o resultado da montagem manual na tela
print(junto, inverso)

# 7. Faz a verificação final para dar o veredito do palíndromo
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É um palíndromo.')
'''
