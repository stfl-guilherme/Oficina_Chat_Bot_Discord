import os
import re
import time

import discord
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. CONFIGURAÇÃO
load_dotenv()  # lê as chaves do arquivo .env
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

MODELO = "gemini-3.8-flash"
COOLDOWN_SEGUNDOS = 5
LIMITE_DISCORD = 2000  # tamanho máximo de uma mensagem no Discord

# Personalidade: diz para a IA como ela deve se comportar
PERSONALIDADE = "Você é um assistente útil. Responda em português, de forma curta."

intents = discord.Intents.default()
intents.message_content = True  # deixa o bot ler o texto das mensagens
bot = discord.Client(intents=intents)
ia = genai.Client(api_key=GEMINI_API_KEY)

# 2. MEMÓRIA
chats = {}  # {id do canal: conversa com o Gemini}
ultima_mensagem = {}  # {id do usuário: horário da última pergunta}


@bot.event
async def on_ready():
    print(f"Online como {bot.user}")


@bot.event
async def on_message(msg):
    # 3. FILTRO
    if msg.author.bot:
        return  # ignora outros bots (e ele mesmo)
    if bot.user not in msg.mentions:
        return  # só responde quando é mencionado

    # 4. PROTEÇÃO
    agora = time.time()
    if agora - ultima_mensagem.get(msg.author.id, 0) < COOLDOWN_SEGUNDOS:
        await msg.reply("Calma! Espere alguns segundos antes de perguntar de novo.")
        return
    ultima_mensagem[msg.author.id] = agora

    # Tira a menção (<@id> ou <@!id>) e sobra só a pergunta
    texto = re.sub(rf"<@!?{bot.user.id}>", "", msg.content).strip()

    # Cada canal tem a sua conversa; se ainda não tem, cria uma
    if msg.channel.id not in chats:
        chats[msg.channel.id] = ia.aio.chats.create(
            model=MODELO,
            config=types.GenerateContentConfig(system_instruction=PERSONALIDADE),
        )

    try:
        resposta = await chats[msg.channel.id].send_message(texto)
        await msg.reply(resposta.text[:LIMITE_DISCORD])
    except Exception as erro:
        print(erro)  # o erro completo aparece no terminal
        await msg.reply("Deu erro ao falar com a IA")


bot.run(DISCORD_TOKEN)
