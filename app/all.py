import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import tkinter.messagebox
import tkinter.simpledialog
from services.cadastro_service import CadastroService
from services.servicos_services import ServicosServices
from services.agendamentos_services import AgendamentosServices


class LoginScreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.login_frame = tk.Frame(self.root)
        self.login_frame.configure(width=400, height=600)
        self.login_frame.pack()

        self.app_name_label = tk.Label(self.login_frame, font=('Bold', 30), fg='#fff', bd=0, bg='#158aff',text="PetService")
        # self.app_name_label.pack()
        self.app_name_label.place(x=10, y=100)


        self.cpf_label = tk.Label(self.login_frame, font=('Bold', 15), fg='#fff', bd=0, bg='#158aff',text="CPF:")
        # self.cpf_label.pack()
        self.cpf_label.place(x=10, y=200)


        self.cpf_entry = tk.Entry(self.login_frame)
        # self.cpf_entry.pack()
        self.cpf_entry.place(x=100, y=200, width=150, height=20)


        self.senha_label = tk.Label(self.login_frame, text="Senha:", font=('Bold', 15), fg='#fff', bd=0, bg='#158aff' )
        # self.senha_label.pack()
        self.senha_label.place(x=10, y=250)


        self.senha_entry = tk.Entry(self.login_frame, show="*")
        # self.senha_entry.pack()
        self.senha_entry.place(x=100, y=250, width=150, height=20)


        self.login_button = tk.Button(self.login_frame, text="Login", font=('Bold', 15), fg='#fff', bd=0, bg='#158aff', command=self.efetuar_login)
        # self.login_button.pack()
        self.login_button.place(x=10, y=400)

        

        self.cadastrar_button = tk.Button(self.login_frame, text="Cadastrar", font=('Bold', 15), fg='#fff', bd=0, bg='#158aff', command=self.abrir_tela_cadastro)
        # self.cadastrar_button.pack()
        self.cadastrar_button.place(x=100, y=400)

        self.cadastro_service = CadastroService()

    def efetuar_login(self):
        senha = self.senha_entry.get()
        cpf = self.cpf_entry.get()
        if not cpf or not senha:
            tkinter.messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
        else:
            verificado = self.cadastro_service.login(cpf, senha)
            if verificado:
                tkinter.messagebox.showinfo("Sucesso", "Bem Vindo!")
                self.login_frame.destroy()
                HomeScreen(self.root, self.app)
            else:
                tkinter.messagebox.showerror("Erro", "Usuario não encontrado.")


    def abrir_tela_cadastro(self):
        self.login_frame.destroy()
        CadastroScreen(self.root, self.app)

class CadastroScreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app


        self.cadastro_frame = tk.Frame(self.root)
        self.cadastro_frame.configure(width=400, height=600)
        self.cadastro_frame.pack()

        self.app_name_label = tk.Label(self.cadastro_frame, font=('Bold', 30), fg='#fff', bd=0, bg='#158aff',text="PetService")
        # self.app_name_label.pack()
        self.app_name_label.place(x=10, y=100)


        self.nome_label = tk.Label(self.cadastro_frame, font=('Bold', 15), fg='#fff', bd=0, bg='#158aff', text="Nome:")
        self.nome_label.place(x=10, y=200)

        # self.nome_label.pack()
        self.nome_entry = tk.Entry(self.cadastro_frame)
        self.nome_entry.place(x=100, y=200)

        # self.nome_entry.pack()

        self.cpf_label = tk.Label(self.cadastro_frame, font=('Bold', 15), fg='#fff', bd=0, bg='#158aff', text="CPF:")
        self.cpf_label.place(x=10, y=250)
        # self.cpf_label.pack()
        
        self.cpf_entry = tk.Entry(self.cadastro_frame)
        self.cpf_entry.place(x=100, y=250)
        # self.cpf_entry.pack()

        self.senha_label = tk.Label(self.cadastro_frame, font=('Bold', 15), fg='#fff', bd=0, bg='#158aff', text="Senha:")
        self.senha_label.place(x=10, y=300)
        # self.senha_label.pack()
        
        self.senha_entry = tk.Entry(self.cadastro_frame)
        self.senha_entry.place(x=100, y=300)
        # self.senha_entry.pack()

        self.email_label = tk.Label(self.cadastro_frame, font=('Bold', 15), fg='#fff', bd=0, bg='#158aff', text="Email:")
        self.email_label.place(x=10, y=400)
        # self.email_label.pack()
        
        self.email_entry = tk.Entry(self.cadastro_frame)
        self.email_entry.place(x=100, y=400)
        # self.email_entry.pack()

        self.confirmar_cadastro_button = tk.Button(self.cadastro_frame, font=('Bold', 15), fg='#fff', bd=0, bg='#158aff', text="Confirmar Cadastro", command=self.confirmar_cadastro)
        self.confirmar_cadastro_button.place(x=10, y=450)
        # self.confirmar_cadastro_button.pack()

        self.voltar_para_login_button = tk.Button(self.cadastro_frame, font=('Bold', 15), fg='#fff', bd=0, bg='#158aff', text="<- Voltar", command=self.voltar_para_login)
        self.voltar_para_login_button.place(x=200, y=450)
        # self.voltar_para_login_button.pack()
            
    def voltar_para_login(self):
        self.cadastro_frame.destroy()
        LoginScreen(self.root, self.app)

    def confirmar_cadastro(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        cpf = self.cpf_entry.get()
        cadastro_service = CadastroService()

        if cadastro_service.salvar_cadastro(nome, email, senha, cpf):
            tkinter.messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.cadastro_frame.destroy()
            LoginScreen(self.root, self.app)
        else:
            tkinter.messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")

class HomeScreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        self.options_frame = tk.Frame(root, bg='#c3c3c3')
        self.options_frame.pack(side=tk.LEFT)
        self.options_frame.propagate(False)
        self.options_frame.configure(width=200, height=400)
        
        self.servicos_services = ServicosServices()
        self.servicos_perfil = CadastroService()
        self.servicos_agendamento = AgendamentosServices()


        def servico_page():
            servicos_text = self.servicos_services.listar_servicos()  # Use a função para listar os serviços
            
            servicos_frame = tk.Frame(self.main_frame)  # Crie um frame para os cards de serviços
            servicos_frame.pack(fill=tk.BOTH, expand=True)

            self.servico_cards = []  # Inicialize a lista de cards de serviço

            canvas = tk.Canvas(servicos_frame)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(servicos_frame, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            canvas.config(yscrollcommand=scrollbar.set)

            self.frame_inside_canvas = tk.Frame(canvas)
            canvas.create_window((0, 0), window=self.frame_inside_canvas, anchor="nw")

            criar_servico_btn = tk.Button(self.frame_inside_canvas, text="Criar Serviço", font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=self.abrir_popup_criar_servico)
            criar_servico_btn.pack(side=tk.TOP, pady=10)


            def on_frame_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            self.frame_inside_canvas.bind("<Configure>", on_frame_configure)

            for servico in servicos_text.split("=====\n"):
                if servico.strip():
                    servico_frame = self.criar_card_servico(servico, self.frame_inside_canvas)
                    servico_frame.pack(fill=tk.BOTH, padx=10, pady=10)
                    self.servico_cards.append(servico_frame)  # Adicione o card à lista


            canvas.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        def perfil_page():
            perfil_info = self.servicos_perfil.current_user_info() 
            
            perfil_frame = tk.Frame(self.main_frame) 
            perfil_frame.pack(fill=tk.BOTH, expand=True)

            nome = perfil_info['nome']
            email = perfil_info['email']
            cpf = perfil_info['cpf']
            senha = perfil_info['senha']

            self.nome_label = tk.Label(perfil_frame, font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Nome: {nome}")
            # self.nome_label.pack()

            self.email_label = tk.Label(perfil_frame, font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Email: {email}")
            # self.email_label.pack()

            self.cpf_label = tk.Label(perfil_frame, font=(12), fg='#fff', bd=0, bg='#158aff', text=f"CPF: {cpf}")
            # self.cpf_label.pack()

            self.senha_label = tk.Label(perfil_frame, font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Senha: {senha}")
            # self.senha_label.pack()

            self.editar_button = tk.Button(perfil_frame, font=(12), fg='#fff', bd=0, bg='#158aff', text="Editar", command=lambda:self.abrir_popup_editar_perfil(cpf, nome, email, senha))
            # self.editar_button.pack()

            self.deletar_button = tk.Button(perfil_frame, font=(12), fg='#fff', bd=0, bg='#158aff', text="Deletar", command=self.deletar_perfil)
            # self.deletar_button.pack()

            self.logout_button = tk.Button(perfil_frame, font=(12), fg='#fff', bd=0, bg='#158aff', text="Logout", command=self.logout)
            # self.logout_button.pack()

                    # Organize os elementos usando o grid manager
            self.nome_label.grid(row=0, column=0, padx=5, pady=5)
            self.email_label.grid(row=1, column=0, padx=5, pady=5)
            self.cpf_label.grid(row=2, column=0, padx=5, pady=5)
            self.editar_button.grid(row=3, column=0, padx=5, pady=5)
            self.deletar_button.grid(row=3, column=1, padx=5, pady=5)
            self.logout_button.grid(row=3, column=2, padx=5, pady=5)


        def agendamentos_page():
            agendamentos_text = self.servicos_agendamento.listar_agendamentos()  # Use a função para listar os serviços
            
            agendamentos_frame = tk.Frame(self.main_frame)  # Crie um frame para os cards de serviços
            agendamentos_frame.pack(fill=tk.BOTH, expand=True)

            self.agendamento_cards = []  # Inicialize a lista de cards de serviço

            canvas = tk.Canvas(agendamentos_frame)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(agendamentos_frame, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            canvas.config(yscrollcommand=scrollbar.set)

            self.frame_inside_canvas = tk.Frame(canvas)
            canvas.create_window((0, 0), window=self.frame_inside_canvas, anchor="nw")

            criar_agendamento_btn = tk.Button(self.frame_inside_canvas, text="Criar Agendamento", font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=self.abrir_popup_criar_agendamento)
            criar_agendamento_btn.pack(side=tk.TOP, pady=10)


            def on_frame_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            self.frame_inside_canvas.bind("<Configure>", on_frame_configure)

            for agendamento in agendamentos_text.split("=====\n"):
                if agendamento.strip():
                    agendamento_frame = self.criar_card_agendamento(agendamento, self.frame_inside_canvas)
                    agendamento_frame.pack(fill=tk.BOTH, padx=10, pady=10)
                    self.agendamento_cards.append(agendamento_frame)  # Adicione o card à lista


            canvas.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        def clear_frames():
            for frame in self.main_frame.winfo_children():
                frame.destroy()

        def hide_indicators():
            home_indicator.config(bg='#c3c3c3')
            menu_indicator.config(bg='#c3c3c3')
            about_indicator.config(bg='#c3c3c3')

        def indicate(lb, page):
            hide_indicators()
            lb.config(bg='#158aff')
            clear_frames()
            page()
        
        home_btn = tk.Button(self.options_frame, text="Agendamentos", font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicator, agendamentos_page))
        home_btn.place(x=10, y=50)
        home_indicator = tk.Label(self.options_frame, text='', bg='#c3c3c3')
        home_indicator.place(x=3, y=50, width=5, height=40)

        menu_btn = tk.Button(self.options_frame, text="Serviços", font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(menu_indicator, servico_page))
        menu_btn.place(x=10, y=100)
        menu_indicator = tk.Label(self.options_frame, text='', bg='#c3c3c3')
        menu_indicator.place(x=3, y=100, width=5, height=40)
        
        about_btn = tk.Button(self.options_frame, text="Perfil", font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(about_indicator, perfil_page))
        about_btn.place(x=10, y=200)
        about_indicator = tk.Label(self.options_frame, text='', bg='#c3c3c3')
        about_indicator.place(x=3, y=200, width=5, height=40)
        

        self.main_frame = tk.Frame(root, highlightbackground='black', highlightthickness="2")
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.propagate(False)
        self.main_frame.configure(height=400, width=500)
    
    # Funções de Servicos
    def abrir_popup_criar_servico(self):
        popup = tk.Toplevel(self.root)
        popup.title("Criar Novo Serviço")

        nome_label = tk.Label(popup, text="Nome do Serviço:")
        nome_label.pack()
        nome_entry = tk.Entry(popup)
        nome_entry.pack()

        preco_label = tk.Label(popup, text="Custo:")
        preco_label.pack()
        preco_entry = tk.Entry(popup)
        preco_entry.pack()

        tempo_label = tk.Label(popup, text="Tempo:")
        tempo_label.pack()
        tempo_entry = tk.Entry(popup)
        tempo_entry.pack()

        confirmar_btn = tk.Button(popup, text="Confirmar", command=lambda: HomeScreen.adicionar_servico(self, nome_entry.get(), preco_entry.get(), tempo_entry.get(), popup))
        confirmar_btn.pack()

    def adicionar_servico(self, nomeServico, preco, tempo, popup):
        adicionado = self.servicos_services.salvar_servico(nome=nomeServico, preco=preco, tempo=tempo)
        if adicionado:
            tkinter.messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            popup.destroy()
            self.update_servicos_cards()  
        else:
            tkinter.messagebox.showerror("Erro", "Não foi possivel cadastrar esse serviço, verifique os dados.")

    def criar_card_servico(self, servico_text, servicos_frame):
        servico_frame = tk.Frame(servicos_frame, borderwidth=0, relief="solid", bg='#158aff')
        
        # Extrair informações do texto do serviço
        lines = servico_text.split("\n")
        nome = lines[0].split(": ")[1]
        preco = lines[1].split(": ")[1]
        tempo = lines[2].split(": ")[1]

        nome_label = tk.Label(servico_frame,  font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Nome: {nome}") 
        preco_label = tk.Label(servico_frame,  font=(12), fg='#fff', bd=0, bg='#158aff',  text=f"Preço: R${preco}")
        tempo_label = tk.Label(servico_frame,  font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Tempo: {tempo}")

        editar_btn = tk.Button(servico_frame, text="Editar", font=(12), fg='#158aff', bd=0, bg='#fff', command=lambda: self.abrir_popup_editar_servico(nome, preco, tempo))
        excluir_btn = tk.Button(servico_frame, text="Excluir", font=(12), fg='#158aff', bd=0, bg='#fff', command=lambda: self.excluir_servico(nome))

        # Organize os elementos usando o grid manager
        nome_label.grid(row=0, column=0, padx=5, pady=5)
        preco_label.grid(row=1, column=0, padx=5, pady=5)
        tempo_label.grid(row=2, column=0, padx=5, pady=5)
        editar_btn.grid(row=3, column=4, padx=5, pady=5)
        excluir_btn.grid(row=3, column=5, padx=5, pady=5)

        self.servico_cards.append(servico_frame)  # Adicione o card à lista
        return servico_frame
    
    def abrir_popup_editar_servico(self, nome, preco, tempo):
        popup = tk.Toplevel(self.root)
        popup.title("Editar Serviço")

        nome_label = tk.Label(popup, text="Nome:")
        nome_label.pack()
        nome_entry = tk.Entry(popup)
        nome_entry.insert(0, nome)
        nome_entry.pack()

        preco_label = tk.Label(popup, text="Preço:")
        preco_label.pack()
        preco_entry = tk.Entry(popup)
        preco_entry.insert(0, preco)
        preco_entry.pack()

        tempo_label = tk.Label(popup, text="Tempo:")
        tempo_label.pack()
        tempo_entry = tk.Entry(popup)
        tempo_entry.insert(0, tempo)
        tempo_entry.pack()

        confirmar_btn = tk.Button(popup, text="Confirmar", command=lambda: self.editar_servico(nome, nome_entry.get(), preco_entry.get(), tempo_entry.get(), popup))
        confirmar_btn.pack()

    def editar_servico(self, nome_antigo, nome_novo, preco_novo, tempo_novo, popup):
        editado = self.servicos_services.atualizar_servico(nome_antigo, nome_novo, preco_novo, tempo_novo)
        if editado:
            tkinter.messagebox.showinfo("Sucesso", "Serviço editado com sucesso!")
            popup.destroy()
            self.update_servicos_cards()
        else:
            tkinter.messagebox.showerror("Erro", "Não foi possível editar o serviço, verifique os dados.")

    def excluir_servico(self, nome):
         if tkinter.messagebox.askyesno("Confirmar Remoção", f"Tem certeza que deseja remover o serviço '{nome}'?"):
            servicos_services = ServicosServices()
            removido = servicos_services.excluir_servico(nome)
            if removido:
                tkinter.messagebox.showinfo("Sucesso", f"O serviço '{nome}' foi removido com sucesso!")
                self.update_servicos_cards()
            else:
                tkinter.messagebox.showerror("Erro", f"Não foi possível remover o serviço '{nome}'.")
    
    def update_servicos_cards(self):
        for card in self.servico_cards:
            card.destroy()  # Remove os cards antigos

        servicos_text = self.servicos_services.listar_servicos()

        for servico in servicos_text.split("=====\n"):
            if servico.strip():
                servico_frame = self.criar_card_servico(servico, self.frame_inside_canvas)
                servico_frame.pack(fill=tk.BOTH, padx=10, pady=10)
                self.servico_cards.append(servico_frame)  # Adicione o novo card à lista

        self.root.update_idletasks()  # Atualize o GUI para refletir as mudanças


    # Funções de Perfil
    def update_perfil_frame(self, nome, email, senha):
        self.nome_label.config(text=f"Nome: {nome}")
        self.email_label.config(text=f"Email: {email}")
        self.senha_label.config(text=f"Senha: {senha}")

    def abrir_popup_editar_perfil(self, cpf, nome, email, senha):
        popup = tk.Toplevel(self.root)
        popup.title("Editar Perfil")

        nome_label = tk.Label(popup, text="Nome:")
        nome_label.pack()
        nome_entry = tk.Entry(popup)
        nome_entry.insert(0, nome)
        nome_entry.pack()

        email_label = tk.Label(popup, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(popup)
        email_entry.insert(0, email)
        email_entry.pack()

        senha_label = tk.Label(popup, text="Senha:")
        senha_label.pack()
        senha_entry = tk.Entry(popup)
        senha_entry.insert(0, senha)
        senha_entry.pack()

        confirmar_btn = tk.Button(popup, text="Confirmar", command=lambda: self.editar_perfil(cpf, nome_novo=nome_entry.get(), email_novo=email_entry.get(), senha_nova=senha_entry.get(), popup=popup))
        confirmar_btn.pack()

    def editar_perfil(self, cpf, nome_novo, email_novo, senha_nova, popup):
        editado = self.servicos_perfil.atualizar_perfil(cpf=cpf, nome_novo=nome_novo, email_novo=email_novo, senha_nova=senha_nova)
        if editado:
            tkinter.messagebox.showinfo("Sucesso", "Serviço editado com sucesso!")
            popup.destroy()

            perfil_atualizado = self.servicos_perfil.current_user_info()
            nome = perfil_atualizado['nome']
            email = perfil_atualizado['email']
            senha = perfil_atualizado['senha']

            self.update_perfil_frame(nome=nome, email=email, senha=senha)
        else:
            tkinter.messagebox.showerror("Erro", "Não foi possível editar o perfil")        

    def deletar_perfil(self):
        # Implemente a lógica para deletar o perfil
        self.servicos_perfil.deletar_perfil()
        self.logout()
        pass

    def logout(self):
        self.servicos_perfil.logout()
        self.main_frame.destroy()
        self.options_frame.destroy()
        LoginScreen(self.root, self.app)

    # Funções Agendamento
    def abrir_popup_criar_agendamento(self):
        popup = tk.Toplevel(self.root)
        popup.title("Criar Novo Agendamento")

        lista_services = self.servicos_services.listar_nomes()

        nome_service_label = tk.Label(popup, text="Nome do Serviço:")
        nome_service_label.pack()
        nome_servico_combo = ttk.Combobox(popup, values=lista_services)
        nome_servico_combo.pack()

        nome_cliente_label = tk.Label(popup, text="Nome do Cliente:")
        nome_cliente_label.pack()
        nome_cliente_entry = tk.Entry(popup)
        nome_cliente_entry.pack()

        tel_cliente_label = tk.Label(popup, text="Telefone do Cliente:")
        tel_cliente_label.pack()
        tel_cliente_entry = tk.Entry(popup)
        tel_cliente_entry.pack()

        data_label = tk.Label(popup, text="Data:")
        data_label.pack()
        data_calendar = Calendar(popup, selectmode="day", year=2023, month=8, day=22)
        data_calendar.pack(padx=10, pady=10)

        # Campo de Hora
        hora_label = tk.Label(popup, text="Hora:")
        hora_label.pack()
        horas = [str(i).zfill(2) for i in range(1, 24)]
        hora_entry = ttk.Combobox(popup, values=horas)
        hora_entry.pack(padx=10, pady=10)



        confirmar_btn = tk.Button(popup, text="Confirmar", command=lambda: HomeScreen.adicionar_agendamento(self, nome_servico_combo.get(), nome_cliente_entry.get(), tel_cliente_entry.get(), data_calendar.get_date(), hora_entry.get(), popup))
        confirmar_btn.pack()

    def adicionar_agendamento(self, nome_servico_combo, nome_cliente_entry, tel_cliente_entry, data_calendar, hora_entry, popup):
        adicionado = self.servicos_agendamento.salvar_agendamento(servico=nome_servico_combo ,cliente_nome=nome_cliente_entry, cliente_tel=tel_cliente_entry, data=data_calendar, hora=hora_entry)
        if adicionado:
            tkinter.messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            popup.destroy()
            self.update_agendamentos_cards()  
        else:
            tkinter.messagebox.showerror("Erro", "Não foi possivel cadastrar esse agendamento, verifique os dados.")

    def criar_card_agendamento(self, agendamento_text, agendamentos_frame):
        agendamento_frame = tk.Frame(agendamentos_frame, borderwidth=2, relief="solid")
        
        # Extrair informações do texto do serviço
        lines = agendamento_text.split("\n")
        id = lines[0].split(": ")[1]
        data = lines[1].split(": ")[1]
        hora = lines[2].split(": ")[1]
        serviço = lines[3].split(": ")[1]
        cliente_nome = lines[4].split(": ")[1]
        cliente_telefone = lines[5].split(": ")[1]


        cliente_nome_label = tk.Label(agendamento_frame,  font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Nome Cliente: {cliente_nome}")
        cliente_telefone_label = tk.Label(agendamento_frame,  font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Telefone: {cliente_telefone}") 
        serviço_label = tk.Label(agendamento_frame,  font=(12), fg='#fff', bd=0, bg='#158aff',  text=f"Serviço: {serviço}")
        data_label = tk.Label(agendamento_frame,  font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Data: {data}")
        hora_label = tk.Label(agendamento_frame,  font=(12), fg='#fff', bd=0, bg='#158aff', text=f"Tempo: {hora}")

        editar_btn = tk.Button(agendamento_frame, text="Editar", font=(12), fg='#158aff', bd=0, bg='#fff', command=lambda: self.abrir_popup_editar_agendamento(id=id, cliente_nome=cliente_nome, cliente_telefone=cliente_telefone, data=data, hora=hora, servico=serviço))
        excluir_btn = tk.Button(agendamento_frame, text="Excluir", font=(12), fg='#158aff', bd=0, bg='#fff', command=lambda: self.excluir_agendamento( id=id, nome=cliente_nome))

        # Organize os elementos usando o grid manager
        cliente_nome_label.grid(row=0, column=0, padx=5, pady=5)
        cliente_telefone_label.grid(row=1, column=0, padx=5, pady=5)
        serviço_label.grid(row=2, column=0, padx=5, pady=5)
        data_label.grid(row=3, column=0, padx=5, pady=5)
        hora_label.grid(row=4, column=0, padx=5, pady=5)

        editar_btn.grid(row=5, column=4, padx=5, pady=5)
        excluir_btn.grid(row=5, column=5, padx=5, pady=5)

        self.agendamento_cards.append(agendamento_frame)  # Adicione o card à lista
        return agendamento_frame
    
    def abrir_popup_editar_agendamento(self, id, cliente_nome, cliente_telefone, data, hora, servico):
        popup = tk.Toplevel(self.root)
        popup.title("Editar Agendamento")


        cliente_nome_label = tk.Label(popup, text="Nome do Cliente:")
        cliente_nome_label.pack()
        cliente_nome_entry = tk.Entry(popup)
        cliente_nome_entry.insert(0, cliente_nome)
        cliente_nome_entry.pack()

        cliente_telefone_label = tk.Label(popup, text="Telefone do cliente:")
        cliente_telefone_label.pack()
        cliente_telefone_entry = tk.Entry(popup)
        cliente_telefone_entry.insert(0, cliente_telefone)
        cliente_telefone_entry.pack()

        confirmar_btn = tk.Button(popup, text="Confirmar", command=lambda: self.editar_agendamento(id=id, cliente_nome=cliente_nome_entry.get(), cliente_telefone=cliente_telefone_entry.get(), data=data, hora=hora, servico=servico, popup=popup))
        confirmar_btn.pack()

    def editar_agendamento(self, cliente_nome, cliente_telefone, id, data, hora, servico, popup):
        editado = self.servicos_agendamento.atualizar_agendamento(id=id, cliente=cliente_nome, telefone=cliente_telefone,data=data, hora=hora, servico=servico)
        if editado:
            tkinter.messagebox.showinfo("Sucesso", "Agendamento editado com sucesso!")
            popup.destroy()
            self.update_agendamentos_cards()
        else:
            tkinter.messagebox.showerror("Erro", "Não foi possível editar o agendamento, verifique os dados.")

    def excluir_agendamento(self, id, nome):
         if tkinter.messagebox.askyesno("Confirmar Remoção", f"Tem certeza que deseja remover o agendamento '{nome}'?"):
            removido = self.servicos_agendamento.excluir_agendamento(id)
            if removido:
                tkinter.messagebox.showinfo("Sucesso", f"O agendamento '{nome}' foi removido com sucesso!")
                self.update_agendamentos_cards()
            else:
                tkinter.messagebox.showerror("Erro", f"Não foi possível remover o serviço '{nome}'.")
    
    def update_agendamentos_cards(self):
        for card in self.agendamento_cards:
            card.destroy()  # Remove os cards antigos

        agendamentos_text = self.servicos_agendamento.listar_agendamentos()

        for agendamento in agendamentos_text.split("=====\n"):
            if agendamento.strip():
                agendamento_frame = self.criar_card_agendamento(agendamento, self.frame_inside_canvas)
                agendamento_frame.pack(fill=tk.BOTH, padx=10, pady=10)
                self.agendamento_cards.append(agendamento_frame)  # Adicione o novo card à lista

        self.root.update_idletasks()  # Atualize o GUI para refletir as mudanças

class PetShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Shop App")
        self.root.geometry("800x600")  # Defina a largura e a altura desejadas

        self.iniciar_tela_login()

    def iniciar_tela_login(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()
        self.login_screen = LoginScreen(self.login_frame, self)  # Mantenha uma referência à tela de login

    
    def mostrar_tela_cadastro(self):
        self.login_frame.destroy()
        CadastroScreen(self.root, self.app)

if __name__ == "__main__":
    root = tk.Tk()
    app = PetShopApp(root)
    root.mainloop()
