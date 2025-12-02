import json

class Jogo:
    STATUS_MAP = {
        1: "inativo",
        2: "jogando",
        3: "finalizado"
    }
    def __init__(self, nome, genero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano_lancamento, avaliacao, multiplayer):
        self._nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self._horas_jogadas = horas_jogadas
        self.status = status
        self._data_inicio = data_inicio
        self._data_termino = data_termino
        self.ano_lancamento = ano_lancamento
        self._avaliacao = avaliacao
        self.multiplayer = multiplayer
    
    def __str__(self):
        return f"{self.nome} ({self.genero}) - {self.status}"
    
    def dicionario(self):
        return {
            "nome": self.nome,
            "genero": self.genero,
            "plataforma": self.plataforma,
            "horas_jogadas": self.horas_jogadas,
            "status": self.status,
            "data_inicio": self.data_inicio,
            "data_termino": self.data_termino,
            "ano_lancamento": self.ano_lancamento,
            "avaliacao": self.avaliacao,
            "multiplayer": self.multiplayer,
            "tipo": self.__class__.__name__,
            "extra": getattr(self, "launcher", getattr(self, "console", getattr(self, "sistema", None)))
        }

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        if nome is None or len(nome.strip()) == 0:
            raise ValueError("Nome não pode ser vazio")
        else:
            self._nome = nome

    @property
    def avaliacao(self):
        return self._avaliacao
    @avaliacao.setter
    def avaliacao(self, avaliacao):
        if avaliacao is None or avaliacao == "":
            self._avaliacao = None
            return
        try:
           avaliacao = float(avaliacao)
        except ValueError:
            raise ValueError("A avaliação deve ser um número entre 0 e 10.")
        if avaliacao <0 or avaliacao > 10:
            raise ValueError("A avaliação deve estar entre 0 e 10.")
        self._avaliacao = avaliacao

    @property
    def horas_jogadas(self):
        return self._horas_jogadas
    @horas_jogadas.setter
    def horas_jogadas(self,horas_jogadas):
        if horas_jogadas <0:
            raise ValueError("As horas não podem ser negativas")
        else:
            self._horas_jogadas = horas_jogadas

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, data):
        if data is None or len(data.strip()) == 0:
            self._data_inicio = "Data de início não informada"
        else:
            self._data_inicio = data

    @property
    def data_termino(self):
        return self._data_termino

    @data_termino.setter
    def data_termino(self, data):
        if data is None or len(data.strip()) == 0:
            self._data_termino = "Data de término não informada"
        else:
            self._data_termino = data

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        if status not in (1,2,3):
            raise ValueError("Status deve ser 1, 2 ou 3.")
        self._status = Jogo.STATUS_MAP[status]

    def atualizarHoras(self):
        horas = float(input("Digite quantas horas você quer adicionar:"))
        self.horas_jogadas += horas
        print("Horas aualizadas:", self.horas_jogadas)

    def atualizarStatus(self):
        novo_status = int(input("Qual é o novo status? (1. inativo, 2. jogando, 3. finalizado): "))
        if novo_status == 1:
            self.status = 1
            print("Status atualizado",self.status)
        elif novo_status == 2:
            self.status = 2
            self.data_inicio = input("Digite a data que começou/voltou a jogar: ")
            self.horas_jogadas += int(input("Digite quantas horas foram jogadas: "))
            print("Status atualizado",self.status)
        elif novo_status == 3:
            self.finalizarJogo()
        else:
            raise ValueError("Status deve ser 1, 2 ou 3.")
            
    def finalizarJogo(self):
        if self.horas_jogadas <5:
            print("Não é possível finalizar o jogo com menos de 5 horas jogadas")
        else:
            self.avaliacao = int(input("Avalie o jogo, (1-10):"))
            self.status = 3
            self.data_termino = input("Digite a data estimada do término: ")
            print("Jogo finalizado.")
            
    def reiniciarJogo(self):
        reiniciar = input("Deseja mesmo reiniciar o jogo?(sim ou não): ")
        if reiniciar == "sim":
            self.horas_jogadas = 0
            self.status
            self.data_termino = "Não informada"
            self.data_inicio = "Não informada"
            self.avaliacao = 0
            self.status = 1
        else:
            return False

