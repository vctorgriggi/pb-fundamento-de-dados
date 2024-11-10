from datetime import datetime

class Tarefa:
    """
    Representa uma tarefa com descrição, data de criação, status, prazo e urgência.

    Atributos:
        descricao (str): Descrição textual da tarefa.
        data_criacao (datetime): Data e hora de criação da tarefa.
        status (str): Estado atual da tarefa, "Pendente" por padrão.
        prazo (datetime, opcional): Prazo para conclusão, se houver.
        urgencia (str): Nível de urgência (padrão: "normal").

    Métodos:
        marcar_concluida(): Marca a tarefa como "Concluída".
        __str__(): Retorna uma string com os detalhes da tarefa.
    """
    _id_contador = 1

    def __init__(self, descricao, prazo=None, urgencia="normal"):
        """
        Inicializa uma nova tarefa com uma descrição, prazo opcional e nível de urgência.

        Args:
            descricao (str): Descrição da tarefa.
            prazo (datetime, opcional): Data limite para a tarefa ser concluída.
            urgencia (str): Nível de urgência da tarefa (padrão: "normal").
        """
        self.id = Tarefa._id_contador
        Tarefa._id_contador += 1

        self.descricao = descricao
        self.data_criacao = datetime.now()
        self.status = "Pendente"
        self.prazo = prazo
        self.urgencia = urgencia

    def marcar_concluida(self):
        """
        Marca a tarefa como concluída, alterando seu status para "Concluída".
        """
        self.status = "Concluída"

    def __str__(self):
        """
        Retorna uma string formatada com os detalhes da tarefa.

        Returns:
            str: Representação textual da tarefa incluindo ID, descrição, status, prazo e urgência.
        """
        return f"ID: {self.id} - Descrição: {self.descricao} - Status: {self.status} - Prazo: {self.prazo} - Urgência: {self.urgencia}"
