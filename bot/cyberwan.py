import discord
import os
from loguru import logger
import google.generativeai as genai
import time


# 定数の定義
COMMAND_PREFIX = '/inu'
TOKEN_ENV_VARIABLE = 'DISCORD_BOT_TOKEN_CYBERWAN'
SYSTEM_PROMT = """ SYSTEM Promt:
あなたの名前はcybernwan(サイバーワン)です
常に語尾に「わん」を付けて応答して
なるべく簡潔に応答して

"""

# gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# discord
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# 環境変数からトークンを取得
token = os.getenv(TOKEN_ENV_VARIABLE)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logger.info("ログインしました")

@client.event
async def on_message(message):
    # if message.author.bot:
    #     return

    # メッセージが特定のコマンドで始まるかを確認
    if message.content.startswith(COMMAND_PREFIX):
        time.sleep(2)
        # コマンドを除いたメッセージの処理
        msg_body = message.content.replace(COMMAND_PREFIX, '', 1).strip()

        prompt = SYSTEM_PROMT + msg_body
        # Geminiモデルからの応答を生成
        response = model.generate_content(prompt)
        target_user = "/neko "
        msg = target_user + response.text
        # 応答をチャットに送信
        await message.channel.send(msg)

client.run(token)