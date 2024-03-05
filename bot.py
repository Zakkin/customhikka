from pyrogram import Client
import config
import os
import sys
import importlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Client("own_hikka", api_id=config.API_ID, api_hash=config.API_HASH)

class ModuleReloader(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py') and not event.src_path.startswith('__'):
            print(f"Detected a change in: {event.src_path}")
            module_name = os.path.basename(event.src_path)[:-3]
            module_path = f"modules.{module_name}"
            try:
                if module_name in sys.modules:
                    importlib.reload(sys.modules[module_path])
                else:
                    importlib.import_module(module_path)
                

                module = sys.modules[module_path]
                if hasattr(module, 'setup'):
                    module.setup(app)
                print(f"Module {module_name} reloaded")
            except Exception as e:
                print(f"Failed to reload module {module_name}: {e}")

def load_and_setup_modules(app):
    modules_path = 'modules'
    for filename in os.listdir(modules_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module_path = f"{modules_path}.{module_name}"
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, 'setup'):
                    module.setup(app)
            except Exception as e:
                print(f"Error loading module {module_name}: {e}")

if __name__ == "__main__":
    load_and_setup_modules(app)
    
    event_handler = ModuleReloader()
    observer = Observer()
    observer.schedule(event_handler, path='modules', recursive=False)
    observer.start()
    
    try:
        app.run()
    finally:
        observer.stop()
        observer.join()
