from pyrogram import filters

class CommandWithPrefix(filters.Filter):
    def __init__(self, command, prefix):
        self.command = command
        self.prefix = prefix

    def __call__(self, _, message):
        text = message.text or ""
        return text.startswith(self.prefix + self.command)

def command_with_prefix(command, prefix="."):
    return CommandWithPrefix(command, prefix)
