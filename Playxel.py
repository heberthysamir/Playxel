from jogo import Jogo
from catalogo import Catalogo
from colecao import Colecao, ListaDeColecoes
from configuracoes import Configuracoes
from relatorio import Relatorio

catalogo = Catalogo()
catalogo.carregar()
suasColecoes = ListaDeColecoes()
configuracoes = Configuracoes()
configuracoes.carregar()
suasColecoes.carregar(catalogo)
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
                    jogo = catalogo.adicionarJogo(configuracoes.limite_jogando)
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
                            jogo.atualizarStatus(limite_jogando=configuracoes.limite_jogando,jogos=catalogo.jogos,limite_horas=configuracoes.limite_horas)
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
            configuracoes.menuConfiguracoes(catalogo)
        elif user == 2:
            while True:
                suasColecoes.listarColecoes()
                suasColecoes.gerarColecoes(catalogo, configuracoes)
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
                            colecao.adicionarJogo(catalogo,suasColecoes)
                        elif user == 2:
                            colecao.removerJogo(suasColecoes)
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