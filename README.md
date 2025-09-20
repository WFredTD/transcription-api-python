🚀 API de Transcrição de Mídia
==============================

> Uma API RESTful de alta performance para converter áudio e vídeo em texto, construída com Python e Inteligência Artificial.

### ✨ Visão Geral

Esta API foi desenvolvida para ser a espinha dorsal de qualquer aplicação que precise de transcrição de mídia. Ela demonstra proficiência técnica em diversas áreas-chave do desenvolvimento moderno:

-   **Desenvolvimento de APIs Robustas:** Criação de um serviço escalável com **FastAPI**.

-   **Integração com IA:** Uso de modelos de **Machine Learning** de ponta (OpenAI Whisper) em um ambiente de produção.

-   **Boas Práticas:** Código limpo, documentação automatizada e gestão de dependências com ambientes virtuais.

### 🛠️ Tecnologias Utilizadas

A API é construída com uma "stack" de tecnologias modernas e eficientes.
<p align='center'>
    <img loading="lazy" src="https://skillicons.dev/icons?i=python,fastapi,git,github,vscode"/> 
</p>

### 🌟 Funcionalidades

-   **Transcrições de Alta Precisão:** Utiliza o modelo **Whisper `medium`**, que oferece uma precisão de nível industrial, ideal para diferentes sotaques e qualidades de áudio.

-   **Suporte Universal a Mídia:** A API aceita uma vasta gama de formatos, incluindo áudio (`.opus`, `.mp3`, `.wav`) e vídeo (`.mp4`, `.mov`).

-   **Documentação Interativa e Completa:** A API vem com documentação interativa automática, perfeita para testes e colaboração:

    -   **Swagger UI:** Acesse em `/docs`

    -   **ReDoc:** Acesse em `/redoc`

### ⚙️ Como Rodar a Aplicação

Siga estes passos simples para rodar o projeto localmente.

#### **Pré-requisitos**

Certifique-se de que você tem o **Python 3.8+** e o **FFmpeg** instalados em sua máquina.

**Instalação do FFmpeg:**

-   **Windows:** Baixe a versão `full` do [gyan.dev](https://www.gyan.dev/ffmpeg/builds/ "null") e adicione a pasta `bin` ao seu PATH.

-   **macOS:** Instale via Homebrew: `brew install ffmpeg`.

-   **Linux (Debian/Ubuntu):** Instale via `apt`: `sudo apt install ffmpeg`.

#### **Início Rápido**

1.  **Clone o Repositório:**

    ```
    git clone [https://www.dio.me/articles/enviando-seu-projeto-para-o-github](https://www.dio.me/articles/enviando-seu-projeto-para-o-github)
    cd [pasta do projeto]

    ```

2.  **Configure e Ative o Ambiente Virtual:**

    ```
    python -m venv .venv
    .venv\Scripts\activate  # No Windows
    source .venv/bin/activate  # No macOS/Linux

    ```

3.  **Instale as Dependências:**

    ```
    pip install -r requirements.txt

    ```

4.  **Inicie a API:**

    ```
    uvicorn main:app --reload

    ```

    O servidor estará ativo em `http://127.0.0.1:8000`.

### 🚀 Endpoints da API

**`POST /transcrever_audio/`**

-   **Descrição:** Recebe um arquivo de mídia via formulário e retorna a transcrição em texto.

-   **Corpo da Requisição:**  `audio_file` (formato `file`)

#### **Exemplo de Uso com HTTPie**

```
http -f POST [http://127.0.0.1:8000/transcrever_audio/](http://127.0.0.1:8000/transcrever_audio/) audio_file@/caminho/para/seu/arquivo.mp4

```

Este projeto é uma prova prática de competência e pode ser facilmente adaptado e integrado a qualquer outro projeto web ou móvel. Fique à vontade para explorá-lo, testá-lo e contribuir.