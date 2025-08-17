# Robicko

کتابخانه قدرتمند برای ساخت ربات در روبیکا 🚀

## نصب
```bash
pip install robicko
```

## مثال
```python
import asyncio
from robicko import RobickoBot
from robicko.ext.rubika_adapter import RubikaAdapter

bot = RobickoBot()

@bot.on_text
async def echo(u):
    await bot.adapter.send_message(u.message.chat.id, f"اکو: {u.message.text}")

if __name__ == "__main__":
    adapter = RubikaAdapter("YOUR_TOKEN_HERE")
    asyncio.run(bot.run(adapter))
```
