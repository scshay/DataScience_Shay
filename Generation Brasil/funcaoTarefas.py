from cores import *

tarefas = []
 
def menu():
  print("\n" + FRENTE_AMARELO + "___MENU___" + RESET)
  print("1 - Adicionar Tarefa")
  print("2 - Listar Tarefas")
  print("3 - Remover Tarefa")
  print("4 - Sair")

def adicionarTarefa():
    tarefa = input('Digite o nome da tarefa: ')
    tarefas.append(tarefa)
    print('Tarefa adicionada!')

def listarTarefas():
    if len(tarefas)==0:
        print('Nenhuma tarefa cadastrada.')
    else:
        for numero, tarefa in enumerate(tarefas, start=1):
            print(f'{numero} - {tarefa}')

def removerTarefa():
    listarTarefas()
    if len(tarefas)>0:
        numero = int(input('Digite o número da tarefa: '))
        if 1<=numero<=len(tarefas):
            tarefas.pop(numero-1)
            print('Tarefa removida!')
        else:
            print('Número inválido.')

opcao=''

while opcao!='4':
    menu()
    opcao=input('Escolha uma opção: ')
    if opcao=='1':
        adicionarTarefa()
    elif opcao=='2':
        listarTarefas()
    elif opcao=='3':
        removerTarefa()
    elif opcao=='4':
        print('Até logo ;)')
    else: 
        print('Opção inválida...')

menu()