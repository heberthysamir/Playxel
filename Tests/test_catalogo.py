from Playxel import Catalogo, Jogo

def criar_catalogo_exemplo():
    c = Catalogo()
    c.jogos = [
        Jogo("A", "RPG", "pc", 10, 1, "", "", 2005, 8, False),
        Jogo("B", "FPS", "pc", 20, 1, "", "", 2010, 9, True),
        Jogo("C", "RPG", "console", 5, 1, "", "", 2001, 7, False)
    ]
    return c

def test_ordenar_lancamento_crescente():
    c = criar_catalogo_exemplo()
    c.ordenarLancamento(False)
    assert [j.ano_lancamento for j in c.jogos] == [2001, 2005, 2010]

def test_ordenar_lancamento_decrescente():
    c = criar_catalogo_exemplo()
    c.ordenarLancamento(True)
    assert [j.ano_lancamento for j in c.jogos] == [2010, 2005, 2001]

def test_filtrar_genero():
    c = criar_catalogo_exemplo()
    c.jogos_filtrados = [j for j in c.jogos if j.genero == "RPG"]
    assert len(c.jogos_filtrados) == 2
