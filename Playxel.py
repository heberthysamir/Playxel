from datetime import date, datetime

class Jogo:
    STATUS_MAP = {
        1: "não iniciado",
        2: "jogando",
        3: "finalizado"
    }
    def __init__(self, nome, genero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano_lancamento, avaliacao):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.horas_jogadas = horas_jogadas
        self.status = status
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.ano_lancamento = ano_lancamento
        self.avaliacao = avaliacao
    
    def __str__(self):
        return f"{self.nome} ({self.genero}) - {self.status}"

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
    def data_inicio(self, data_inicio):
        if data_inicio is None or data_inicio == "":
            self._data_inicio = None
            return
        try:
            self._data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data de inicio inválida. Use o formato dd/mm/yyyy.")

    @property
    def data_termino(self):
        return self._data_termino
    @data_termino.setter
    def data_termino(self, data_termino):
        if data_termino is None or data_termino == "":
            self._data_termino = None
            return
        try:
            self._data_termino = datetime.strptime(data_termino, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data de término inválida. Use o formato dd/mm/yyyy.")

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        if status not in (1,2,3):
            raise ValueError("Status deve ser 1, 2 ou 3.")
        self._status = Jogo.STATUS_MAP[status]

    def atualizarHoras(self):
        pass
    def atualizarStatus(self):
        pass
    def finalizarJogo(self, horas):
        if horas <5:
            print("Não é possível finalizar o jogo com menos de 5 horas jogadas")
        else:
            self.avaliacao = int(input("Avalie o jogo, (1-10):"))
            self.horas_jogadas = horas
            self.status = 3
            self.data_termino = date.today().strftime("%d/%m/%Y")
            
    def reiniciarJogo(self):
        pass

class JogoPC(Jogo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class JogoConsole(Jogo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class JogoMobile(Jogo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Catalogo:
    def __init__(self):
        self.jogos = []
    
    def adicionarJogo(self):
        while True: 
            try:
                nome = input("Digite o nome do jogo: ")
                genero = input("Digite o genero do jogo: ")
                plataforma = input("Digite a plataforma do seu jogo: ")
                horas_jogadas = float(input("Digite as horas jogadas: "))
                status = int(input("Digite o status, 1.não iniciado, 2.jogando ou 3.finalizado: "))
                data_inicio = input("Digite a data que você começou a jogar: " )
                data_termino = None
                ano = input("Digite o ano de laçamento: ")
                avaliacao = None
                if plataforma == "pc":
                    jogo = JogoPC(nome, genero, plataforma,horas_jogadas, status, data_inicio, data_termino, ano, avaliacao)
                elif plataforma == "console":
                    jogo = JogoConsole(nome, genero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano, avaliacao)
                elif plataforma == "mobile":
                    jogo = JogoMobile(nome, genero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano, avaliacao)
                else:
                    raise ValueError("Plataforma inválida.")

                self.jogos.append(jogo)
                print("Jogo adicionado com sucesso!")
                break
            except ValueError as erro:
                print(f"Erro: {erro}. Tente novamente.\n")

    def listarNomes(self):
        print("\nJogos cadastrados:")
        if not self.jogos:
            print("Nenhum jogo cadastrado!")
            return
        else:
            for jogo in self.jogos:
                print(jogo)

    def removerJogo(self):
        pass
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
                return colecao  # retorna a coleção encontrada
        print("Coleção não encontrada!")
        return None


    def listarColecoes(self):
        print("\nSuas Coleções:")
        if not self.colecaos:
            print("Nenhuma coleção")
            return
        else:
            for colecao in self.colecaos:
                print(colecao)

class Relatorio:
    def __init__(self, horas_jogadas, avaliacao, status):
        self.horas_jogadas = horas_jogadas
        self.avaliacao = avaliacao
        self.status = status

    def calcularHorasTotais(self):
        pass
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
suasColecoes = ListaDeColecoes()

if __name__ == "__main__":
    while True:
        print("- Opções: \n1.Catálogo\n2.Suas coleções\n3.Sair")
        user = int(input("Digite uma opção: "))
        if user == 3:
            break
        elif user == 1:
            while True:
                catalogo.listarNomes()
                print("\n-Opções do catálogo:\n1.Adicionar Jogo\n2.Remover Jogo\n3.Buscar Jogo\n4.Abrir Jogo\n5.Filtrar Jogos\n6.Ordenar Jogos\n7.Voltar")
                user = int(input("\nDigite uma opção do catálogo: "))
                if user == 1:
                    catalogo.adicionarJogo()
                elif user == 7:
                    break
        elif user == 2:
            while True:
                suasColecoes.listarColecoes()
                print("\n-Opções das Coleções:\n1.Criar coleção\n2.Remover coleção\n3.Abrir coleção\n4.Voltar")
                user = int(input("\nDigite uma opção do catálogo: "))
                if user == 1:
                    suasColecoes.criarColecao()
                elif user == 3:
                    colecao = suasColecoes.abrirColecao()
                    if colecao is None:
                        continue 
                    while True:
                        print(f"\nColeção: {colecao.nome}")
                        colecao.exibirJogos()
                        print("\n1. Adicionar Jogo\n2. Remover Jogo\n3. Voltar")
                        user = int(input("Digite uma opção da coleção: "))
                        if user == 1:
                            colecao.adicionarJogo()
                        elif user == 3:
                            break
                elif user == 4:
                    break