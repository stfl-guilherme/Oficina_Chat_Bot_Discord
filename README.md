# Crie seu chatbot de IA no Discord com Python

Código da oficina da Semana Acadêmica de Sistemas de Informação · TecnoAMF.

Um bot que responde quando é mencionado no Discord, lembra a conversa do canal e tem a personalidade que você escrever, usando a API do Gemini.

## Pré-requisitos

- Python 3.10 ou mais novo
- Conta no Discord e um servidor seu para testes
- Conta Google para gerar a chave do Gemini ([aistudio.google.com](https://aistudio.google.com))
- VS Code (ou outro editor)

## Ministrantes

Equipe de desenvolvimento da TecnoAMF: Guilherme Stefanello, Luiz Guilherme, Lorenzo Paludett, Murilo Muller

## Como rodar

Abra o terminal na pasta do projeto e siga os passos do seu sistema.

| Passo | Windows (PowerShell) | Linux / macOS |
| --- | --- | --- |
| 1. Criar o venv | `py -m venv .venv` | `python3 -m venv .venv` |
| 2. Ativar o venv | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| 3. Instalar as bibliotecas | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| 4. Criar o `.env` | `Copy-Item .env.example .env` | `cp .env.example .env` |
| 5. Rodar o bot | `python main.py` | `python3 main.py` |

Depois do passo 4, abra o `.env` e cole o token do bot do Discord e a chave do Gemini. O `.env` nunca vai para o GitHub (ele está no `.gitignore`).

Para desligar o bot, aperte `Ctrl+C` no terminal.

## Quando der erro

| Erro | O que fazer |
| --- | --- |
| `Activate.ps1` bloqueado ("execução de scripts foi desabilitada") | Rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` no PowerShell, confirme com `S` e ative o venv de novo. |
| `ensurepip is not available` ao criar o venv (Linux) | Instale o pacote do venv: `sudo apt install python3-venv` e crie o venv de novo. |
| `PrivilegedIntentsRequired` | No [Discord Developer Portal](https://discord.com/developers/applications), abra o seu bot > **Bot** > ligue **Message Content Intent** e salve. |
| `KeyError: 'DISCORD_TOKEN'` | O `.env` não foi encontrado ou o nome está errado. Confira se o arquivo se chama `.env` (não `.env.txt`), se está na pasta do projeto e se a linha começa com `DISCORD_TOKEN=`. |
| Bot online, mas mudo | Você precisa **mencionar** o bot (`@NomeDoBot pergunta`). Confira também se a **Message Content Intent** está ligada e se o bot consegue ver o canal. |
| Bot responde "Deu erro ao falar com a IA" | Olhe o erro no terminal. Normalmente é a `GEMINI_API_KEY` errada ou o limite gratuito do Gemini estourado (espere um minuto e tente de novo). |
| `403 Forbidden` (`Missing Permissions`) | O bot não tem permissão para enviar mensagens naquele canal. Dê a permissão **Enviar mensagens** ao cargo do bot ou teste em outro canal. |
