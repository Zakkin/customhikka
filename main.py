from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import config

app = Client("own_hikka", api_id=config.API_ID, api_hash=config.API_HASH)
