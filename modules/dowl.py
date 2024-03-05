from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from custom_filters import command_with_prefix
import requests
import os

def import_module(client: Client, message: Message):
    if message.reply_to_message and message.reply_to_message.document:
        document = message.reply_to_message.document
        module_name = document.file_name
        if not module_name.endswith(".py"):
            message.reply_text("Ошибка: Файл не является модулем")
            return
        

        file_path = client.download_media(message.reply_to_message)
        
        os.rename(file_path, f'modules/{module_name}')
        try:
            formatted_module_name = module_name.replace('.py', '')
            with open('main.py', 'a') as main_file:
                main_file.write(f'\nfrom modules.{formatted_module_name} import setup as setup_{formatted_module_name}\n')
                main_file.write(f'setup_{formatted_module_name}(app)\n')
            
            message.reply_text(f"Модуль {module_name} успешно импортирован и добавлен, для перезагрузки откройте ``restart.bat``")
        except Exception as e:
            message.reply_text(f"Ошибка при добавлении модуля: {e}")
    else:
        message.reply_text("Пожалуйста, ответьте на сообщение с Python файлом командой .import")

def setup(app: Client):
    app.add_handler(MessageHandler(import_module, command_with_prefix("import", ".")))
