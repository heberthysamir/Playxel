from datetime import datetime

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
        return f"{self.nome}, {self.ano_lancamento}.({self.genero}) - {self.plataforma}"
    
    def __eq__(self, outro):
        if not isinstance(outro, Jogo):
            return False
        return self.nome.lower() == outro.nome.lower() and self.plataforma.lower() == outro.plataforma.lower()

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
    def _nome(self):
        return self.nome
    @_nome.setter
    def _nome(self,_nome):
        if _nome is None or len(_nome.strip()) == 0:
            raise ValueError("[Nome não pode ser vazio!]")
        else:
            self.nome = _nome
    
    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self,genero):
        if genero is None or len(genero.strip()) == 0:
            raise ValueError("[Gênero não pode ser vazio!]")
        else:
            self._genero = genero

    @property
    def _avaliacao(self):
        return self.avaliacao
    @_avaliacao.setter
    def _avaliacao(self, valor):
        if valor is None or valor == "":
            self.avaliacao = None
            return
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError("A avaliação deve ser um número entre 0 e 10.")
        
        if not 0 <= valor <= 10:
            raise ValueError("A avaliação deve estar entre 0 e 10.")
        self.avaliacao = valor

    @property
    def _horas_jogadas(self):
        return self.horas_jogadas
    @_horas_jogadas.setter
    def _horas_jogadas(self,_horas_jogadas):
        if _horas_jogadas <0:
            raise ValueError("[As horas não podem ser negativas!]")
        else:
            self.horas_jogadas = _horas_jogadas

    @property
    def _data_inicio(self):
        return self.data_inicio

    @_data_inicio.setter
    def _data_inicio(self, data):
        if data is None or len(data.strip()) == 0:
            self.data_inicio = "Data de início não informada"
        else:
            self.data_inicio = data

    @property
    def _data_termino(self):
        return self.data_termino

    @_data_termino.setter
    def _data_termino(self, data):
        if data is None or len(data.strip()) == 0:
            self.data_termino = "Data de término não informada"
        else:
            self.data_termino = data

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        if status not in (1,2,3):
            raise ValueError("Status deve ser 1, 2 ou 3.")
        self._status = Jogo.STATUS_MAP[status]
    
    @property
    def ano_lancamento(self):
        return self._ano_lancamento
    @ano_lancamento.setter
    def ano_lancamento(self, ano):
        if ano is None or ano == "":
            self._ano_lancamento = None
            return
        try:
            ano = int(ano)
        except ValueError:
            raise ValueError("Ano de lançamento deve ser um número inteiro.")
        ano_atual = datetime.now().year
        if ano < 1800 or ano > ano_atual:
            raise ValueError(f"[O ano deve estar entre 1800 e {ano_atual}!]")
        self._ano_lancamento = ano

    @property
    def multiplayer(self):
        return self._multiplayer

    @multiplayer.setter
    def multiplayer(self, valor):
        if valor is None:
            self._multiplayer = False
            return
        if isinstance(valor, bool):
            self._multiplayer = valor
            return
        valor = str(valor).strip().lower()

        if valor not in ("sim", "não", "nao"):
            raise ValueError("Multiplayer deve ser 'sim' ou 'não'.")
        self._multiplayer = (valor == "sim")

    def atualizarHoras(self):
        horas = float(input("Digite quantas horas você quer adicionar:"))
        self.horas_jogadas += horas
        print("Horas aualizadas:", self.horas_jogadas)

    def atualizarStatus(self,limite_jogando, jogos,limite_horas):
        novo_status = int(input("Qual é o novo status? (1. inativo, 2. jogando, 3. finalizado): "))
        if novo_status == 1:
            self.status = 1
            print("Status atualizado!",self.status)
        elif novo_status == 2:
            if limite_jogando not in (None, "", 0):
                contJogando = sum(1 for j in jogos if j.status == "jogando")
                if contJogando >= int(limite_jogando):
                    print(f"\n[Você atingiu o limite de ({limite_jogando}) jogos com status 'jogando']")
                    return
            self.status = 2
            self.data_inicio = input("Digite a data que começou/voltou a jogar: ")
            self.horas_jogadas += int(input("Digite quantas horas foram jogadas: "))
            print("Status atualizado!")
        elif novo_status == 3:
            self.finalizarJogo(limite_horas)
        else:
            raise ValueError("[Status deve ser 1, 2 ou 3]")
            
    def finalizarJogo(self,limite_horas):
        if self.horas_jogadas < limite_horas:
            print(f"[Não é possível finalizar o jogo com menos de {limite_horas} horas jogadas]")
        else:
            self.avaliacao = int(input("Avalie o jogo, (1-10):"))
            self.status = 3
            self.data_termino = input("Digite a data estimada do término: ")
            print("Jogo finalizado!")
            
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