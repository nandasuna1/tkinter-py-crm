from utils.validators import validar_email, validar_senha, validar_cpf

class CadastroService:
    def __init__(self):
        self.dados = self.formatar_dados(nome_arquivo="data/users_data.txt")

    def salvar_cadastro(self, nome, email, senha, cpf):
        if not self.usuario_ja_cadastrado(cpf) and self.validar_dados(nome, email, senha, cpf):
            with open("data/users_data.txt", "a") as file:
                file.write(f"nome: {nome}\n")
                file.write(f"email: {email}\n")
                file.write(f"CPF: {cpf}\n")
                file.write(f"senha: {senha}\n")
                file.write("=====\n")  # Delimitador entre registros
            return True
        else:
            return False

    def usuario_ja_cadastrado(self, cpf):
        for data in self.dados:
            if data.get("cpf") == cpf:
                return True
        return False

    def validar_dados(self, nome, email, senha, cpf):
        if not nome or not email or not senha or not cpf:
            return False

        if not validar_email(email) or not validar_senha(senha) or not validar_cpf(cpf):
            return False

        return True

    def formatar_dados(self, nome_arquivo, delimiter="=====\n"):
        dados = []

        with open(nome_arquivo, "r") as file:
            sections = file.read().split(delimiter)
            for section in sections:
                if section.strip():
                    section_lines = section.strip().split("\n")
                    data_dict = {}
                    for line in section_lines:
                        if ": " in line:
                            key, value = line.split(": ", 1)
                            data_dict[key] = value
                    dados.append(data_dict)
        
        return dados
    
    def login(self, cpf, senha):
        data = self.formatar_dados("data/users_data.txt")       
        for data in self.dados:
            if data.get("cpf") == cpf and data.get("senha") == senha:
                nome = data.get("nome")
                email = data.get("email")
                with open("data/current_user.txt", "a") as file:
                    file.write(f"nome: {nome}\n")
                    file.write(f"email: {email}\n")
                    file.write(f"cpf: {cpf}\n")
                    file.write(f"senha: {senha}\n")
                return True
        return False
    
    def current_user_info(self):        
        with open("data/current_user.txt", "r") as file:
            lines = file.readlines()

        user_info = {}
        for line in lines:
            key, value = line.strip().split(": ")
            user_info[key] = value

        return user_info
    
    def logout(self):
        # Apagar os dados antigos do arquivo
        open("data/current_user.txt", "w").close()

    def deletar_perfil(self):
        user_info = self.current_user_info()
        cpf_usuario_atual = user_info.get("CPF")

        with open("data/users_data.txt", "r") as file:
            linhas = file.readlines()

        indice_inicio = None
        indice_fim = None
        for i, linha in enumerate(linhas):
            if linha.strip() == f"cpf: {cpf_usuario_atual}":
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
        
        self.dados = self.formatar_dados(nome_arquivo="data/users_data.txt")
        return True

    def atualizar_perfil(self, cpf, nome_novo, email_novo, senha_nova):
        if self.usuario_ja_cadastrado(cpf):
            print(nome_novo, email_novo, senha_nova)

            with open("data/users_data.txt", "r") as file:
                linhas = file.readlines()

            indice_inicio = None
            indice_fim = None

            for i, linha in enumerate(linhas):
                if linha.strip().lower() == f"cpf: {cpf}".lower():
                    indice_inicio = i
                    break

            if indice_inicio is not None:
                for i in range(indice_inicio, len(linhas)):
                    if linhas[i].strip() == "=====":
                        indice_fim = i
                        break

            if indice_inicio is not None and indice_fim is not None:
                with open("data/users_data.txt", "w") as file:
                    for i, linha in enumerate(linhas):
                        print(linha)  # Debug
                        print(f"Comparando linha: {linha.strip().lower()} com 'nome:'")  # Debug
                        if i < indice_inicio or i > indice_fim:
                            file.write(linha)
                        elif linha.strip().lower().startswith("nome:"):
                            file.write(f"nome: {nome_novo}\n".lower())
                        elif linha.strip().lower().startswith("email:"):
                            file.write(f"email: {email_novo}\n".lower())
                        elif linha.strip().lower().startswith("cpf:"):
                            file.write(f"cpf: {cpf}\n".lower())
                        elif linha.strip().lower().startswith("senha:"):
                            file.write(f"senha: {senha_nova}\n".lower())
                            file.write("=====\n")  # Delimitador entre registros

            self.atualizar_current_user(cpf, nome=nome_novo, email=email_novo, senha=senha_nova)
            return True
        else:
            return False

    def atualizar_current_user(self, cpf, nome, email, senha):
        with open("data/current_user.txt", "w") as file:
            file.write(f"nome: {nome}\n")
            file.write(f"email: {email}\n")
            file.write(f"cpf: {cpf}\n")
            file.write(f"senha: {senha}\n")

