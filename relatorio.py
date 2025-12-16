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
        return f"Inativo: {sum(j.status == "inativo" for j in self.jogos)*100/len(self.jogos):.2f}%\n Jogando: {sum(j.status == "jogando" for j in self.jogos)*100/len(self.jogos):.2f}%\n Finalizado: {sum(j.status == "finalizado" for j in self.jogos)*100/len(self.jogos):.2f}%"
        
    def top5Jogos(self):
        if not self.jogos:
            print("\n[Nenhum jogo cadastrado!]")
            return
        top5 = sorted(self.jogos, key=lambda j: j.horas_jogadas, reverse=True)[:5]
        print("Top 5 jogos mais jogados:")
        for i, jogo in enumerate(top5, start=1):
            print(f"{i}. {jogo.nome} - {jogo.horas_jogadas} horas")