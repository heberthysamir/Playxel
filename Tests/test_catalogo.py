from Playxel import Catalogo, Jogo

def test_adicionar_jogo_manual():
    c = Catalogo()

    jogo = Jogo(
        "Stardew",
        "RPG",
        "pc",
        5,
        1,
        "01/01/2024",
        None,
        2016,
        None
    )

    c.jogos.append(jogo)

    assert len(c.jogos) == 1
    assert c.jogos[0].nome == "Stardew"
