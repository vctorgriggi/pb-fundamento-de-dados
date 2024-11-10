from tarefa import Tarefa

tarefas = []

def adicionar_tarefa(descricao, prazo=None, urgencia="normal"):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Args:
        descricao (str): A descrição da tarefa.
        prazo (datetime, opcional): O prazo para conclusão da tarefa.
        urgencia (str): Nível de urgência da tarefa (padrão: "normal").

    Exibe uma mensagem de sucesso ao adicionar a tarefa.
    """
    nova_tarefa = Tarefa(descricao, prazo, urgencia)
    tarefas.append(nova_tarefa)
    print(f"Sucesso! Tarefa '{descricao}' adicionada com sucesso.")

def listar_tarefas():
    """
    Lista todas as tarefas atuais. Se não houver tarefas cadastradas, exibe uma mensagem informativa.
    """
    if not tarefas:
        print("Não há tarefas cadastradas.")
        return
    
    for tarefa in tarefas:
        print(tarefa)

def marcar_concluida(tarefa_id):
    """
    Marca uma tarefa como concluída, alterando seu status para "Concluída".

    Args:
        tarefa_id (int): O ID da tarefa a ser marcada como concluída.

    Exibe uma mensagem de sucesso ao marcar a tarefa como concluída.
    """
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            tarefa.marcar_concluida()
            print(f"Tarefa '{tarefa.descricao}' marcada como concluída.")
            return
        
    print("O ID informado não corresponde a nenhuma tarefa.")

def remover_tarefa(tarefa_id):
    """
    Remove uma tarefa da lista com base em seu ID.

    Args:
        tarefa_id (int): O ID da tarefa a ser removida.

    Exibe uma mensagem de confirmação ao remover a tarefa.
    """
    global tarefas
    
    tarefas = [tarefa for tarefa in tarefas if tarefa.id != tarefa_id]
    print(f"Sucesso! Tarefa com ID {tarefa_id} removida.")
