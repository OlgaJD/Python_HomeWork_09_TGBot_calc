import telebot
import rational_calc
import complex_calc
import bot_log


API_TOKEN = 'your_token'
bot = telebot.TeleBot(API_TOKEN)

rational=False
complex=False

@bot.message_handler(commands=['start'])
def start_message(message):
    action = 'Бот начал работу'
    bot_log.act_log(action)
    bot.send_message(message.chat.id, 'Привет! Я готов к работе.\nМогу посчитать рациональные и комплексные выражения - /calc\nОтправить ссылку на проект в github - /git\nИли отправить всю историю моей работы - /log\nДля подсказки по командам всегда можно отправить мне - /help')


@bot.message_handler(commands=['help'])
def help_message(message):
    action = 'Пользователь запросил помощь по командам'
    bot_log.act_log(action)
    bot.send_message(message.chat.id, f'Помощь по командам:\n/calc - калькулятор\n/log - просмотр лога (будет отправлен файл)\n/git - ссылка на мой github с ботом')    


@bot.message_handler(commands=['calc'])
def calc_choose_message(message):
    bot.send_message(message.chat.id, f'Выбери калькулятор:\n/rational - для рациональных чисел \n/complex - для комплексных чисел')


@bot.message_handler(commands=['rational'])
def rational_calc_message(message):
    action = 'Используется калькулятор рациональных чисел'
    bot_log.act_log(action)
    global rational
    rational=True
    bot.send_message(message.chat.id, 'Введи выражение' )


@bot.message_handler(commands=['complex'])
def complex_calc_message(message):
    action = 'Используется калькулятор комплексных чисел'
    bot_log.act_log(action)
    global complex
    complex=True
    bot.send_message(message.chat.id, 'Подсказки для верного ввода:\n * Мнимая часть выражения должна быть обозначена буквой i или j, используй только одну букву в выражении.\n * Комплексные числа должны быть заключены в скобки.\n * Пример правильного ввода выражения:\n  (3+2j)*(4-3j)\nВведи выражение:\n')


@bot.message_handler(commands=['log'])
def get_log(message):
    action = 'Отправлен лог'
    bot_log.act_log(action)
    bot.send_message(message.chat.id, 'Лови лог' )
    bot.send_document(message.chat.id, open(r'log.txt', 'rb'))


@bot.message_handler(commands=['git'])
def get_github_link(message):
    action = 'Запрос на ссылку github'
    bot_log.act_log(action)
    bot.send_message(message.chat.id,'Ссылка на мой гитхаб:\n\n' + "https://github.com/OlgaJD/Python_HomeWork_09_TGBot_calc.git")   


@bot.message_handler(content_types='text')
def message_reply(message):
    global rational
    global complex
    greeting_set=['привет','Привет','Hi','hi','Здравствуй','Добрый день','Дратути']
    for values in greeting_set:
        if values in message.text:
            bot.send_message(message.chat.id, 'Я тут')
    if rational:
        bot.send_message(message.chat.id, f'Ответ: {rational_calc.get_rational_result(message.text)}')
        expression = message.text
        result = rational_calc.get_rational_result(message.text)
        bot_log.cal_log(expression, result)
        rational = False
    if complex:
        bot.send_message(message.chat.id, f'Ответ: {complex_calc.get_complex_result(message.text)}')
        expression = message.text
        result = complex_calc.get_complex_result(message.text)
        bot_log.cal_log(expression, result)
        complex=False


bot.polling()
