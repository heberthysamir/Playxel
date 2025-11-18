class Jogo:
    def __init__(self, nome, genero, plataforma, horas_jogadas, status, data_inicio, data_termino,ano_lancamento, avaliacao):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.horas_jogadas = horas_jogadas
        self.status = status
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.ano_lancamento = ano_lancamento
        self.avaliacao = avaliacao

    def atualizarHoras():
        pass
    def atualizarStatus():
        pass
    def finalizarJogo():
        pass
    def reiniciarJogo():
        pass

class Catalogo:
    def __init__(self, jogo):
        self.jogo = jogo
    
    def adiadicionarJogo():
        pass
    def removerJogo():
        pass
    def filtrarGenero():
        pass
    def filtrarAvaliacao():
        pass
    def filtrarPlataforma():
        pass
    def filtrarStatus():
        pass
    def ordenarAvaliacao():
        pass
    def ordenarTempoJogado():
        pass
    def ordenarLançamento():
        pass
    def buscarTitulo():
        pass

class Colecao:
    def __init__(self, nome, jogo):
        self.nome = nome
        self.jogo = jogo

    def adicionarJogo():
        pass
    def removerJogo():
        pass
    def exibirJogos():
        pass

class ListaDeColecoes:
    def __init__(self,colecao):
        self.colecao = colecao
    
    def criarColecao():
        pass
    def removerColecao():
        pass
    def abrirColecao():
        pass

class Relatorio:
    def __init__(self, horas_jogadas, avaliacao, status):
        self.horas_jogadas = horas_jogadas
        self.avaliacao = avaliacao
        self.status = status

    def calcularHorasTotais():
        pass
    def calcularAvaliacoes():
        pass
    def calcularPercentualStatus():
        pass
    def top5Jogos():
        pass

class Configuracoes:
    def __init__(self, genero_favorito, metas, plataforma_principal):
        self.genero_favorito = genero_favorito
        self.metas = metas
        self.plataforma_principal = plataforma_principal