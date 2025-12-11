import json
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

    def atualizarStatus(self):
        novo_status = int(input("Qual é o novo status? (1. inativo, 2. jogando, 3. finalizado): "))
        if novo_status == 1:
            self.status = 1
            print("Status atualizado!",self.status)
        elif novo_status == 2:
            if configuracoes.limite_jogando not in (None, "", 0):
                contJogando = sum(1 for j in catalogo.jogos if j.status == "jogando")
                if contJogando >= int(configuracoes.limite_jogando):
                    print(f"\n[Você atingiu o limite de ({configuracoes.limite_jogando}) jogos com status 'jogando']")
                    return
            self.status = 2
            self.data_inicio = input("Digite a data que começou/voltou a jogar: ")
            self.horas_jogadas += int(input("Digite quantas horas foram jogadas: "))
            print("Status atualizado!")
        elif novo_status == 3:
            self.finalizarJogo()
        else:
            raise ValueError("[Status deve ser 1, 2 ou 3]")
            
    def finalizarJogo(self):
        if self.horas_jogadas < configuracoes.limite_horas:
            print(f"[Não é possível finalizar o jogo com menos de {configuracoes.limite_horas} horas jogadas]")
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

class Catalogo:
    def __init__(self):
        self.jogos = []
        self.jogos_filtrados = None
    
    def adicionarJogo(self):
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
                    limite = configuracoes.limite_jogando
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

class Colecao:
    def __init__(self, nome, jogos = None):
        self.nome = nome
        self.jogos = jogos if jogos is not None else []

    def __str__(self):
        return f"{self.nome}"
    
    def dicionario(self):
        return {
            "nome": self.nome,
            "jogos": [j.nome for j in self.jogos]
        }

    def adicionarJogo(self):
        jogo_nome = input("Digite o nome do jogo que quer adicionar: ")
        for j in catalogo.jogos:
            if j.nome == jogo_nome:
                self.jogos.append(j)
                suasColecoes.salvar()
                print("Jogo adicionado.")
                return 
        print("Jogo não encontrado!")

    def removerJogo(self):
        nome = input("Digite o nome do jogo que deseja remover: ")
        for j in catalogo.jogos:
            if j.nome == nome:
                self.jogos.remove(j)
                suasColecoes.salvar()
                print("Jogo deletado")
                return
        print("Jogo não encontrado.")

    def exibirJogos(self):
        if not self.jogos:
            print("Nenhum jogo na coleção.")
            return

        for jogo in self.jogos:
            print(jogo)

