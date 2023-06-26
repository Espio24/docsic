import telebot
import time
import datetime as DT

bot = telebot.TeleBot('6279890702:AAEYWD05qirwlzGZ-ZclGw5HGq1SJ5IiNHw')
CHAT_BY_DATETIME = dict()

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(func=lambda message: True)
def get_user_text(message: telebot.types.Message):
    text = '''Добрый день! Меня зовут Доксик и я бот.
Внедрение вашего ресторана завершено и в этом чате нет сотрудников службы поддержки, теперь обратиться в техническую поддержку можно так:
- Позвонив по номеру +7(800)555-96-79 - Написав на почту support@docsinbox.ru - Написав в личные сообщения в telegram @DocInBox_bot
Подробная инструкция об этом доступна по ссылке https://wiki.dxbx.ru/pages/viewpage.action?pageId=106267499'''
    need_seconds= 50
    current_time = DT.datetime.now()
    last_datetime = CHAT_BY_DATETIME.get(message.chat.id)

    if not last_datetime:
        CHAT_BY_DATETIME[message.chat.id] = current_time
        bot.send_message(message.chat.id, text, parse_mode='html')
    else:
        # Разница в секундах между текущим временем и временем последнего сообщения
        delta_seconds = (current_time - last_datetime).total_seconds()

        # Осталось ждать секунд перед отправкой
        seconds_left = int(need_seconds - delta_seconds)

        # Если время ожидания не закончилось
        if seconds_left > 0:
            log = f'Подождите {seconds_left} секунд перед выполнение этой команды {message.chat.id}'
            print(log)
        else:
            bot.send_message(message.chat.id, text, parse_mode='html')
            CHAT_BY_DATETIME[message.chat.id] = current_time


bot.polling(none_stop=True)