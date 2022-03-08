import telebot

#BOT_TOKEN = "5192874877:AAHE4es-_5QUfvCvR2Mxj3qcaX5YrQiixjI"

#a = Bot(token="5192874877:AAHE4es-_5QUfvCvR2Mxj3qcaX5YrQiixjI")
from telebot import types
import requests

a = telebot.TeleBot("5192874877:AAHE4es-_5QUfvCvR2Mxj3qcaX5YrQiixjI")

@a.message_handler(commands=['start'])
def startWork(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1", "2", "3", "4", "5")
    tid = message.chat.id
    a.send_message(tid, "Бот запущен!", reply_markup=markup)


@a.message_handler(content_types=['text'])
def sendYourMessage(message):
    mid = message.chat.id

    if message.text == "1":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add("Популярные сайты IT", "Полезные сайты IT",
                   "еще несколько популярных сайтов", "назад")
        a.send_message(mid, "Выбирайте", reply_markup=markup)


    elif message.text == "2":

        @a.message_handler(content_types=['voice'])
        def handle_voice(message):
            tid = message.chat.id
            a.send_message(tid, "ага")
            a.polling()

    elif message.text == "3":

        tid = message.chat.id
        l = a.send_message(tid, 'Привет! Как тебя зовут?')

        a.register_next_step_handler(l, hello)

    elif message.text == "4":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add("Привет", "Пока",
                   "Удалить клавиатуру", "назад")
        a.send_message(mid, "Выбирайте", reply_markup=markup)


    elif message.text == "5":
        response = requests.get("https://reqres.in/api/users/2")
        mail = response.json()
        a.send_message(mid, mail["data"]["email"])



    elif message.text == "Популярные сайты IT":
        a.send_message(
            mid,
            "habr.com\nХабр — русскоязычный веб-сайт в формате системы тематических коллективных блогов с элементами новостного сайта, созданный для публикации новостей, аналитических статей, мыслей, связанных с информационными технологиями, бизнесом и интернетом. Основан Денисом Крючковым в июне 2006 года.\ncomnews.ru\nНовости цифровой трансформации, ИТ, телекоммуникаций\nAppleinsider.ru\nОбзор лучших приложений под iPhone, как отремонтировать iPhone или iPad, что нужно знать при покупке Mac и MacBook.\nFerra.\nроссийский журнал о потребительской электронике."
        )
    elif message.text == "Полезные сайты IT":
        a.send_message(
            mid,
            "ru.stackoverflow.com\nStack Overflow — система вопросов и ответов о программировании\ngithub.com\nGitHub — крупнейший веб-сервис для хостинга IT-проектов и их совместной разработки.\ncyberforum.ru\nКиберФорум - форум программистов, системных администраторов, администраторов баз данных, компьютерный форум, форум по электронике"
        )
    elif message.text == "еще несколько популярных сайтов":
        a.send_message(
            mid,
            "3dnews.ru\nСамые интересные и оперативные новости из мира высоких технологий.\nTdaily.ru\nЕжедневно на сайте публикуются десятки новостей рынка телекоммуникаций"
        )
    elif message.text == "Привет":
        a.send_message(mid, "Привет:)")
    elif message.text == "Удалить клавиатуру":
        a.send_message(
            mid,
            "Клавиатура удалена",
            reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text == "Пока":
        a.send_message(mid, "Пока:(")
    elif message.text == "назад":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add("1", "2", "3", "4", "5")
        a.send_message(mid, "Мы вернулись", reply_markup=markup)
    else:
        a.send_message(mid, "Не понимаю тебя")


def hello(message):
    b = a.send_message(
        message.chat.id,
        'Приятно познакомиться, {name}. Сколько тебе лет?'.format(
            name=message.text))
    a.register_next_step_handler(b, age)


def age(message):
    c = a.send_message(
        message.chat.id,
        'Ого, целых {old}. Где ты живёшь?'.format(
            old=message.text))
    a.register_next_step_handler(c, live)


def live(message):
    d = a.send_message(
        message.chat.id,
        'Знакомый город, {city}, как у тебя дела? '.format(
            city=message.text))
    a.register_next_step_handler(d, how)


def how(message):
    e = a.send_message(
        message.chat.id,
        ' Ага, {f}, значит, у меня все неплохо '.format(
            f=message.text))


@a.message_handler(content_types=['voice'])
def handle_voice(message):
    tid = message.chat.id
    a.send_message(tid, "ага")


a.polling()
