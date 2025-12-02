import pytest
from Playxel import Colecao, JogoPC

def test_criacao_colecao():
    c = Colecao("Favoritos")
    assert c.nome == "Favoritos"
    assert len(c.jogos) == 0

def test_adicionar_jogo_direto():
    c = Colecao("Coleção X")
    jogo = JogoPC("Steam", "Jogo1", "Ação", "pc", 0, 1, "Não", "Não", 2020, 5, "não")

    c.jogos.append(jogo)

    assert len(c.jogos) == 1
    assert c.jogos[0].nome == "Jogo1"

def test_exibirJogos(capsys):
    c = Colecao("Teste")
    c.jogos.append(JogoPC("Steam", "Halo", "FPS", "pc", 10, 1, "Não", "Não", 2021, 8, "não"))

    c.exibirJogos()
    saida = capsys.readouterr().out

    assert "Halo" in saida
