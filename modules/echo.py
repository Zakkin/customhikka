from pyrogram import Client
from pyrogram.handlers import MessageHandler
from custom_filters import command_with_prefix


def echo(client, message):
    text = message.text[len(".echo"):].strip() 
    message.reply_text(f'Echo: {text}')

def setup(app: Client):
    app.add_handler(MessageHandler(echo, command_with_prefix("echo", ".")))
