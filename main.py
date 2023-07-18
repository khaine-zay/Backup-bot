from pyrogram import Client, filters
from logging import basicConfig, StreamHandler, getLogger, INFO, DEBUG
import os
from dotenv import load_dotenv

basicConfig(
    level=INFO,
    handlers=[StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

LOGGER = getLogger(__name__)
getLogger("pyrogram").setLevel(INFO)

load_dotenv()
api_id = int(os.environ.get("API_ID", ""))

api_hash = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

MAIN_CHANNEL = os.environ.get("MAIN_CHANNEL", "")
MAIN_CHANNEL = list(set(int(x) for x in MAIN_CHANNEL.split()))
MAIN_CHANNEL = list(set(MAIN_CHANNEL))

BACKUP_CHANNEL = int(os.environ.get("BACKUP_CHANNEL", ""))

bot = Client('bot', api_id, api_hash, bot_token=BOT_TOKEN).start()

@bot.on_message(filters.channel & filters.chat(MAIN_CHANNEL))
async def a(client, message):
    await message.forward(chat_id=BACKUP_CHANNEL)

bot.loop.run_forever()
