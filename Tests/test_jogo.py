import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Playxel import Jogo, JogoPC, JogoConsole, JogoMobile
from datetime import datetime

def test_criacao_jogo_valido():
    jogo = Jogo(
        nome="Minecraft",
        genero="Sandbox",
        plataforma="pc",
        horas_jogadas=10.5,
        status=1,
        data_inicio="10/01/2024",
        data_termino=None,
        ano_lancamento="2011",
        avaliacao=None
    )

    assert jogo.nome == "Minecraft"
    assert jogo.genero == "Sandbox"
    assert jogo._status == "não iniciado"
    assert jogo.horas_jogadas == 10.5
    assert isinstance(jogo.data_inicio, datetime)
    assert jogo.data_termino is None


def test_nome_vazio_deve_gerar_erro():
    import pytest
    with pytest.raises(ValueError):
        Jogo("", "Ação", "pc", 10, 1, "10/01/2024", None, 2020, None)


def test_status_convertido_para_texto():
    jogo = Jogo(
        nome="FIFA",
        genero="Esporte",
        plataforma="console",
        horas_jogadas=5,
        status=2,
        data_inicio="01/02/2024",
        data_termino=None,
        ano_lancamento=2023,
        avaliacao=None
    )
    assert jogo.status == "jogando"


def test_avaliacao_inicial_none():
    jogo = Jogo(
        "LOL", "MOBA", "pc",
        0, 1,
        "01/01/2024",
        None,
        2009,
        None
    )
    assert jogo.avaliacao is None


def test_avaliacao_valida():
    jogo = Jogo(
        "GTA V", "Ação", "console",
        20, 3,
        "10/10/2020",
        "20/10/2020",
        2013,
        9
    )
    assert jogo.avaliacao == 9


def test_avaliacao_invalida():
    import pytest
    with pytest.raises(ValueError):
        Jogo("GTA", "Ação", "console", 10, 1, "10/10/2020", None, 2013, 15)
