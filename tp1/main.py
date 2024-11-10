from operacoes import adicionar_tarefa, listar_tarefas, marcar_concluida, remover_tarefa
from utils import exibir_menu

def main():
    """
    Função principal que controla o sistema de gerenciamento de tarefas.
    
    O programa exibe um menu interativo que permite ao usuário:
    1. Adicionar uma nova tarefa com descrição, prazo e urgência.
    2. Listar todas as tarefas cadastradas.
    3. Marcar uma tarefa específica como concluída usando seu ID.
    4. Remover uma tarefa da lista através do ID.
    5. Sair do programa.

    Após cada operação, retorna ao menu até que o usuário escolha sair.
    """
    while True:
        exibir_menu()
        opcao = input("Caro usuário, por favor, escolha uma opção: ")
        
        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            prazo = input("Prazo (opcional): ")
            urgencia = input("Urgência (normal, alta, baixa): ")
            adicionar_tarefa(descricao, prazo, urgencia)
        
        elif opcao == "2":
            listar_tarefas()
        
        elif opcao == "3":
            try:
                tarefa_id = int(input("Informe o ID da tarefa a marcar como concluída: "))
                marcar_concluida(tarefa_id)

            except ValueError:
                print("Oopss! Por favor, insira um ID válido.")
        
        elif opcao == "4":
            try:
                tarefa_id = int(input("Informe o ID da tarefa a remover: "))
                remover_tarefa(tarefa_id)

            except ValueError:
                print("Oopss! Por favor, insira um ID válido.")
        
        elif opcao == "5":
            print("Obrigado por usar o sistema. Até a próxima!")
            break

        else:
            print("Oopss! Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
