import json

class Colecao:
    def __init__(self, nome, jogos = None):
        self.nome = nome
        self.jogos = jogos if jogos is not None else []

    def __str__(self):
        return f"{self.nome}"
    
    def dicionario(self):
        return {
            "nome": self.nome,
            "jogos": [
                {
                    "nome": j.nome,
                    "plataforma": j.plataforma
                }
                for j in self.jogos
            ]
        }

    def adicionarJogo(self, catalogo, lista_colecoes):
        while True:
            nome = input("Digite o nome do jogo que quer adicionar: ").strip()
            if nome == "":
                return
            encontrados = [j for j in catalogo.jogos if j.nome.lower() == nome.lower()]
            if len(encontrados) == 0:
                print("\n[Jogo não encontrado no catálogo.]\n")
                continue
            if len(encontrados) == 1:
                jogo = encontrados[0]
                if jogo in self.jogos:
                    print("\n[Esse jogo já está na coleção.]\n")
                    return
                self.jogos.append(jogo)
                lista_colecoes.salvar()
                print("\n[Jogo adicionado à coleção!]\n")
                return
            print(f"\nForam encontrados {len(encontrados)} jogos com o nome '{nome}':\n")
            for i, jogo in enumerate(encontrados, start=1):
                print(f"{i}. {jogo.nome} - Plataforma: {jogo.plataforma}")
            while True:
                try:
                    escolha = int(input("\nEscolha o número do jogo que deseja adicionar: "))
                    if 1 <= escolha <= len(encontrados):
                        jogo_escolhido = encontrados[escolha - 1]
                        if jogo_escolhido in self.jogos:
                            print("\n[Esse jogo já está na coleção.]\n")
                            return
                        self.jogos.append(jogo_escolhido)
                        lista_colecoes.salvar()
                        print("\n[Jogo adicionado à coleção!]\n")
                        return
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")


    def removerJogo(self, lista_colecoes):
        while True:
            nome = input("Digite o nome do jogo que deseja remover: ").strip()
            if nome == "":
                return
            encontrados = [j for j in self.jogos if j.nome.lower() == nome.lower()]
            if len(encontrados) == 0:
                print("\n[Jogo não encontrado na coleção. Tente novamente!]\n")
                continue
            if len(encontrados) == 1:
                self.jogos.remove(encontrados[0])
                lista_colecoes.salvar()
                print("\n[Jogo removido com sucesso!]\n")
                return
            print(f"\nForam encontrados {len(encontrados)} jogos com o nome '{nome}':\n")
            for i, jogo in enumerate(encontrados, start=1):
                print(f"{i}. {jogo.nome} - Plataforma: {jogo.plataforma}")
            while True:
                try:
                    escolha = int(input("\nEscolha o número do jogo a remover: "))
                    if 1 <= escolha <= len(encontrados):
                        jogo_escolhido = encontrados[escolha - 1]
                        self.jogos.remove(jogo_escolhido)
                        lista_colecoes.salvar()
                        print("\n[Jogo removido com sucesso!]")
                        return
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Digite um número válido.")

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

        with open("data/colecoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)


    def carregar(self, catalogo):
        try:
            with open("data/colecoes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            self.colecaos = []
            for item in dados:
                nova = Colecao(item["nome"])
                for jogo_salvo in item["jogos"]:
                    for j in catalogo.jogos:
                        if (
                            j.nome == jogo_salvo["nome"] and
                            j.plataforma == jogo_salvo["plataforma"]
                        ):
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
        self.colecaos = [
            c for c in self.colecaos
            if not (
                c.nome.startswith("Gênero") or
                c.nome.startswith("Plataforma") or
                c.nome == "Jogos Multiplayer"
            )
        ]

        genero = configuracoes.genero_favorito
        colecao_genero = Colecao(f"Gênero {genero}")
        colecao_genero.jogos = [
            j for j in catalogo.jogos if j.genero == genero
        ]
        self.colecaos.append(colecao_genero)

        plataforma = configuracoes.plataforma_principal
        colecao_plataforma = Colecao(f"Plataforma {plataforma}")
        colecao_plataforma.jogos = [
            j for j in catalogo.jogos if j.plataforma == plataforma
        ]
        self.colecaos.append(colecao_plataforma)

        colecao_multi = Colecao("Jogos Multiplayer")
        colecao_multi.jogos = [
            j for j in catalogo.jogos if j.multiplayer
        ]
        self.colecaos.append(colecao_multi)

