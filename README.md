# Playxel
## Descrição:
- Playxel é um catálogo de jogos digitais que tem a função de organizar, acompanhar e analisar o progresso dos seus jogos favoritos. O sistema permite cadastrar jogos, acompanhar status ("inativo","jogando" e "finalizado"), registar e atualizar horas jogadas, criar coleções personalizadas, gerar relatórios (como total de horas, média de avaliações e jogos mais jogados) e configurar suas preferências.

## Objetivo:
- O objetivo é oferecer uma forma simples e eficiente de gerenciar sua biblioteca pessoal de jogos, aplicando conceitos de programação orientada a objetos, herança, encapsulamento, regras de negócio configuráveis e atender os requisitos funcionais.

## Definição das classes:

### Class Jogo:
> A classe responsável por conter as informações de um jogo e modificar os seus objetos.
- Atributos: nome, gênero, plataforma, horas_jogadas, status, data_inicio, data_termino, ano_lançamento, avaliação, multiplayer.
- Métodos principais: atualizarHoras(), atualizarStatus(), finalizarJogo(), reiniciarJogo()

### Class JogoPC:
> Uma subclasse da classe pai "Jogo", agrupa os jogos de PC
- Atributos: herda os atributos da classe pai, launcher
- Métodos: herda todos os métodos da classe pai

### Class JogoConsole:
> Uma subclasse da classe pai "Jogo", agrupa os jogos de Console
- Atributos: herda os atributos da classe pai, console
- Métodos: herda todos os métodos da classe pai

### Class JogoMobile:
> Uma subclasse da classe pai "Jogo", agrupa os jogos Mobile
- Atributos: herda os atributos da classe pai, sistema
- Métodos: herda todos os métodos da classe pai
  
### Class Catalogo:
> Classe responsável por gerenciar todos os jogos cadastrados no sistema (filtros, ordenações e buscas).
- Atributos: jogos
- Métodos principais: adicionarJogo(), removerJogo(), listarNomes(), abrirJogo(), filtrarGenero(), filtrarPlataforma(), filtrarrStatus(), ordenarPorTempo(), ordenarTempoJogado(), ordenarLancamento().

### Class Colecao:
> Representa uma coleção nomeada de jogos criada pelo usuário (ex.: Favoritos).
- Atributos: nome, jogos
- Métodos principais: adicionarJogo(), removerJogo(), exibirJogos().

### Class ListaDeColecoes:
> Controla todas as coleções existentes no sistema, permitindo criar e remover coleções.
- Atributos: colecoes
- Métodos: criarColecao(), removerColecao(), abrirColecao(), listarColecoes(), gerarColecoes().

### Class Relatorio:
> Classe utilitária responsável por gerar estatísticas e relatórios sobre o catálogo de jogos.
- Atributos: horas_jogadas, avaliação, status
- Métodos: totalHoras(), mediaAvaliacoesFinalizados(), percentualPorStatus(), top5MaisJogados()

### Class Configuracoes:
> Gerencia as preferências do usuário (meta anual, plataforma principal, gêneros favoritos).
- Atributos: generos_favoritos, metas, plataforma_principal, limite_jogando, limite_horas.
- Métodos: carregar(), salvar(), menuConfiguracoes()

## Documentação completa:
> https://docs.google.com/document/d/1UeGcQkk62bEYJT1ucjH1O0DPqV4r0UdikPmub1u32a0/edit?usp=sharing

## Organização do projeto:
```
Playxel/
├── Playxel.py                     - Arquivo principal de execução do programa
├── colecoes.json                  - Arquivo que armazena as coleções criadas
├── configuracoes.json             - Arquivo que armazena as configurações do usuário
├── jogos.json                     - Aquivo que armazena os jogos cadastrados
|
├── Tests
|   ├── test_catalogo.py           - Arquivo que testa a classe catálogo
|   ├── test_colecao.py            - Arquivo que testa a classe coleção
|   ├── test_converter.py          - Arquivo que testa a interação entre o ojeto jogo e o dicionário
|   ├── test_jogo.py               - Arquivo que testa a classe jogo
|   └── test_subclasses.py         - Aquivo que testa as subclasses de jogo
|
└── README.md                      - Este arquivo
```
## Pré-requisitos:

- Python instalado

## Como executar:

1. Clone o repositório,

2. Execute o programa:
```bash
python Playxel.py
```
## Funcionalidades e restrições:
- Gerenciamento de jogos (criar, remover e atualizar sua progressão).
- O sistema não aceita determinados atributos na criação de jogos, se houver erro, não será armazenado.
- Forma de visualização dos jogos variadas, a partir dos filtros e ordenação.
- Configuração de gênero favorito, meta de jogos finalizados, sua plataforma principal, limite de jogos que você está jogando e limite de horas para finalizar jogo.
- Coleções criadas altomaticamente que armazena os seus jogos do seu gênero favorito, plataforma principal e os jogos multiplayer.
- Criação de coleções personalizadas, podendo adicionar e remover jogos.
- Relatórios gerais que mostra dados gerais dos seus jogos.

## Passo a passo:
1. No menu inicial escolha uma das opções, configure seu programa pela primeira vez, digite "4".

> <img width="743" height="175" alt="Captura de tela 2025-12-11 125016" src="https://github.com/user-attachments/assets/d331f385-d1a7-4275-9464-3598ad09defd" />

2. Configure o programa da maneira que desejar, escolhendo as opções de 1 a 5. Em seguida, digite "6" para voltar.

