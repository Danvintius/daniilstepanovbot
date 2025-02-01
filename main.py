from random import choice
import telebot

token = '*'

bot = telebot.TeleBot(token)

HELP = """
/help - напечатать справку по программе.
/author - информация об авторе.
/books - информация о книгах.
/shop - купить книгу.
/meet - записаться на приём.
/exit - выйти из программы."""

author_text = "Даниил Максимович Степанов родился в 1994 г. в Воронежской области. Начал писать в 15 лет. Различные истории из детства вдохновили его писать фантастические повести для детей. В 2016 г. окончил Российский государственный гуманитарный университет, архивист-документовед по образованию. В настоящее время проживает в г. Балашиха."

books_text = "Серия \"Центральноградские сыщики\":\n1. Заговор котов\n2. Новый враг\n3. Царский меч\n\nПустой трон"
book_offer = "Хотите купить книгу? Тогда введите команду /shop"
howareyou_answers = ["Нормально", "Отлично!", "Как у зебры", "Бывало и лучше", "Дела идут, контора пишет", "Всё нормально"]
howareyoudoing_answers = ["Размышляю", "Занимаюсь ботскими делами", "Ищу смысл жизни", "Строю планы"]
question_answers = ["Хороший вопрос. Я подумаю", "Надо подумать", "А сам как думаешь?", "Да. Наверное. Или нет?", "Это интересный вопрос", "Уточните вопрос"]
advices = ["Тут надо всё обдумать", "Будь благоразумнее", "Пока ты готовишься к жизни - она проходит", "Время бесценно. Не трать его попусту", "Будь собой"]
bot_listen = ["Слушаю", "Бот слушает", "Внимательно"]
elsy_answers = ["Хм", "Ясно", "Понятно", "Думаю", "Завис", "Ок", "Надо подумать", "Увидимся", "Занимаюсь ботскими делами", "Да ладно", book_offer]

@bot.message_handler(commands=['start', 'help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['author'])
def author(message):
    bot.send_message(message.chat.id, author_text)
    bot.send_message(message.chat.id, book_offer)

@bot.message_handler(commands=['books'])
def books(message):
    bot.send_message(message.chat.id, books_text)
    bot.send_message(message.chat.id, book_offer)

@bot.message_handler(commands=['shop'])
def shop(message):
    text = "Хотите купить книгу? Пишите на e-mail"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['meet'])
def meet(message):
    text = "Хотите записаться на приём? Пишите на e-mail"
    bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, book_offer)

@bot.message_handler(commands=['exit'])
def exit(message):
    bot.send_message(message.chat.id, book_offer)
    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=SDTD4pL0mLc')

@bot.message_handler(content_types=['text', 'sticker'])
def conversation(message):
    howareyou_answer = choice(howareyou_answers)
    howareyoudoing_answer = choice(howareyoudoing_answers)
    elsy_answer = choice(elsy_answers)
    question_answer = choice(question_answers)
    advice = choice(advices)
    bot_listen_answer = choice(bot_listen)
    if 'Привет' in message.text:
      bot.send_message(message.chat.id, "Привет!")
    elif 'Как дела' in message.text:
      bot.send_message(message.chat.id, howareyou_answer)
      bot.send_message(message.chat.id, "Как сам?")
    elif 'как дела' in message.text:
      bot.send_message(message.chat.id, howareyou_answer)
    elif 'Как жизнь' in message.text:
      bot.send_message(message.chat.id, howareyou_answer)
      bot.send_message(message.chat.id, "Как сам?")
    elif 'Ты как' in message.text:
      bot.send_message(message.chat.id, howareyou_answer)
      bot.send_message(message.chat.id, "Как сам?")
    elif 'Нормально' in message.text:
      bot.send_message(message.chat.id, "Хорошо")
      bot.send_message(message.chat.id, elsy_answer)
    elif 'Слушай' in message.text:
      bot.send_message(message.chat.id, bot_listen_answer)
    elif 'бот' in message.text:
      bot.send_message(message.chat.id, bot_listen_answer)
    elif 'Бот' in message.text:
      bot.send_message(message.chat.id, bot_listen_answer)
    elif 'ситуация' in message.text:
      bot.send_message(message.chat.id, "Ситуация непростая")
    elif 'Эй' in message.text:
      bot.send_message(message.chat.id, "На \"эй\" зовут свиней" + '%F0%9F%98%81')
    elif 'делаешь' in message.text:
      bot.send_message(message.chat.id, howareyoudoing_answer)
    elif 'занимаешься' in message.text:
      bot.send_message(message.chat.id, howareyoudoing_answer)
    elif 'Книги' in message.text:
      bot.send_message(message.chat.id, books_text)
    elif 'книги' in message.text:
      bot.send_message(message.chat.id, books_text)
    elif 'делать' in message.text:
        bot.send_message(message.chat.id, "Почитай книгу")
        bot.send_message(message.chat.id, "Я советую эти")
        bot.send_message(message.chat.id, books_text)
        bot.send_message(message.chat.id, book_offer)
    elif 'книгу' in message.text:
        bot.send_message(message.chat.id, books_text)
        bot.send_message(message.chat.id, book_offer)
    elif 'Посоветуй' in message.text:
        bot.send_message(message.chat.id, advice)
    elif 'посоветуй' in message.text:
        bot.send_message(message.chat.id, advice)
    elif 'посоветуешь' in message.text:
        bot.send_message(message.chat.id, advice)
    elif 'совет' in message.text:
        bot.send_message(message.chat.id, advice)
    elif 'совета' in message.text:
        bot.send_message(message.chat.id, advice)
    elif '?' in message.text:
        bot.send_message(message.chat.id, question_answer)
        bot.send_message(message.chat.id, "А пока купи книгу или сделай пожертвование")
    else:
      bot.send_message(message.chat.id, elsy_answer)

@bot.message_handler(content_types=['location'])
def location(message):
      bot.send_message(message.chat.id, "Понял, выдвигаюсь")

@bot.message_handler(content_types=['contact'])
def contact(message):
      bot.send_message(message.chat.id, "Обязательно позвоню")

bot.polling(none_stop=True)
