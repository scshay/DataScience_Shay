'''Como o mais conhecido no mercado é o PyGame, não vamos prosseguir oficialmenter com a solução abaixo. Obs:. o código abaixo funcionou em 20/08/2026!
import playsound3
playsound3.playsound('C:\\Users\\DSS\\Documents\\Shayenne\\Python\\Guanabara\\Exercicios\\Mundo1_Fundamentos\\ex21_worry.mp3')'''

import pygame   # Feito o pip install do pygame-ce, pois hoje (20/08/2026) o pygame não funciona mais no Windows 11 (Gerado por IA do VS Code).
pygame.init()
pygame.mixer.music.load('C:\\Users\\DSS\\Documents\\Shayenne\\Python\\Guanabara\\Exercicios\\Mundo1_Fundamentos\\ex21_worry.mp3')
pygame.mixer.music.play()
 # Não funcionou sem esse comando input abaixo mesmo com o pygame.event.wait(), já na resolução do Guanabara não deu o problema, mas pelos comentários deu pra pegar a resolução. 
 # Por que funciona sem o pygame.event.wait()? Porque o input() faz com que o programa espere até que o usuário pressione Enter, então a música tem tempo de tocar. O pygame.event.wait() faz com que o programa espere até que um evento aconteça, mas como não estamos lidando com eventos, não é necessário usar ele aqui.
input()
# pygame.event.wait()
