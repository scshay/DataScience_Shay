valores = []

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.insert(0, valor)
        print('O primeiro... adicionado à lista ;)')
    else:
        # LOOP 2 (O Detetive): Varre os itens existentes para descobrir a posição correta
        for posicao, item in enumerate(valores):
            # LÓGICA DO MEIO: Se o novo valor for menor que o item atual da lista, ele assume o índice desse item (empurrando o resto para a direita)
            if valor < item:
                valores.insert(posicao, valor)
                print(f'Adicionado na lista na posição {posicao}.')
                print(valores)
                break # Interrompe este loop interno e IMPEDE a execução do 'else' abaixo
                
        else:
            # ESTRUTURA FOR/ELSE: Este bloco SÓ roda se o LOOP 2 terminar de ler a lista inteira sem ter encontrado nenhum 'break' (ou seja, o valor é o maior de todos)
            valores.insert(len(valores), valor)
            print(f'Adicionado ao final da lista na posição {posicao + 1}!')
            print(valores)
print('-=' * 20)
print(f'Os valores digitados em ordem foram {valores}')
