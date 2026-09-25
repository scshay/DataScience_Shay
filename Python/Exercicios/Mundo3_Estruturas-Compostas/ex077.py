palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for item in palavras:   #range(0,len(palavras)):  #Utilizei esse formato aqui, mas se provou desnecessário durante a resolução
    print(f'\nNa palavra {item.upper()} temos: ', end='')
    for letra in item:   #palavras[item]: #Como acima chamei a tupla direto, não preciso citar a tupla e o item, mas sim somente item porque criei uma 'variável temporária' no for acima
        if letra.lower() in 'aeiou':   #Adicionei o .lower() pois se tivesse alguma vogal maiúscula ('AEIOU'), não seria encontrado
            print(f'{letra} ', end='')
