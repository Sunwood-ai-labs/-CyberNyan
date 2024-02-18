import discord
import os  # osモジュールをインポート
from loguru import logger

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# 環境変数からトークンを取得
TOKEN = os.getenv('DISCORD_BOT_TOKEN_CYBERNYAN')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logger.info("ログインしました")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/tori':
        await message.channel.send('ちゅん')

client.run(TOKEN)