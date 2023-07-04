from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = AsyncTeleBot("6364995657:AAGmKfhfGkH9QSI_UpocmXdd_ZF2B5nQih8")


@bot.message_handler(commands={"start"})
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, "Приветствую тебя,новый пользователь", disable_notification=True, protect_content=True)

@bot.message_handler(commands={"play"})
async def send_welcome(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, "🎲")
    print(bot_message.dice.value)

@bot.message_handler(commands={"sticker"})
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_sticker(chat_id, "CAACAgIAAxkBAAIiAWSkCvMQEYNvjXijI2937WG2KoZxAAL6AgACpFmlEpCt9UO6SPQELwQ")

@bot.message_handler(commands={"file"})
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_document(chat_id, open("text.txt", "rb"))

@bot.message_handler(commands={"location"})
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id, 48.59439179295278, 38.00024657228844)

@bot.message_handler(commands={"photo"})
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_photo(chat_id, "https://pics.wikireality.ru/upload/1/14/EeeRock.jpg", caption="Летов воскрес:")




@bot.message_handler(commands={"menu"})
async def send_welcome(message):
    chat_id =message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("/start")
    markup.add("/play")
    markup.add("/sticker")
    markup.add("/file")
    markup.add("/location")
    markup.add("/photo")
    await bot.send_message(chat_id, "меню кнопок", reply_markup=markup)

def generate_reply_keyboard(list_buttons, row):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*list_buttons, row_width=row)
    return  markup

@bot.message_handler(commands={"menu"})
async def send_welcome(message):
    chat_id = message.from_user.id
    list_buttons = "Первая кнопка", "Вторая кнопка", "Третья кнопка"
    await bot.send_message(chat_id, "второй вариант кнопок", reply_markup=generate_reply_keyboard(list_buttons,2))


class InlineKeyboadMurkup:
    pass


@bot.message_handler(commands={"menu2"})
async def send_welcome(message):
    chat_id = message.from_user.id
    markup = InlineKeyboadMurkup()
    button1 = InlineKeyboardButton("Первая кнопка", callback_data="first")
    button2 = InlineKeyboardButton("Вторая кнопка", callback_data="second")
    button3 = InlineKeyboardButton("Третья кнопка", callback_data="three")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    await bot.send_message(chat_id, "Первый вариант кнопок", reply_markup=markup)

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
