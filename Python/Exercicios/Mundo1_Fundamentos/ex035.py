print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Essa foi a minha solução tentando com IF/ELSE
'''
maior = r1
if r2 > r1 and r2 > r3:
   maior = r2
if r3 > r1 and r3 > r2:
   maior = r3
'''

# Segue minha versão mais limpa com max()
maior = max(r1,r2,r3)

resultado = (r1 + r2 + r3) - maior   # Tem como usar o sum() mas para passar as variáveis precisa ser dentro de uma lista, como não aprendi formalmente sobre, preferi não colocar; ficaria assim: resultado = sum([r11,r2,r3])-maior

if resultado >  maior:
# Resolução do Guanabara replicou a fórmula de todas as combinações possíveis e fica muito mais limpo porque não tem outras contas é só esse IF/ELSE mesmo:
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print(f'Os segmentos acima \033[4;34mPODEM FORMAR\033[m um triângulo!')   # azul sublinhado: \033[4;34m e para ele não correr pra linha toda \033[m
else:
   print(f'Os segmentos acima \033[4;30;41mNÃO PODEM FORMAR\033[m um triângulo.')   # branco sublinhado com fundo vermelho: \033[4;30;41m e para ele não correr pra linha toda \033[m