> <img width="709" height="283" alt="Captura de tela 2025-12-11 125213" src="https://github.com/user-attachments/assets/8039fdae-12e5-4616-8da0-119b94a74ef9" />

3. Após voltar ao menu principal digite "1", para acessar o catálogo. Nele você verá os jogos cadastrados e terá as opções para criar, remover e visualizar.

> <img width="909" height="401" alt="Captura de tela 2025-12-11 125809" src="https://github.com/user-attachments/assets/02d9e6e1-23f2-4607-9815-602204017922" />

4. Para filtrar ou ordenar a forma de visualizar os jogos, basta selecionar a forma que deseja.

> <img width="406" height="223" alt="Captura de tela 2025-12-11 125953" src="https://github.com/user-attachments/assets/bf6a8021-e7fd-48a0-962e-427c4f449ed3" />
> <img width="489" height="348" alt="Captura de tela 2025-12-11 130012" src="https://github.com/user-attachments/assets/5d54f11b-2897-4438-875f-12eb7694d426" />

5. Ao criar o jogo o sitema fará perguntas que variam dependendo do status e plataforma que escolher, lembre-se dos limites que você estabeleceu nas configurações.

> <img width="601" height="277" alt="Captura de tela 2025-12-11 131015" src="https://github.com/user-attachments/assets/7d72546a-40bf-48f1-ac5c-ee76ea8fa12e" />

6. Ao abrir um jogo, digite o nome do jogo cadastrado. Existe a possibilidade de ter o mesmo jogo em plataformas diferenetes, o sitema perguntará qual deseja abrir.

> <img width="903" height="461" alt="Captura de tela 2025-12-11 130324" src="https://github.com/user-attachments/assets/21a01851-30dd-40f1-8adc-0385abf74210" />

7. No jogo selecionado, você pode adicionar mais horas jogadas, atualizar o status(inativo, jogando, finalizado) ou reiniciar que reseta todo o seu progresso

8. Tenha certeza ao reiniciar ou remover um jogo, pois as alterações não podem ser desfeitas.

9. Volte até o menu inicial e digite "2", para acessar as sua coleções.

> <img width="795" height="163" alt="Captura de tela 2025-12-11 132051" src="https://github.com/user-attachments/assets/d8295058-68e8-41b7-8d38-14488dea27a3" />

10.Observe que algumas coleções já foram criadas automaticamente, elas recebem automaticamente os jogos que estão relacionados. Se quiser remover, basta digitar "2". Digite "3" para abrir uma coleção, vizualizar, adicionar ou remover seus jogos .

> <img width="401" height="275" alt="Captura de tela 2025-12-11 132149" src="https://github.com/user-attachments/assets/a9028a35-0d2c-4f3c-bb07-8b7c7b33a2d4" />
> <img width="537" height="263" alt="Captura de tela 2025-12-11 132248" src="https://github.com/user-attachments/assets/de77a1a1-fb19-4afe-8526-c417fb6404db" />

11. Volte e crie uma coleção com o nome que deseja, para adicionar jogos nela, basta abri-lá e adicionar os jogos cadastrados que deseja e remover quando quiser

> <img width="822" height="377" alt="Captura de tela 2025-12-11 132822" src="https://github.com/user-attachments/assets/41b44728-ca6c-491d-9cce-3b8a22d4adcf" />

12. Volte ao menu principal novamente e digite "3" para receber um relatório. Você receberá informações interessantes que variam em relação aos seus jogos.
    
> <img width="974" height="462" alt="Captura de tela 2025-12-11 133621" src="https://github.com/user-attachments/assets/36ed01bb-2ec5-49d8-8fa8-d2df17efb182" />

13. Detalhe interessante! Se os seus jogos finalizados estiverem abaixo da sua meta, o sistema irá te notificar sobre isso no menu principal.

> <img width="947" height="203" alt="Captura de tela 2025-12-11 133826" src="https://github.com/user-attachments/assets/e09d7a1a-6f36-4e59-abbd-07c89f759dcb" />

14. Observações importantes. Sempre que você digitar alguma informação errada, o sistema irá notificar o seu erro. Digite sempre o que se pede e da maneira correta.
## Execução dos testes:
1. No terminal verifique se o python está corretamente instalado:
```bash
python --version
```
ou
```bash
py --version
```
2. Em seguida instale o pytest:
```bash
py -m pip install --upgrade pip
py -m pip install pytest
```
3. Por último, execute os testes:
```bash
py -m pytest
```
<img width="1623" height="343" alt="Captura de tela 2025-12-11 140146" src="https://github.com/user-attachments/assets/90ef7b9c-60f2-4eaa-8582-eb4684917d94" />

## Decisões importantes:
- Com a simplicidade do programa em relação ao seu objetivo, escolhi desenvolver a interface em CLI, já que nenhuma funcionalidade seria deixado de lado e não seria difícil executar. Futuramente, pretendo adicionar uma API.
- No desenvolvimento do código, segui rigorosamente as regras de negócio. Exemplo: não deixando o status "finalizado" ,se as horas forem menores que as horas necessária, seja no momento do cadastro ou na atualização.
- Dei liberdade ao usuário em alguns aspectos, comao cadastrar um jogo já finalizado (seguindo as horas necessárias) e definir a data de início e de término da maneira como quiser, já que o usúario pode não lembrar a data exata.
- A criação de coleções automáticas são coleções que o usuário provavelmente iria criar um dia, criar e atualiza-las automaticamente deixa o sistema mais valorizado

