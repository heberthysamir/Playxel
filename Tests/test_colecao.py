from colecao import Colecao
from jogo import Jogo

def test_criar_colecao_e_adicionar():
    j1 = Jogo("Skyrim", "RPG", "pc", 100, 3, "", "", 2011, 10, False)
    col = Colecao("Favoritos", [])
    col.jogos.append(j1)

    assert len(col.jogos) == 1
    assert col.jogos[0].nome == "Skyrim"

def test_str_colecao():
    col = Colecao("Multiplayer")
    assert str(col) == "Multiplayer"
