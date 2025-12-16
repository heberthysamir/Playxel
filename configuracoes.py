import json

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
        with open("data/configuracoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.dicionario(), arquivo, indent=4, ensure_ascii=False)

    def carregar(self):
        try:
            with open("data/configuracoes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                self.genero_favorito = dados.get("genero_favorito", self.genero_favorito)
                self.metas = dados.get("meta", self.metas)
                self.plataforma_principal = dados.get("plataforma_principal", self.plataforma_principal)
                self.limite_jogando = dados.get("limite_jogando", self.limite_jogando)
                self.limite_horas = dados.get("limite_horas", self.limite_horas)

        except FileNotFoundError:
             self.salvar()  

    def menuConfiguracoes(self, suasColecoes):
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
