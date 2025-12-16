import pytest
from jogo import Jogo

def test_jogo_criacao_basica():
    j = Jogo("Halo", "FPS", "console", 10, 1, "01/01/2020", "", 2001, 8.5, True)
    assert j.nome == "Halo"
    assert j.genero == "FPS"
    assert j.plataforma == "console"
    assert j.horas_jogadas == 10
    assert j.status == "inativo"
    assert j.ano_lancamento == 2001
    assert j.avaliacao == 8.5
    assert j.multiplayer is True

def test_jogo_nome_invalido():
    with pytest.raises(ValueError):
        Jogo("", "RPG", "pc", 5, 1, "", "", 2010, 7, False)

def test_jogo_avaliacao_invalida():
    with pytest.raises(ValueError):
        Jogo("Zelda", "Aventura", "console", 5, 1, "", "", 2017, 15, False)

def test_eq_mesmo_jogo_mesma_plataforma():
    j1 = Jogo("Minecraft", "Sandbox", "pc", 10, 1, "", "", 2010, 9, True)
    j2 = Jogo("minecraft", "Sandbox", "pc", 5, 1, "", "", 2011, 9, True)
    assert j1 == j2

def test_eq_jogos_diferentes():
    j1 = Jogo("Minecraft", "Sandbox", "pc", 10, 1, "", "", 2010, 9, True)
    j2 = Jogo("Terraria", "Sandbox", "pc", 5, 1, "", "", 2011, 9, True)
    assert j1 != j2

def test_str_retorno():
    j = Jogo("Halo", "FPS", "console", 10, 1, "", "", 2001, 8.5, True)
    assert "Halo" in str(j) and "2001" in str(j)
