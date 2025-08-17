import asyncio

class RobickoBot:
    def __init__(self):
        self.handlers = []
        self.adapter = None

    def on_message(self, func):
        self.handlers.append(("message", func))
        return func

    def on_text(self, func):
        self.handlers.append(("text", func))
        return func

    def on_command(self, cmd):
        def decorator(func):
            self.handlers.append((f"command:{cmd}", func))
            return func
        return decorator

    async def run(self, adapter):
        self.adapter = adapter
        print("✅ Robicko Bot Started with", adapter)
        await adapter.poll(self)
