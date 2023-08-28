class ServicosServices:

    def __init__(self):
        pass

    def listar_servicos(self):
        with open("data/servicos_data.txt", "r") as file:
            servicos = file.read()
            return servicos
        
    def salvar_servico(self, nome, preco, tempo):
        if self.validar_dados(nome, preco, tempo) and not self.servico_existe(nome):
            with open("data/servicos_data.txt", "a") as file:
                file.write(f"nome: {nome}\n".lower())
                file.write(f"custo: {preco}\n".lower())
                file.write(f"tempo: {tempo}\n".lower())
                file.write("=====\n")  # Delimitador entre registros
        if self.servico_existe(nome):
            return True
        else:
            return False
        
    def listar_nomes(self):
        servicos_text = self.listar_servicos()
        servicos = servicos_text.split("=====\n")

        # Lista para armazenar os nomes dos serviços
        nomes_servicos = []

        # Loop para extrair os nomes dos serviços
        for servico in servicos:
            linhas = servico.strip().split("\n")
            if len(linhas) >= 1:
                nome_line = linhas[0]
                if ": " in nome_line:
                    nome = nome_line.split(": ")[1]
                    nomes_servicos.append(nome)
        
        return nomes_servicos
    
    def servico_existe(self, nome):
        lista_de_nomes = self.listar_nomes()
        if nome in lista_de_nomes:
            return True
        else:
            print('e3')
            return False
        
    def validar_dados(self, nome, preco, tempo):
        if not nome or not preco or not tempo:
            print('e1')
            return False
        else:
            return True

    def excluir_servico(self, nome):
        if self.servico_existe(nome):
            with open("data/servicos_data.txt", "r") as file:
                linhas = file.readlines()

            indice_inicio = None
            indice_fim = None
            for i, linha in enumerate(linhas):
                if linha.strip() == f"nome: {nome}":
                    indice_inicio = i
                    break

            if indice_inicio is not None:
                for i in range(indice_inicio, len(linhas)):
                    if linhas[i].strip() == "=====":
                        indice_fim = i
                        break

            if indice_inicio is not None and indice_fim is not None:
                with open("data/servicos_data.txt", "w") as file:
                    for i, linha in enumerate(linhas):
                        if i < indice_inicio or i > indice_fim:
                            file.write(linha)
            
            return True
        
        else:
            return False
        
    def atualizar_servico(self, nome_antigo, nome_novo, preco_novo, tempo_novo):
        if self.servico_existe(nome_antigo):
            with open("data/servicos_data.txt", "r") as file:
                linhas = file.readlines()

            indice_inicio = None
            indice_fim = None

            for i, linha in enumerate(linhas):
                if linha.strip().lower() == f"nome: {nome_antigo}".lower():
                    indice_inicio = i
                    break

            if indice_inicio is not None:
                for i in range(indice_inicio, len(linhas)):
                    if linhas[i].strip() == "=====":
                        indice_fim = i
                        break

            if indice_inicio is not None and indice_fim is not None:
                with open("data/servicos_data.txt", "w") as file:
                    for i, linha in enumerate(linhas):
                        if i < indice_inicio or i > indice_fim:
                            file.write(linha)
                        elif linha.strip().lower().startswith("nome:"):
                            file.write(f"nome: {nome_novo}\n".lower())
                        elif linha.strip().lower().startswith("custo:"):
                            file.write(f"custo: {preco_novo}\n".lower())
                        elif linha.strip().lower().startswith("tempo:"):
                            file.write(f"tempo: {tempo_novo}\n".lower())
                            file.write("=====\n")  # Delimitador entre registros

            return True
        else:
            print('servico n existe')
            return False
