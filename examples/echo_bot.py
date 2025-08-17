import asyncio
from robicko import RobickoBot
from robicko.ext.rubika_adapter import RubikaAdapter

# توکن ربات
TOKEN = "YOUR_TOKEN_HERE"

# ساخت نمونه ربات
bot = RobickoBot()

# دستور /start
@bot.on_command("start")
async def start(update):
    await bot.adapter.send_message(
        update.message.chat.id,
        "سلام! من ربات روبیکو هستم 🤖"
    )

# اکو کردن پیام‌ها
@bot.on_text
async def echo(update):
    await bot.adapter.send_message(
        update.message.chat.id,
        f"اکو: {update.message.text}"
    )

# اجرای ربات
if __name__ == "__main__":
    adapter = RubikaAdapter(TOKEN)
    asyncio.run(bot.run(adapter))
