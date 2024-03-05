from pyrogram import Client
import config
from module_loader import load_and_setup_modules

app = Client("own_hikka", api_id=config.API_ID, api_hash=config.API_HASH)

if __name__ == "__main__":
    load_and_setup_modules(app)
    app.run()
