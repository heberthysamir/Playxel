import pytest
from Playxel import Jogo, JogoPC, JogoConsole, JogoMobile, jogo_from_dict

def test_criacao_jogo_basico():
    jogo = Jogo("Teste", "Ação", "pc", 10, 1, "01/01/2024", "Não informada", 2020, 8, "não")
    assert jogo.nome == "Teste"
    assert jogo.genero == "Ação"
    assert jogo.status == "inativo"
    assert jogo.horas_jogadas == 10

def test_subclasses_pc_console_mobile():
    pc = JogoPC("Steam", "Jogo PC", "Ação", "pc", 10, 1, "01/01", "Não", 2020, 8, "não")
    console = JogoConsole("PS5", "Jogo Console", "RPG", "console", 5, 2, "01/02", "Não", 2018, 7, "sim")
    mobile = JogoMobile("Android", "Jogo Mobile", "Puzzle", "mobile", 3, 1, "01/03", "Não", 2019, 6, "não")

    assert pc.launcher == "Steam"
    assert console.console == "PS5"
    assert mobile.sistema == "Android"

def test_dicionario_e_reconstrucao():
    original = JogoPC("Steam", "Elden Ring", "Ação", "pc", 50, 3, "01/01", "01/03", 2022, 10, "não")
    d = original.dicionario()

    novo = jogo_from_dict(d)

    assert isinstance(novo, JogoPC)
    assert novo.nome == "Elden Ring"
    assert novo.launcher == "Steam"
    assert novo.status == "finalizado"
