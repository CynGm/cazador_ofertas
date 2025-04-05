import asyncio
from telegram import Bot

TELEGRAM_TOKEN = '7966462978:AAGiHM5Orax-0SfgF7T9ExbjOepLAqjq3bc'
CHAT_ID = '5811332307'

async def send_telegram_alert(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Ejecutar función async correctamente
asyncio.run(send_telegram_alert("¡Hola Cynthia! 🎉 Tu bot cazador de ofertas ya puede enviarte alertas."))

