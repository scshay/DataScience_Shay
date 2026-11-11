matriz = []
pares = []
coluna3 = []

# Loop externo: controla a criação de cada uma das 3 linhas (índices 0, 1 e 2)
for l in range(0, 3):
    # Cria uma lista temporária vazia para construir a linha atual do zero; é totalmente zerada toda vez que o loop externo começa uma nova rodada.
    linha = []
    
    # Loop interno: controla a criação das 3 colunas dentro da linha atual
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{l},{c}]: '))
        # Adiciona o número digitado ao final da lista temporária "linha"
        linha.append(n)  
    # Impressão de controle para averiguar valores da linha
    # print(linha)
    # Adiciona a lista "linha" inteira como um novo elemento dentro da lista "matriz"
    matriz.append(linha)
    # Impressão de controle para averiguar valores da matriz
    # print(matriz)

print('-=' * 20)
# Loop externo de exibição: extrai cada sublista (linha) de dentro da matriz
for linha in matriz:
    # Loop interno de exibição: extrai cada número individual (valor) de dentro daquela linha
    for valor in linha:
        print(f'[ {valor} ] ', end='')        
    # Quando o loop interno termina (fim da linha da matriz), este print vazio força a quebra de linha na tela
    print()
print('-=' * 20)
for linha in matriz:
    if matriz.index(linha) == 1:
        maior = max(linha)
    for valor in linha:
        if valor % 2 == 0:
            pares.append(valor)
        if linha.index(valor) == 2:
            coluna3.append(valor)
print(f'A soma dos valores pares é {sum(pares)}.')
print(f'A soma dos valores da terceira coluna é {sum(coluna3)}.')
print(f'O maior valor da segunda linha é {maior}.')

'''A resolução do Guanabara ficou bem diferente da minha e muito mais enxuta (23 linhas de código), porque ele não criou novas listas para guardar os valores procurados, somente foi somando os itens que iam se enquadrando no que procurava. Preferi versionar o que eu fiz, porque guardando em listas, as possibilidades de tratamento (min, max, mean, etc) são muito maiores para a minha formação em Ciência de Dados.'''