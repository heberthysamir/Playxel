import pytest
import json
import os
from Playxel import Catalogo, jogo_from_dict, JogoPC

def test_salvar_e_carregar(tmp_path):
    caminho = tmp_path / "jogos.json"

    c = Catalogo()
    c.jogos.append(JogoPC("Steam", "Jogo1", "Ação", "pc", 5, 1, "01/01", "Não", 2020, 7, "não"))

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump([c.jogos[0].dicionario()], f, indent=4, ensure_ascii=False)

    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = json.load(f)
        jogo = jogo_from_dict(conteudo[0])

    assert jogo.nome == "Jogo1"
    assert jogo.status == "inativo"

def test_listarNomes_sem_jogos(capsys):
    c = Catalogo()
    c.listarNomes()
    saida = capsys.readouterr().out
    assert "Nenhum jogo cadastrado" in saida

def test_remover_jogo(monkeypatch, capsys):
    c = Catalogo()
    c.jogos = [
        JogoPC("Steam", "Jogo1", "Ação", "pc", 5, 1, "01/01", "Não", 2020, 7, "não"),
    ]

    monkeypatch.setattr("builtins.input", lambda _: "Jogo1")
    c.removerJogo()

    assert len(c.jogos) == 0
