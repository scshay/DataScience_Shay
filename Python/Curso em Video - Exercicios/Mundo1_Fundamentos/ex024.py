cidade = input('Em que cidade você nasceu? ').strip().upper()   # Lembrando que strip() remove espaços antes e depois do nome da cidade, caso o usuário digite algum espaço a mais. A função upper() é usado para não termos problemas com a forma que o usuário digitou o nome da cidade

# Resposta abaixo não está errada, mas há mapeei um contra-tempo que também existe na resolução do Guanabarta abaixo: o primeiro nome não ser só SANTO mas conter SANTO, por exemplo, a cidade de SANTOS. 

cidadeSeparado = cidade.split()
print('SANTO' in cidadeSeparado[0])

'''
# Aqui eu estou pegando os 5 primeiros caracteres da string, que é o nome da cidade, e comparando com a palavra SANTO. Se for igual, retorna True, se não, retorna False.
print(cidade[:5] == 'SANTO')   
'''