from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("6364995657:AAGmKfhfGkH9QSI_UpocmXdd_ZF2B5nQih8")


@bot.message_handler(commands={"help", "start", "menu", "stop"})
async def send_welcome(message):
    await bot.reply_to(message, "Приветствую тебя,новый пользователь")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text_message = message.text
    text_message = text_message.lower()
    if "дела" in text_message or "настроение" in text_message:
        await bot.reply_to(message, "Хорошо, а у тебя?")
    elif "погода" in text_message:
        await bot.reply_to(message, "Отличная")
    else:
        await bot.reply_to(message, "Извините, я вас не понял")

import asyncio

asyncio.run(bot.polling())
