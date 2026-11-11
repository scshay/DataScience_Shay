matriz = []

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
        print(f'[{valor:^5}] ', end='')        
    # Quando o loop interno termina (fim da linha da matriz), este print vazio força a quebra de linha na tela
    print()

'''A resolução do Guanabara ficou bem diferente da minha e muito mais enxuta (9 linhas de código), porém ele iniciou a matriz com todos os valores preenchidos, enquanto que na minha versão a matriz é criada dinamicamente precisando modificar somente o range para outros formatos para além do 3x3 que fiz.'''