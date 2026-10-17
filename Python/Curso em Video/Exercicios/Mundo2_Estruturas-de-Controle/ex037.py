numero = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha uma das bases para conversão! \n[ 1 ] Converter para BINÁRIO \n[ 2 ]Converter para OCTAL \n[ 3 ] Converter para HEXADECIMAL \nSua opção: '))

if opcao == 1:
    # bin = format(numero,'b') ---> essa foi a função que achei na documentação do Python, como ela é mais genérica, o comportamento dela depende exclusivamente do 2º argumento que for posto
    print(f'{opcao} convertida para BINÁRIO é igual a "{bin(numero)}".')   # Na função "bin(numero)", o resultado sai com o prefixo "0b", por isso, é necessário o fatiamento acima
elif opcao == 2:
    # oct = format(numero,'o')
    print(f'{opcao} convertida para OCTAL é igual a "{oct(numero)[2:]}".')   # Na função "oct(numero)", o resultado sai com o prefixo "0o", por isso, é necessário o fatiamento acima
else: 
    # hex = format(numero,'x')   
    print(f'{numero} convertida para HEXADECIMAL é igual a "{hex(numero)[2:]}".')   # Na função "hex(numero)", o resultado sai com o prefixo "0x", por isso, é necessário o fatiamento abaixo
