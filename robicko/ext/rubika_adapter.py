import asyncio
from ..types import Message

class RubikaAdapter:
    def __init__(self, token):
        self.token = token

    async def poll(self, bot):
        # شبیه‌ساز دریافت پیام
        while True:
            msg = Message(chat_id=12345, text="/start")
            for (typ, func) in bot.handlers:
                if typ == "command:start":
                    await func(type("Update", (), {"message": msg}))
            await asyncio.sleep(5)

    async def send_message(self, chat_id, text):
        print(f"[SEND MESSAGE to {chat_id}] {text}")
