import json
from jogo import jogo_from_dict, JogoConsole, JogoMobile, JogoPC

class Catalogo:
    def __init__(self):
        self.jogos = []
        self.jogos_filtrados = None
    
    def adicionarJogo(self,limite_jogando):
        while True: 
            try:
                nome = input("Digite o nome do jogo: ")
                genero = input("Digite o genero do jogo: ")
                plataforma = input("Digite a plataforma do seu jogo (pc, mobile, console): ")
                ano = input("Digite o ano de laçamento: ")
                multiplayer = input("Jogo é multiplayer?(sim ou não): ")
                if multiplayer == "sim":
                    multiplayer = True
                else:
                    multiplayer = False
                status = int(input("Digite o status, 1.inativo, 2.jogando ou 3.finalizado: "))
                if status == 1:
                    data_inicio = "Não informada"
                    data_termino = "Não informada"
                    horas_jogadas = 0
                    avaliacao = 0

                elif status == 2:
                    contJogando = sum(1 for j in self.jogos if j.status == "jogando")
                    limite = limite_jogando
                    if limite is not None and limite != "" and contJogando >= int(limite):
                        print(f"\nVocê atingiu o limite de ({limite}) jogos com status 'jogando'.")
                        return
                    horas_jogadas = float(input("Digite as horas jogadas: "))
                    data_inicio = input("Digite a data estimada que você começou a jogar: " )
                    data_termino = "Não informada"
                    avaliacao = 0

                elif status == 3:
                    horas_jogadas = float(input("Digite as horas jogadas: "))
                    data_inicio = input("Digite a data estimada que você começou a jogar: " )
                    data_termino = input("Digite a data estimada que você terminou de jogar: " )
                    avaliacao = input("Como você avalia o jogo?(1-10): ")

                if plataforma == "pc":
                    launcher = input("Digite o seu laucher: ")
                    jogo = JogoPC(launcher, nome, genero, plataforma,horas_jogadas, status, data_inicio, data_termino, ano, avaliacao, multiplayer)

                elif plataforma == "console":
                    console = input("Digite o seu console: ")
                    jogo = JogoConsole(console, nome, genero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano, avaliacao, multiplayer)

                elif plataforma == "mobile":
                    sistema = input("Seu sistema é android, IOs ou outro? ")
                    jogo = JogoMobile(sistema, nome, genero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano, avaliacao, multiplayer)

                else:
                    raise ValueError("Plataforma inválida.")

                for existente in self.jogos:
                    if existente == jogo:
                        print("\n[Este jogo já existe nesta plataforma!]")
                        return
                    
                self.jogos.append(jogo)
                self.salvar()
                print("\nJogo adicionado com sucesso!")
                break
            except ValueError as erro:
                print(f"Erro: {erro}. Tente novamente.\n")
    
    def salvar(self):
        lista_dicts = [jogo.dicionario() for jogo in self.jogos]

        with open("data/jogos.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_dicts, arquivo, indent=4, ensure_ascii=False)

    def carregar(self):
        try:
            with open("data/jogos.json", "r", encoding="utf-8") as arquivo:
                lista_dicts = json.load(arquivo)
                self.jogos = [jogo_from_dict(d) for d in lista_dicts]
        except FileNotFoundError:
            self.jogos = []


    def listarNomes(self):
        lista = self.jogos_filtrados if self.jogos_filtrados is not None else self.jogos
        print("\nJogos cadastrados:")
        if not self.jogos:
            print("Nenhum jogo cadastrado!")
            return
        else:
            for jogo in lista:
                print(jogo)

    def abrirJogo(self):
        while True:
            nome = input("Digite o nome do jogo que deseja abrir: ").strip()
            if nome == "":
                return None
            encontrados = [j for j in self.jogos if j.nome.lower() == nome.lower()]
            if len(encontrados) == 0:
                print("\n[Jogo não encontrado. Tente novamente!]\n")
                continue
            if len(encontrados) == 1:
                return encontrados[0]
            print(f"\nForam encontrados {len(encontrados)} jogos com o nome '{nome}':\n")
            for i, jogo in enumerate(encontrados, start=1):
                print(f"{i}. {jogo.nome} - Plataforma: {jogo.plataforma}")
            while True:
                try:
                    escolha = int(input("\nEscolha o número do jogo que deseja abrir: "))
                    if 1 <= escolha <= len(encontrados):
                        return encontrados[escolha - 1]
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")

    def removerJogo(self):
        while True:
            nome = input("Digite o nome do jogo que deseja remover: ").strip()
            if nome == "":
                return
            encontrados = [j for j in self.jogos if j.nome.lower() == nome.lower()]
            if len(encontrados) == 0:
                print("\n[Jogo não encontrado. Tente novamente!]\n")
                continue
            if len(encontrados) == 1:
                self.jogos.remove(encontrados[0])
                self.salvar()
                print("\n[Jogo removido com sucesso!]\n")
                return
            print(f"\nForam encontrados {len(encontrados)} jogos com o nome '{nome}':\n")
            for i, jogo in enumerate(encontrados, start=1):
                print(f"{i}. {jogo.nome} - Plataforma: {jogo.plataforma}")
            while True:
                try:
                    escolha = int(input("\nEscolha o número do jogo que deseja remover: "))
                    if 1 <= escolha <= len(encontrados):
                        jogo_escolhido = encontrados[escolha - 1]
                        self.jogos.remove(jogo_escolhido)
                        self.salvar()
                        print("\n[Jogo removido com sucesso!]")
                        return
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")

    def filtrarGenero(self):
        generos = sorted({jogo.genero for jogo in self.jogos})
        print("\nGêneros cadastrados:")
        for g in generos:
            print("-", g)
        genero = input("\nDigite o gênero que deseja filtrar: ").strip()
        if genero not in generos:
            print("\n[Gênero não encontrado!]")
            return
        self.jogos_filtrados = [jogo for jogo in self.jogos if jogo.genero == genero]

    def filtrarPlataforma(self):
        plataformas = sorted({jogo.plataforma for jogo in self.jogos})
        for p in plataformas:
            print("-", p)
        plataforma = input("\nDigite a plataforma que deseja filtrar: ").strip()
        if plataforma not in plataformas:
            print("[Plataforma não encontrada!]")
            return
        self.jogos_filtrados = [jogo for jogo in self.jogos if jogo.plataforma == plataforma]

    def filtrarStatus(self):
        statuss = sorted({jogo.status for jogo in self.jogos})
        for s in statuss:
            print("-", s)
        status = input("\nDigite o status que deseja filtrar: ").strip()
        if status not in statuss:
            print("[Status não encontrado!]")
            return
        self.jogos_filtrados = [jogo for jogo in self.jogos if jogo.status == status]

    def ordenarTempoJogado(self,ordem):
        lista = self.jogos_filtrados if self.jogos_filtrados is not None else self.jogos
        if not lista:
            print("\n[Nenhum jogo para ordenar!]")
            return
        lista.sort(key=lambda j: j.horas_jogadas, reverse=ordem)

    def ordenarLancamento(self,ordem):
        lista = self.jogos_filtrados if self.jogos_filtrados is not None else self.jogos
        if not lista:
            print("\n[Nenhum jogo para ordenar!]")
            return
        lista.sort(key=lambda j: j.ano_lancamento, reverse=ordem)

    def limparFiltro(self):
        self.jogos_filtrados = None  