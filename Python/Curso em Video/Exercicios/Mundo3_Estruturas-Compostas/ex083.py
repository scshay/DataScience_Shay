while True:     #Deixei assim para conseguir enviar várias expressões, se quiser parar só digitar Ctrl+C no terminal 
    parenteses = 0
    expressao = input('Digite a expressão: ')
    if '(' in expressao and ')' in expressao:
        for posicao, item in enumerate(expressao):
                if item == '(':
                    parenteses += 1
                elif item == ')':
                    parenteses -= 1
        print(parenteses)
        if parenteses != 0:
            print('Sua expressão até contém parentêses, mas não abre e fecha todos... veredito: errada!')
        else:
            print('Sua expressão está correta ;)')
    else:
        print('A expressão não contém parênteses OU não contém o par de parênteses... veredito: errada!')
