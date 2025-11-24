# Playxel
## Descrição:
> Playxel é um catálogo de jogos digitais que tem a função de organizar, acompanhar e analisar o progresso dos seus jogos favoritos. O sistema permite cadastrar jogos, acompanhar status ("não jogado","jogando" e "finalizado"), registar e atualizar horas jogadas, criar coleções personalizadas e gerar relatórios como total de horas, média de avaliações e jogos mais jogados.

## Objetivo:
> O objetivo é oferecer uma forma simples e eficiente de gerenciar sua biblioteca pessoal de jogos, aplicando conceitos de programação orientada a objetos, herança, encapsulamento, regras de negócio configuráveis e atender os requisitos funciionais.

## Documento de requisitos:
> https://docs.google.com/document/d/1UeGcQkk62bEYJT1ucjH1O0DPqV4r0UdikPmub1u32a0/edit?usp=sharing

## Definição das classes:

### Class Jogo:
> A classe responsável por conter as informações de um jogo e modificar os seus objetos.
- Atributos: nome, gênero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano_lançamento, avaliação.
- Métodos: atualizarHoras(), atualizarStatus(), finalizarJogo(), reiniciarJogo()

### Class JogoPC:
> A uma subclasse da classe pai "Jogo"
- Atributos: herda os atributos da classe pai
- Métodos: herda os métodos da classe pai
  
### Class Catalogo:
> Classe responsável por gerenciar todos os jogos cadastrados no sistema (filtros, ordenações e buscas).
- Atributos: jogos
- Métodos: adicionarJogo(), removerJogo(), buscarPorTitulo(), filtrarPorGenero(), filtrarPorPlataforma(), filtrarPorStatus(), filtrarPorNotaMinima(), ordenarPorTempo(), ordenarPorAvaliacao(), ordenarPorAno()

### Class Colecao:
> Representa uma coleção nomeada de jogos criada pelo usuário (ex.: Favoritos).
- Atributos: nome, jogos
- Métodos: adicionarJogo(), removerJogo(), listarJogos()

### Class ListaDeColecoes:
> Controla todas as coleções existentes no sistema, permitindo criar e remover coleções.
- Atributos: colecoes
- Métodos: criarColecao(), removerColecao(), obterColecao()

### Class Relatorio:
> Classe utilitária responsável por gerar estatísticas e relatórios sobre o catálogo de jogos.
- Atributos: horas_jogadas, avaliação, status
- Métodos: totalHoras(), mediaAvaliacoesFinalizados(), percentualPorStatus(), top5MaisJogados()

### Class Configuracoes:
> Gerencia as preferências do usuário (meta anual, plataforma principal, gêneros favoritos).
- Atributos: generos_favoritos, meta_anual, plataforma_principal
- Métodos: carregar(), atualizarConfiguracao(), SalvarAlteracao()
