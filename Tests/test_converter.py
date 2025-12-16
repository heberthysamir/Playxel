from jogo import jogo_from_dict, JogoPC

def test_converter_pc():
    data = {
        "tipo": "JogoPC",
        "extra": "Steam",
        "nome": "Portal",
        "genero": "Puzzle",
        "plataforma": "pc",
        "horas_jogadas": 10,
        "status": "jogando",
        "data_inicio": "01/01/2024",
        "data_termino": "",
        "ano_lancamento": 2007,
        "avaliacao": 9,
        "multiplayer": False
    }

    j = jogo_from_dict(data)

    assert isinstance(j, JogoPC)
    assert j.launcher == "Steam"
    assert j.nome == "Portal"
    assert j.status == "jogando"
