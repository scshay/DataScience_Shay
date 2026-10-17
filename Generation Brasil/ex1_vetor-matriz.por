programa {
  inclua biblioteca Matematica --> mat

  funcao inicio() {
    inteiro posicao, item, maior, temp, vetor[10]={2,5,1,3,4,9,7,8,10,6}
    
    para(posicao=0; posicao<=9; posicao++) {
      para(item=posicao+1; item<=9; item++){
        se(vetor[posicao] < vetor[item]){
            temp = vetor[posicao] 
            vetor[posicao] = vetor[item]
            vetor[item] = temp
          }
        }
      }
    para(posicao=0; posicao<=9; posicao++){
      escreva(vetor[posicao]," ")
    }
  }
}