class JogoPC(Jogo):
    def __init__(self, launcher, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launcher = launcher

class JogoConsole(Jogo):
    def __init__(self, console, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.console = console 

class JogoMobile(Jogo):
    def __init__(self, sistema,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sistema = sistema

def jogo_from_dict(data):
    tipo = data.get("tipo")

    if tipo == "JogoPC":
        return JogoPC(
            data["extra"], data["nome"], data["genero"], data["plataforma"], data["horas_jogadas"],
            1 if data["status"] == "inativo" else
            2 if data["status"] == "jogando" else 3,
            data["data_inicio"], data["data_termino"], data["ano_lancamento"],
            data["avaliacao"], data["multiplayer"]
        )

    if tipo == "JogoConsole":
        return JogoConsole(
            data["extra"],
            data["nome"], data["genero"], data["plataforma"], data["horas_jogadas"],
            1 if data["status"] == "inativo" else
            2 if data["status"] == "jogando" else 3,
            data["data_inicio"], data["data_termino"], data["ano_lancamento"],
            data["avaliacao"], data["multiplayer"]
        )

    if tipo == "JogoMobile":
        return JogoMobile(
            data["extra"],
            data["nome"], data["genero"], data["plataforma"], data["horas_jogadas"],
            1 if data["status"] == "inativo" else
            2 if data["status"] == "jogando" else 3,
            data["data_inicio"], data["data_termino"], data["ano_lancamento"],
            data["avaliacao"], data["multiplayer"]
        )

class Catalogo:
    def __init__(self):
        self.jogos = []
    
    def adicionarJogo(self):
        while True: 
            try:
                nome = input("Digite o nome do jogo: ")
                genero = input("Digite o genero do jogo: ")
                plataforma = input("Digite a plataforma do seu jogo (pc, mobile, console): ")
                ano = input("Digite o ano de laçamento: ")
                multiplayer = input("Jogo é multiplayer?(sim ou não): ")
                status = int(input("Digite o status, 1.inativo, 2.jogando ou 3.finalizado: "))
                if status == 1:
                    data_inicio = "Não informada"
                    data_termino = "Não informada"
                    horas_jogadas = 0
                    avaliacao = 0
                elif status == 2:
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
                    sistema = input("Seu sistema é android ou IOs? ")
                    jogo = JogoMobile(sistema, nome, genero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano, avaliacao, multiplayer)
                else:
                    raise ValueError("Plataforma inválida.")

                self.jogos.append(jogo)
                self.salvar()
                print("Jogo adicionado com sucesso!")
                break
            except ValueError as erro:
                print(f"Erro: {erro}. Tente novamente.\n")
    
    def salvar(self):
        lista_dicts = [jogo.dicionario() for jogo in self.jogos]

        with open("jogos.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_dicts, arquivo, indent=4, ensure_ascii=False)

    def carregar(self):
        try:
            with open("jogos.json", "r", encoding="utf-8") as arquivo:
                lista_dicts = json.load(arquivo)
                self.jogos = [jogo_from_dict(d) for d in lista_dicts]
        except FileNotFoundError:
            self.jogos = []


    def listarNomes(self):
        print("\nJogos cadastrados:")
        if not self.jogos:
            print("Nenhum jogo cadastrado!")
            return
        else:
            for jogo in self.jogos:
                print(jogo)

    def abrirJogo(self):
        nome = input("Digite o nome do jogo que deseja abrir: ")
        for jogo in self.jogos:
            if jogo.nome == nome:
                return jogo
        print("\nJogo não encontrado. Tente novamente.\n")
        return None

    def removerJogo(self):
        nome = input("Digite o nome do jogo que deseja remover: ")
        for jogo in self.jogos:
            if jogo.nome == nome:
                self.jogos.remove(jogo)
                self.salvar()
                print("Jogo deletado")
                return
        print("Jogo não encontrado.")
    
    def filtrarGenero(self):
        pass
    def filtrarAvaliacao(self):
        pass
    def filtrarPlataforma(self):
        pass
    def filtrarStatus(self):
        pass
    def ordenarAvaliacao(self):
        pass
    def ordenarTempoJogado(self):
        pass
    def ordenarLancamento(self):
        pass
    def buscarTitulo(self):
        pass

class Colecao:
    def __init__(self, nome, jogos = None):
        self.nome = nome
        self.jogos = jogos if jogos is not None else []

    def __str__(self):
        return f"{self.nome}"

    def adicionarJogo(self):
        jogo_nome = input("Digite o nome do jogo que quer adicionar: ")
        for j in catalogo.jogos:
            if j.nome == jogo_nome:
                self.jogos.append(j)
                print("Jogo adicionado.")
                return 
        print("Jogo não encontrado!")

    def removerJogo(self):
        pass
    def exibirJogos(self):
        if not self.jogos:
            print("Nenhum jogo na coleção.")
            return

        for jogo in self.jogos:
            print(" -", jogo.nome)

class ColecaoFinalizado(Colecao):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ColecaoMultiplayer(Colecao):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ListaDeColecoes:
    def __init__(self):
        self.colecaos = []
    
    def criarColecao(self):
        nome = input("Digite o nome da coleção: ")
        for c in self.colecaos:
            if c.nome == nome:
                print("Já existe uma coleção com esse nome.")
                return
        nova = Colecao(nome, [])
        self.colecaos.append(nova)
        print("Coleção criada!")

    def removerColecao(self):
        pass

    def abrirColecao(self):
        nome = input("Digite o nome da coleção que deseja abrir: ")
        for colecao in self.colecaos:
            if colecao.nome == nome:
                return colecao
        print("Coleção não encontrada.")
        return None


    def listarColecoes(self):
        print("\nSuas Coleções:")
        if not self.colecaos:
            print("Nenhuma coleção")
            return
        else:
            for colecao in self.colecaos:
                print("-",colecao)

class Relatorio:
    def __init__(self,jogos):
        self.jogos = jogos

    def calcularHorasTotais(self):
        return sum(j.horas_jogadas for j in self.jogos)
    
    def calcularJogos(self):
        return len(self.jogos)
    
    def calcularAvaliacoes(self):
        pass
    def calcularPercentualStatus(self):
        pass
    def top5Jogos(self):
        pass

class Configuracoes:
    def __init__(self, genero_favorito, metas, plataforma_principal):
        self.genero_favorito = genero_favorito
        self.metas = metas
        self.plataforma_principal = plataforma_principal

catalogo = Catalogo()
catalogo.carregar()
suasColecoes = ListaDeColecoes()

if __name__ == "__main__":
    while True:
        print("- Opções: \n1.Catálogo\n2.Suas coleções\n3.Relatório\n4.Configurações\n5.Sair")
        user = int(input("Digite uma opção: "))
        if user == 5:
            break 
        elif user == 1:
            while True:
                catalogo.listarNomes()
                print("\n-Opções do catálogo:\n1.Adicionar Jogo\n2.Remover Jogo\n3.Buscar Jogo\n4.Abrir Jogo\n5.Filtrar Jogos\n6.Ordenar Jogos\n7.Voltar")
                user = int(input("\nDigite uma opção do catálogo: "))
                if user == 1:
                    jogo = catalogo.adicionarJogo()
                if user == 2:
                    jogo = catalogo.removerJogo()
                elif user == 4:
                    jogo = catalogo.abrirJogo()
                    while True:
                        if jogo is None:
                            continue 
                        print(f"\nJogo: {jogo.nome} ({jogo.genero}) - {jogo.plataforma}\n Status: {jogo.status}\n Horas jogadas: {jogo.horas_jogadas}\n Data de início: {jogo.data_inicio}\n Data de término {jogo.data_termino}")
                        print("\n1.Atualizar horas\n2.Atualizar status\n3.Reiniciar jogo\n4.Voltar")
                        user = int(input("Digite o que quer fazer com seu jogo: "))
                        if user == 1:
                            jogo.atualizarHoras()
                            catalogo.salvar()
                        elif user == 2:
                            jogo.atualizarStatus()
                            catalogo.salvar()
                        elif user == 3:
                            jogo.reiniciarJogo()
                            catalogo.salvar()
                        elif user == 4:
                            break
                elif user == 7:
                    break
        elif user == 2:
            while True:
                suasColecoes.listarColecoes()
                print("\n-Opções das Coleções:\n1.Criar coleção\n2.Remover coleção\n3.Abrir coleção\n4.Voltar")
                user = int(input("\nDigite uma opção da coleção: "))
                if user == 1:
                    suasColecoes.criarColecao()
                elif user == 3:
                    colecao = suasColecoes.abrirColecao()
                    if colecao is None:
                        continue 
                    while True:
                        print(f"\nColeção: {colecao.nome}")
                        colecao.exibirJogos()
                        print("\n1.Adicionar Jogo\n2. Remover Jogo\n3. Voltar")
                        user = int(input("Digite uma opção da coleção: "))
                        if user == 1:
                            colecao.adicionarJogo()
                        elif user == 3:
                            break
                elif user == 4:
                    break
        elif user == 3:
            rel = Relatorio(catalogo.jogos)
            print("\nHoras totais:", rel.calcularHorasTotais())
            print("Quantidade de jogos:", rel.calcularJogos(),"\n")

