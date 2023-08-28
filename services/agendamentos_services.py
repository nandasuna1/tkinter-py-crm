class AgendamentosServices:
    def __init__(self):
        pass

    def listar_agendamentos(self):
        with open("data/agendamento_data.txt", "r") as file:
            agendamentos = file.read()
            return agendamentos
        
    ## adicionar funcao para pegar ultimo id
    def salvar_agendamento(self, id, nome, data, hora, cliente, telefone):
        if not self.agendamento_existe(id):
            with open("data/agendamentos_data.txt", "a") as file:
                file.write(f"nome: {nome}\n".lower())
                file.write(f"data: {data}\n".lower())
                file.write(f"hora: {hora}\n".lower())
                file.write(f"cliente: {cliente}\n".lower())
                file.write(f"telefone: {telefone}\n".lower())

                file.write("=====\n")  # Delimitador entre registros
        if self.agendamento_existe(nome):
            return True
        else:
            return False
        
    def listar_ids(self):
        agendamentos_text = self.listar_agendamentos()
        agendamentos = agendamentos_text.split("=====\n")

        # Lista para armazenar os nomes dos serviços
        nomes_agendamentos = []

        # Loop para extrair os nomes dos serviços
        for agendamento in agendamentos:
            linhas = agendamento.strip().split("\n")
            if len(linhas) >= 1:
                nome_line = linhas[0]
                if ": " in nome_line:
                    nome = nome_line.split(": ")[1]
                    nomes_agendamentos.append(nome)
        
        return nomes_agendamentos
    
    def agendamento_existe(self, id):
        lista_ids = self.listar_ids()
        if id in lista_ids:
            return True
        else:
            return False
        
    def validar_dados(self, nome, preco, tempo):
        if not nome or not preco or not tempo:
            return False
        else:
            return True

    def excluir_agendamento(self, id):
        if self.agendamento_existe(id):
            with open("data/agendamento_data.txt", "r") as file:
                linhas = file.readlines()

            indice_inicio = None
            indice_fim = None
            for i, linha in enumerate(linhas):
                if linha.strip() == f"id: {id}":
                    indice_inicio = i
                    break

            if indice_inicio is not None:
                for i in range(indice_inicio, len(linhas)):
                    if linhas[i].strip() == "=====":
                        indice_fim = i
                        break

            if indice_inicio is not None and indice_fim is not None:
                with open("data/agendamentos_data.txt", "w") as file:
                    for i, linha in enumerate(linhas):
                        if i < indice_inicio or i > indice_fim:
                            file.write(linha)
            
            return True
        
        else:
            return False
        
    def atualizar_agendamento(self, id, servico, data, hora):
        if self.agendamento_existe(id):
            with open("data/agendamento_data.txt", "r") as file:
                linhas = file.readlines()

            indice_inicio = None
            indice_fim = None

            for i, linha in enumerate(linhas):
                if linha.strip().lower() == f"id: {id}".lower():
                    indice_inicio = i
                    break

            if indice_inicio is not None:
                for i in range(indice_inicio, len(linhas)):
                    if linhas[i].strip() == "=====":
                        indice_fim = i
                        break

            if indice_inicio is not None and indice_fim is not None:
                with open("data/agendamento_data.txt", "w") as file:
                    for i, linha in enumerate(linhas):
                        if i < indice_inicio or i > indice_fim:
                            file.write(linha)
                        elif linha.strip().lower().startswith("servico:"):
                            file.write(f"servico: {servico}\n".lower())
                        elif linha.strip().lower().startswith("data:"):
                            file.write(f"data: {data}\n".lower())
                        elif linha.strip().lower().startswith("hora:"):
                            file.write(f"hora: {hora}\n".lower())
                            file.write("=====\n")  # Delimitador entre registros

            return True
        else:
            print('agendamento n existe')
            return False