class ListaDeColecoes:
    def __init__(self):
        self.colecaos = []
    
    def salvar(self):
        lista = [c.dicionario() for c in self.colecaos]

        with open("colecoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)


    def carregar(self, catalogo):
        try:
            with open("colecoes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            self.colecaos = []
            for item in dados:
                nova = Colecao(item["nome"])
                for nome_jogo in item["jogos"]:
                    for j in catalogo.jogos:
                        if j.nome == nome_jogo:
                            nova.jogos.append(j)
                self.colecaos.append(nova)
        except FileNotFoundError:
            self.salvar()

    def criarColecao(self):
        nome = input("Digite o nome da coleção: ")
        for c in self.colecaos:
            if c.nome == nome:
                print("Já existe uma coleção com esse nome.")
                return
        nova = Colecao(nome, [])
        self.colecaos.append(nova)
        self.salvar()
        print("Coleção criada!")

    def removerColecao(self):
        nome = input("Digite o nome da coleção que deseja remover: ")
        for c in self.colecaos:
            if c.nome == nome:
                self.colecaos.remove(c)
                self.salvar()
                print("Coleção deletado")
                return
        print("Coleção não encontrado.")

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
    
    def gerarColecoes(self, catalogo, configuracoes):
        self.colecaos = [c for c in self.colecaos if not (
            c.nome.startswith("Gênero") or 
            c.nome.startswith("Plataforma") or 
            c.nome == "Jogos Multiplayer"
        )]
        genero = configuracoes.genero_favorito
        colecao_genero = Colecao(f"Gênero {genero}")
        colecao_genero.jogos = [j for j in catalogo.jogos if j.genero == genero]
        self.colecaos.append(colecao_genero)

        plataforma = configuracoes.plataforma_principal
        colecao_plataforma = Colecao(f"Plataforma {plataforma}")
        colecao_plataforma.jogos = [j for j in catalogo.jogos if j.plataforma == plataforma]
        self.colecaos.append(colecao_plataforma)

        colecao_multi = Colecao("Jogos Multiplayer")
        colecao_multi.jogos = [j for j in catalogo.jogos if j.multiplayer]
        self.colecaos.append(colecao_multi)
        self.salvar()

class Configuracoes:
    def __init__(self, genero_favorito = "Não definido", metas = 0, plataforma_principal = "Não definida", limite_jogando = None, limite_horas = 0):
        self.genero_favorito = genero_favorito
        self.metas = metas
        self.plataforma_principal = plataforma_principal
        self.limite_jogando = limite_jogando
        self.limite_horas = limite_horas

    def __str__(self):
        return (
            f"Configurações:\n"
            f"- Gênero favorito: {self.genero_favorito}\n"
            f"- Metas de Jogos para finalizar: {self.metas}\n"
            f"- Plataforma principal: {self.plataforma_principal}\n"
            f"- Limite de jogos 'jogando': {self.limite_jogando}\n"
            f"- Limite de horas para finalizar jogo: {self.limite_horas}"
        )
    
    def dicionario(self):
        return {
            "genero_favorito": self.genero_favorito,
            "meta": self.metas,
            "plataforma_principal": self.plataforma_principal,
            "limite_jogando": self.limite_jogando,
            "limite_horas": self.limite_horas
        }

    def salvar(self):
        with open("configuracoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.dicionario(), arquivo, indent=4, ensure_ascii=False)

    def carregar(self):
        try:
            with open("configuracoes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                self.genero_favorito = dados.get("genero_favorito", self.genero_favorito)
                self.metas = dados.get("meta", self.metas)
                self.plataforma_principal = dados.get("plataforma_principal", self.plataforma_principal)
                self.limite_jogando = dados.get("limite_jogando", self.limite_jogando)
                self.limite_horas = dados.get("limite_horas", self.limite_horas)

        except FileNotFoundError:
             self.salvar()  

    def menuConfiguracoes(self):
        while True:
            print("\nConfigurações:")
            print(self)
            print("\nOpções:\n1.Alterar gênero favorito\n2.Alterar meta de jogos finalizados\n3.Alterar plataforma principal\n4.Alterar limite de jogos\n5.Alterar limite de horas para finalizar um jogo\n6.Voltar")

            opc = input("Digite uma opção: ")

            if opc == "1":
                self.genero_favorito = input("Novo gênero favorito: ")
                self.salvar()
                suasColecoes.salvar()
            elif opc == "2":
                self.metas = int(input("Digite suas metas: "))
                self.salvar()
            elif opc == "3":
                self.plataforma_principal = input("Plataforma principal (pc, mobile, console): ")
                self.salvar()
                suasColecoes.salvar()
            elif opc == "4":
                self.limite_jogando = int(input("Limite de jogos com status'jogando': "))
                self.salvar()
            elif opc == "5":
                self.limite_horas = int(input("Limite de horas para finalizar jogo: "))
                self.salvar()
            elif opc == "6":
                break
            else:
                print("Opção inválida!")

class Relatorio:
    def __init__(self,jogos):
        self.jogos = jogos

    def calcularHorasTotais(self):
        return sum(j.horas_jogadas for j in self.jogos)
    
    def calcularJogos(self):
        return len(self.jogos)
    
    def calcularAvaliacoes(self):
        return sum(j.avaliacao for j in self.jogos) / len(self.jogos)
    
    def calcularPercentualStatus(self):
        return f"Inativo: {sum(j.status == "inativo" for j in self.jogos)*100/len(self.jogos)}%\n Jogando: {sum(j.status == "jogando" for j in self.jogos)*100/len(self.jogos)}%\n Finalizado: {sum(j.status == "finalizado" for j in self.jogos)*100/len(self.jogos)}%"
        
    def top5Jogos(self):
        if not self.jogos:
            print("\n[Nenhum jogo cadastrado!]")
            return
        top5 = sorted(self.jogos, key=lambda j: j.horas_jogadas, reverse=True)[:5]
        print("Top 5 jogos mais jogados:")
        for i, jogo in enumerate(top5, start=1):
            print(f"{i}. {jogo.nome} - {jogo.horas_jogadas} horas")


catalogo = Catalogo()
catalogo.carregar()
suasColecoes = ListaDeColecoes()
configuracoes = Configuracoes()
configuracoes.carregar()
suasColecoes.gerarColecoes(catalogo, configuracoes)

if __name__ == "__main__":
    while True:
        print("\n- Opções: \n1.Catálogo\n2.Suas coleções\n3.Relatório\n4.Configurações\n5.Sair")
        cont = sum(1 for j in catalogo.jogos if j.status == "finalizado")
        if cont < configuracoes.metas:
            print("\n[Seus jogos finalizados estão abaixo de sua meta anual!]")
        user = int(input("Digite uma opção: "))
        if user == 5:
            break 
        elif user == 1:
            while True:
                catalogo.listarNomes()
                print("\n-Opções do catálogo:\n1.Adicionar Jogo\n2.Remover Jogo\n3.Abrir Jogo\n4.Filtrar Jogos\n5.Ordenar Jogos\n6.Voltar")
                user = int(input("\nDigite uma opção do catálogo: "))
                if user == 1:
                    jogo = catalogo.adicionarJogo()
                elif user == 2:
                    jogo = catalogo.removerJogo()
                elif user == 3:
                    jogo = catalogo.abrirJogo()
                    if jogo is None:
                        break
                    if jogo is False:
                        continue 
                    while True:
                        if jogo is None:
                            continue 
                        print(f"\nJogo: {jogo.nome} ({jogo.genero}) - {jogo.plataforma}\n Status: {jogo.status}\n Horas jogadas: {jogo.horas_jogadas}\n Data de início: {jogo.data_inicio}\n Data de término: {jogo.data_termino}")
                        if jogo.avaliacao != 0:
                            print(" Avaliação(1-10): ",jogo.avaliacao)
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
                elif user == 4:
                    while True:
                        print("\n-Como deseja filtrar:\n1.Gênero\n2.Plataforma\n3.Status\n4.Limpar\n5.Voltar")
                        user = int(input("\nDigite uma opção: "))
                        if user == 1:
                            catalogo.filtrarGenero()
                            break
                        elif user == 2:
                            catalogo.filtrarPlataforma()
                            break
                        elif user == 3:
                            catalogo.filtrarStatus()
                            break
                        elif user == 4:
                            catalogo.limparFiltro()
                            break
                        elif user == 5:
                            break
                elif user == 5:
                    while True:
                        print("\n-Como deseja ordenar:\n1.Lançamento recente\n2.Lançamento antigo\n3.Mais jogados\n4.Menos jogados\n5.Voltar")
                        user = int(input("\nDigite uma opção: "))
                        if user == 1:
                            catalogo.ordenarLancamento(True)
                            break
                        elif user == 2:
                            catalogo.ordenarLancamento(False)
                            break
                        elif user == 3:
                            catalogo.ordenarTempoJogado(True)
                            break
                        elif user == 4:
                            catalogo.ordenarTempoJogado(False)
                            break
                        elif user == 5:
                            break
                elif user == 6:
                    break
        elif user == 4:
            configuracoes.menuConfiguracoes()
        elif user == 2:
            while True:
                suasColecoes.gerarColecoes(catalogo, configuracoes)
                suasColecoes.listarColecoes()
                print("\n-Opções das Coleções:\n1.Criar coleção\n2.Remover coleção\n3.Abrir coleção\n4.Voltar")
                user = int(input("\nDigite uma opção da coleção: "))
                if user == 1:
                    suasColecoes.criarColecao()
                elif user == 2:
                    suasColecoes.removerColecao()
                elif user == 3:
                    colecao = suasColecoes.abrirColecao()
                    if colecao is None:
                        continue 
                    while True:
                        print(f"\nColeção: {colecao.nome}")
                        colecao.exibirJogos()
                        print("\n1.Adicionar Jogo\n2.Remover Jogo\n3.Voltar")
                        user = int(input("Digite uma opção da coleção: "))
                        if user == 1:
                            colecao.adicionarJogo()
                        elif user == 2:
                            colecao.removerJogo()
                        elif user == 3:
                            break
                elif user == 4:
                    break
        elif user == 3:
            rel = Relatorio(catalogo.jogos)
            print("\nHoras totais:", rel.calcularHorasTotais())
            print("Quantidade de jogos:", rel.calcularJogos())
            print("Média de avaliações:", rel.calcularAvaliacoes())
            print("Porcentagens de status:\n", rel.calcularPercentualStatus())
            rel.top5Jogos()