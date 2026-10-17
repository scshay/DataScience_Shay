programa {
  funcao inicio() {
    inteiro posicao, item, soma, media, vetor[10]

    para(item=0;item<=9;item++){
      escreva("Digite o número de posição ",item,": ")
      leia(vetor[item])
    }
    escreva("\nElementos nos ÍNDICES ímpares\n")
    para(posicao=0;posicao<=9;posicao++){
      se(posicao % 2 != 0){
        escreva(vetor[posicao]," ")
      }
    }
    escreva("\nElementos pares\n")
    para(item=0;item<=9;item++){
        se(vetor[item] % 2 == 0){
          escreva(vetor[item]," ")
        }
    }
    escreva("\nSoma\n")
    para(item=0;item<=9;item++){
        se(item==0){
          soma = vetor[item]
        }
        senao{
          soma += vetor[item]
        }
    }
    escreva(soma)   //fora do laço para a fim de imprimir somente a última soma
    media = soma/10
    escreva("\nMédia\n",media)
  }
}
