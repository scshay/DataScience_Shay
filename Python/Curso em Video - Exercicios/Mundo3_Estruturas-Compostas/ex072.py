numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

posicao = int(input('Digite um número entre 0 e 20: '))
while posicao < 0 or posicao > 20:
    posicao = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[posicao]}.')
