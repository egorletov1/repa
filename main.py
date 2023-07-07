from telebot import types
import telebot
import random



TOKEN='6137544522:AAGtLYNcv3eIeqQAK_q8jnwFsPwPfcyz3Ws'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

def par_an():
    anec_list = list()
    anec_str = ''
    with open('text.txt', 'r', encoding="utf-8") as file:
        anec = file.read()

    while anec.find('#') !=-1:
        anec_list.append(anec[0:anec.find('#')])
        anec = anec[anec.find('#')+1:len(anec)-1]
    print(anec_list)
    return anec_list



def w_b_id(id):
    with open('id.txt', 'w') as file:
        file.write(str(id.id))
def r_b_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
    return id

def calculet(primer):
    try:
        answer = eval(primer)
    except:
        return 'Не правильно введен пример'
    return primer + '=' + str(answer)

class M_sost():
    def __init__(self):
        self.call_2 = False

m_sost = M_sost()

def skill(chat_id):
    print('work')
    keyword = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Расскажи анекдот', callback_data='3')
    btn2 = types.InlineKeyboardButton(text='Могу стать калькулятором', callback_data='4')
    keyword.add(btn1)
    keyword.add(btn2)
    dz_id = bot.send_message(chat_id, 'Я много чего умею, выбери что хочешь', reply_markup=keyword)
    w_b_id(dz_id)

def b_answer(chat_id, ans, message):
    bot.delete_message(chat_id, r_b_id())
    bot.delete_message(chat_id, message.id)
    keyword = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Вернуться к моим умениям', callback_data='5')
    keyword.add(btn1)
    dz_id = bot.send_message(chat_id, ans, reply_markup=keyword)
    w_b_id(dz_id)

def b_answer1(chat_id, ans, message):
    bot.delete_message(chat_id, r_b_id())
    keyword = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Вернуться к моим умениям', callback_data='5')
    keyword.add(btn1)
    dz_id = bot.send_message(chat_id, ans, reply_markup=keyword)
    w_b_id(dz_id)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    keyword = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='да', callback_data='1')
    btn2 = types.InlineKeyboardButton(text='Нет', callback_data='2')
    keyword.row(btn1, btn2)
    dz_id = bot.send_message(chat_id, 'Привет, меня зовут Джудия. Хочешь узнать что я умею?', reply_markup=keyword)
    w_b_id(dz_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    chat_id = call.message.chat.id
    if call.data == '1':
        bot.delete_message(chat_id, r_b_id())
        skill(chat_id)
    elif call.data == '4':
        m_sost.call_2 = True
        bot.delete_message(chat_id, r_b_id())
        markup = types.ForceReply(selective=False)
        dz_id = bot.send_message(chat_id, 'Введи однострочный пример', reply_markup=markup)
        w_b_id(dz_id)
    elif call.data == '3':
        ans = par_an()
        b_answer1(chat_id, ans[random.randint(0, len(ans)-1)], call.message)

    elif call.data == '5':
        bot.delete_message(chat_id, r_b_id())
        skill(chat_id)
    elif call.data == '2':
        bot.send_message(chat_id, 'Ладно, если передумаешь просто нажми на /start)')
    else:
        bot.send_message(chat_id, 'Извини я тебя не поняла')



@bot.message_handler(func=lambda message: True)
def messege_worker(message):
    chat_id = message.chat.id
    if m_sost.call_2:
        m_sost.call_2 = False
        ans = calculet(message.text)
        b_answer(chat_id, ans, message)




bot.infinity_polling()