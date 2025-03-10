## OllamaRTC

OllamaRTC é um projeto que implementa um servidor WebRTC utilizando aiohttp e aiortc para permitir comunicação em tempo real. Ele inclui uma interface de chat que interage com o modelo de linguagem llama3.2:latest. O objetivo do projeto é fornecer uma plataforma de comunicação que combina WebRTC para transmissão de dados em tempo real e llama3.2:latest para processamento de linguagem natural.


## Arquivos Principais

- `app.py`: Implementa o servidor WebRTC usando aiohttp e aiortc.
- `chat.py`: Contém funções para interação com o modelo de linguagem.
- `settings.py`: Contém configurações do projeto.
- `test.html`: Página HTML para o frontend do aplicativo de chat.
- `pyproject.toml`: Arquivo de configuração do projeto.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/Souzanderson/OllamaRTC
    cd OllamaRTC
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Inicie o servidor:
    ```sh
    python app.py
    ```

2. Abra o arquivo [test.html](https://github.com/Souzanderson/OllamaRTC/blob/main/test.html) em um navegador para acessar o frontend do aplicativo de chat.

## Dependências

As dependências do projeto estão listadas no arquivo [pyproject.toml](https://github.com/Souzanderson/OllamaRTC/blob/main/pyproject.toml):
- aiohttp-cors>=0.7.0
- aiohttp>=3.11.13
- aiortc>=1.10.1
- openai>=1.65.5
- requests>=2.32.3

## Licença

Este projeto está licenciado sob a MIT License.