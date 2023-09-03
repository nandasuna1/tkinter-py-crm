class AgendamentosServices:
    def __init__(self):
        pass

    def listar_agendamentos(self):
        with open("data/agendamento_data.txt", "r") as file:
            agendamentos = file.read()
            return agendamentos
        
    def salvar_agendamento(self, servico ,cliente_nome, cliente_tel, data, hora):
        ids = self.listar_ids()
        id = len(ids) 
        if self.agendamento_disponivel(data, hora):
            print('Entrei!!!')
            with open("data/agendamento_data.txt", "a") as file:
                file.write(f'id: {id}\n'.lower())
                file.write(f"data: {data}\n".lower())
                file.write(f"hora: {hora}\n".lower())
                file.write(f"servico: {servico}\n".lower())
                file.write(f"cliente: {cliente_nome}\n".lower())
                file.write(f"telefone: {cliente_tel}\n".lower())

                file.write("=====\n")  # Delimitador entre registros
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
        with open("data/agendamento_data.txt", "r") as file:
            linhas = file.read().split("=====\n")

        for linha in linhas:
            print(linha, id)
            if linha.strip():  # Ignora linhas em branco
                if f"id: {id}" in linha:
                    return True  # ID encontrado no arquivo

        return False  # ID não encontrado no arquivo
        
    def agendamento_disponivel(self, data, hora):
        with open("data/agendamento_data.txt", "r") as file:
            linhas = file.read().split("=====\n")

        for linha in linhas:
            if linha.strip():  # Ignora linhas em branco
                agendamento = {}
                for atributo in linha.strip().split("\n"):
                    chave, valor = atributo.split(": ", 1)
                    agendamento[chave] = valor

                if agendamento["data"] == data and agendamento["hora"] == hora:
                    print(agendamento["data"], data, agendamento["hora"], hora)
                    print('ja existe')
                    return False  # Agendamento já existe nessa data e hora
        
        return True  # Agendamento disponível
        
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
                with open("data/agendamento_data.txt", "w") as file:
                    for i, linha in enumerate(linhas):
                        if i < indice_inicio or i > indice_fim:
                            file.write(linha)
            
            return True
        
        else:
            return False
        
    def atualizar_agendamento(self, id, cliente, telefone, data, hora, servico):
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
                        elif linha.strip().lower().startswith("id:"):
                            file.write(f"id: {id}\n".lower())
                        elif linha.strip().lower().startswith("data:"):
                            file.write(f"data: {data}\n".lower())
                        elif linha.strip().lower().startswith("hora:"):
                            file.write(f"hora: {hora}\n".lower())
                        elif linha.strip().lower().startswith("servico:"):
                            file.write(f"servico: {servico}\n".lower())
                        elif linha.strip().lower().startswith("cliente:"):
                            file.write(f"cliente: {cliente}\n".lower())
                        elif linha.strip().lower().startswith("telefone:"):
                            file.write(f"telefone: {telefone}\n".lower())
                            file.write("=====\n")  # Delimitador entre registros

            return True
        else:
            print('agendamento n existe')
            return False
