sal = float(input(f'Qual é o salário do funcionário? RS$'))

if sal <= 1250:
    novoSal = sal + ((15*sal)/100)   # Daria também para fazer multiplicando por 1,15
else:
    novoSal = sal + ((10*sal)/100)   # Daria também para fazer multiplicando por 1,10

print(f'Quem ganhava RS${sal:.2f} passa a ganhar RS${novoSal:.2f} agora.')
