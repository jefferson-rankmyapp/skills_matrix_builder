# People.AI - Assistente de Matriz de Habilidades
Este projeto é uma aplicação web interativa desenvolvida com Streamlit para auxiliar na construção de uma matriz de habilidades para qualquer cargo. O aplicativo guia o usuário passo a passo, desde a definição do cargo, passando pela escolha de hard skills, definição de objetivos para cada nível e mapeamento de atividades típicas.

## Funcionalidades
- Entrada interativa para definição do cargo e contexto.
- Seleção e customização das hard skills.
- Definição de objetivos por nível (Assistente, Júnior, Pleno, Sênior, Especialista).
- Mapeamento de 4 atividades típicas para cada nível de cada hard skill.
- Revisão e exportação da matriz final.

## Como executar
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/skills_matrix_builder.git
    ```
2. Acesse a pasta do projeto
    ```bash
    cd skills_matrix_builder
    ```
3. Instale as dependências
    ```bash
    pip install -r requirements.txt
    ```
4. Crie um arquivo .env na raiz do projeto (veja o exemplo no arquivo .env.example se disponível).
5. Execute a aplicação:
    ```bash
    streamlit run main.py
    ```

## Estrutura do Projeto:
```
skills_matrix_builder/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── utils/
│   ├── __init__.py
│   ├── session_manager.py
│   ├── exporter.py
├── modules/
│   ├── __init__.py
│   ├── input_stage.py
│   ├── hard_skills_stage.py
│   ├── objectives_stage.py
│   ├── activities_stage.py
│   ├── review_stage.py
└── assets/
    └── (imagens, logos, etc.)
```

- .env: Arquivo para variáveis de ambiente (como chaves de API, configurações, etc.).
- .gitignore: Arquivo para ignorar arquivos/pastas indesejadas no versionamento (ex.: arquivos temporários, dados sensíveis).
- README.md: Documentação inicial do projeto com instruções, escopo e como rodar a aplicação.
- requirements.txt: Lista de dependências necessárias para rodar o projeto.
- config.py: Módulo para carregamento e gerenciamento das configurações do projeto (ex.: variáveis do .env).
- main.py: Ponto de entrada do aplicativo Streamlit.
- utils/: Módulo com funções utilitárias, como gerenciamento de sessão e exportação de dados.
- modules/: Pasta onde cada etapa (tela) do construtor é modularizada: desde a entrada inicial, definição de hard skills, objetivos, atividades e revisão/exportação final.
- assets/: Pasta para armazenar imagens, logos ou outros arquivos estáticos que a aplicação possa utilizar.