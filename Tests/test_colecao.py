from Playxel import Colecao, Jogo

def test_adicionar_jogo_na_colecao():
    jogo = Jogo(
        "Terraria", "Ação", "pc",
        12, 3,
        "10/02/2024", "20/02/2024",
        2011, 9
    )

    colecao = Colecao("Favoritos")
    colecao.jogos.append(jogo)

    assert len(colecao.jogos) == 1
    assert colecao.jogos[0].nome == "Terraria"


def test_exibir_jogos_vazia():
    colecao = Colecao("Vazia")
    assert colecao.jogos == []
