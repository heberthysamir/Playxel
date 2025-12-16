from jogo import JogoPC, JogoConsole, JogoMobile

def test_jogo_pc_extra():
    j = JogoPC("Steam", "CS2", "FPS", "pc", 10, 1, "", "", 2023, 9, False)
    assert j.launcher == "Steam"

def test_jogo_console_extra():
    j = JogoConsole("PS5", "God of War", "Ação", "console", 20, 1, "", "", 2022, 10, False)
    assert j.console == "PS5"

def test_jogo_mobile_extra():
    j = JogoMobile("Android", "Clash Royale", "Estrategia", "mobile", 5, 1, "", "", 2016, 8, True)
    assert j.sistema == "Android"
