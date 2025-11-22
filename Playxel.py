from datetime import date, datetime

class Jogo:
    STATUS_MAP = {
        1: "não iniciado",
        2: "jogando",
        3: "finalizado"
    }
    def __init__(self, nome, genero, dispositivo, horas_jogadas, status, data_inicio, data_termino, ano_lancamento, avaliacao):
        self.nome = nome
        self.genero = genero
        self.dispositivo = dispositivo
        self.horas_jogadas = horas_jogadas
        self.status = status
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.ano_lancamento = ano_lancamento
        self.avaliacao = avaliacao

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
    def data_inicio(self,data_inicio):
        try:
            data_obj = datetime.strptime(data_inicio, "%d/%m/%Y")
            self._data_inicio = data_obj
        except ValueError:
            print("Formato de data inválido. Use o formato DD/MM/AAAA.")

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
            self.status = "finalizado"
            self.data_termino = date.today()
            
    def reiniciarJogo(self):
        pass

class JogoPC(Jogo):
    def __init__(self):
        pass

class JogoConsole(Jogo):
    def __init__(self):
        pass

class JogoMobile(Jogo):
    def __init__(self):
        pass
    
class Catalogo:
    def __init__(self):
        self.jogos = []
    
    def adicionarJogo(self):
        while True: 
            try:
                nome = input("Digite o nome do jogo: ")
                genero = input("Digite o genero do jogo: ")
                dispositivo = input("Digite o dispositivo do seu jogo: ")
                horas_jogadas = float(input("Digite as horas jogadas: "))
                status = int(input("Digite o status, 1.não iniciado, 2.jogando ou 3.finalizado: "))
                data_inicio = input("Digite a data que você começou a jogar: " )
                data_termino = None
                ano = input("Digite o ano de laçamento: ")
                avaliacao = None
                jogo = Jogo(nome, genero, dispositivo, horas_jogadas,status, data_inicio, data_termino, ano, avaliacao)
                self.jogos.append(jogo)
                print("Jogo adicionado com sucesso!")
                break 
            except ValueError as erro:
                print(f"Erro: {erro}. Tente novamente.\n")
        
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
    def __init__(self, nome, jogo):
        self.nome = nome
        self.jogo = jogo

    def adicionarJogo(self):
        pass
    def removerJogo(self):
        pass
    def exibirJogos(self):
        pass

class ListaDeColecoes:
    def __init__(self,colecao):
        self.colecao = colecao
    
    def criarColecao(self):
        pass
    def removerColecao(self):
        pass
    def abrirColecao(self):
        pass

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

print("- Opções: \n1.Catálogo\n2.Coleções\n3.Sair")
user = int(input("Digite uma opção: "))
catalogo = Catalogo()
while user != 3:
    if user == 1:
        print("\n-Opções do ctálogo:\n1.Adicionar Jogo\n2.Remover Jogo\n3.Sair\n4.Abrir Jogo\n5.Filtrar Jogos\n6.Ordenar Jogos\n7.Buscar Jogogo")
        user = int(input("\nDigite uma opção do catálogo: "))
        if user == 1:
            catalogo.adicionarJogo()
