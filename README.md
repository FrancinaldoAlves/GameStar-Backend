# API Backend do Sistema de Jogos e Reviews GameStar

Este repositório contém a **API** desenvolvida para o sistema de catálogo, reviews, favoritos e notícias de jogos.

A aplicação permite que usuários se cadastrem, façam login, avaliem jogos, favoritem títulos e visualizem notícias, enquanto administradores gerenciam o conteúdo da plataforma.

## Conteúdos

- [Tecnologias e Dependências](#tecnologias-e-dependências)
- [Ambientes de execução](#ambientes-de-execução)
    - [Desenvolvimento](#desenvolvimento-development)
- [Inicializando a API localmente](#inicializando-a-api-localmente)

## Tecnologias e Dependências

A aplicação foi construída com **Python 3** utilizando o framework **FastAPI**, com as seguintes dependências principais:

- [**FastAPI**](https://fastapi.tiangolo.com/) – Framework web moderno e de alta performance
- [**SQLAlchemy**](https://www.sqlalchemy.org/) – ORM para integração com banco de dados
- [**Pydantic**](https://docs.pydantic.dev/) – Validação e serialização de dados
- [**python-jose[cryptography]**](https://pypi.org/project/python-jose/) – Autenticação com tokens JWT
- [**passlib[bcrypt]**](https://passlib.readthedocs.io/) – Hashing seguro de senhas
- [**python-dotenv**](https://pypi.org/project/python-dotenv/) – Gerenciamento de variáveis de ambiente
- [**Uvicorn**](https://uvicorn.dev) – Servidor ASGI para desenvolvimento

## Ambientes de execução

Atualmente o projeto utiliza **SQLite** (`banco.db`) por simplicidade.

### Desenvolvimento (`development`)

- Modo com reload automático
- Documentação interativa do Swagger disponível em `/docs`
- Banco de dados local (`banco.db`)
- **CORS configurado** para permitir requisições do frontend

## Inicializando a API localmente

> [!WARNING]
> Todas as variáveis sensíveis devem ser definidas no arquivo `.env` localizado na raiz do projeto.
> (exemplo [.env.template](.env.template) fornecido no repositório)

Siga os passos abaixo para configurar o ambiente de desenvolvimento local da aplicação:

1. Criar ambiente virtual

    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux/Mac:
    source .venv/bin/activate
    ```

2. Instalação das dependências

    ```bash
    pip install -r requirements.txt
    ```

3. Configuração do arquivo de ambiente

    ```bash
    cp .env.template .env
    ```

   Edite o arquivo `.env` e preencha os valores necessários.

4. Executar a API localmente

    ```bash
    uvicorn main:website --reload
    ```

   A documentação Swagger estará disponível em:  
   **http://127.0.0.1:8000/docs**