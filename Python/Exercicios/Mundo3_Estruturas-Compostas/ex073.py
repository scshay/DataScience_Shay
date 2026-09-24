# Dados do Brasileirão acessados em 23/09/2026 (GE Globo)
classificao = ('Flamengo','Palmeiras','Athletico-PR','Fluminense','Bahia','Cruzeiro','Atlético-MG','Santos','Coritiba','Bragantino','São Paulo','Botafogo','Vitória','Corinthians','Mirassol','Vasco','Grêmio','Internacional','Remo','Chapecoense')

print('-='*30)
print(f'Lista de times do Brasileirão: {classificao}.')
print('-='*30)
print(f'Os 5 primeiros são: {classificao[0:5]}.')
print('-='*30)
print(f'Os 4 últimos são: {classificao[-4:]}.')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(classificao)}.')
print('-='*30)
print(f'O Chapecoense está na {classificao.index("Chapecoense") + 1}º posição da tabela.')     # .index("Chapecoense") retorna a posição do time na tupla, começando em 0. Como a tabela começa em 1, somamos +1 para exibir a posição correta. 