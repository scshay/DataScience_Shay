import datetime as dt
import emoji 
import time

for c in range(10,0,-1):
    print(f'{c}...')
    time.sleep(1)
print(f'FELIZ ANO NOVO!!! {emoji.emojize(":fireworks:")}')   # As aspas do fireworks também podia ser a simples, mas coloquei essa pra não confundir com a do f-string
print(emoji.emojize(f'PRÓSPERO {dt.date.today().year} :sparkler:'))   # Dá para imprimir desse jeito também
