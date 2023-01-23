from telebot import TeleBot, types
import work_with_json as w_json
import logger
from pathlib import Path
import calculate_telebot as calc_telebot

person = {}

'''данные о пользователеях и паролях хранятся в account_data.json
общение с ботом начинается с ввода /start
далее нужно либо войти либо зарегистрироваться. 
если никнэйм или пароль не совпадают с имеющимся в json, то предложит повторить.
если все нормально, то появится кнопка калькулятор (работает и с комплексными числами)
ввод аргументов строго через запятую в указанном порядке.
'''


TOKEN = '5822534129:AAGn65-0aqBL0YSqysQsF-MzSj77yDxU5z8'


bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Вход в систему')
    btn2 = types.KeyboardButton('Регистрация')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Здравствуйте!\nЯ бот - калькулятор.\nДля начала пользования войдите в систему или зарегистрируйтесь', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_text_message(msg: types.Message):

    if msg.text == 'Регистрация':

        bot.send_message(chat_id=msg.from_user.id, text ='введите свой никнэйм: ')
        bot.register_next_step_handler(msg, add_nickname)



    elif msg.text == 'Вход в систему':
        bot.send_message(chat_id=msg.from_user.id, text ='введите свой никнэйм: ')
        bot.register_next_step_handler(msg, get_nickname)



    elif msg.text == 'калькулятор':
        bot.send_message(chat_id=msg.from_user.id, text = 'введите через запятую: число 1, знак(+,-,/,*), число 2')
        bot.register_next_step_handler(msg, calc_telebot.calculate)

    elif msg.text == 'выход':
        bot.send_message(chat_id=msg.from_user.id, text = 'досвидания!)')

        pass
    else:
        print('недолет')


def add_nickname(msg: types.Message):
    nickname = msg.text
    account_data = w_json.json_in_lst('account_data.json')
    check = True
    for i in account_data:
        if logger.check_data(nickname, i['nickname']):
            check = True
            break
        else:
            check = False
        
    if check == True:
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вход в систему')
        btn2 = types.KeyboardButton('Регистрация')
        markup.add(btn1, btn2)
        bot.send_message(chat_id=msg.from_user.id, text ='пользователь с таким именем уже сущестует', reply_markup=markup)

        
    else:
        person['nickname'] = nickname
        bot.send_message(chat_id=msg.from_user.id, text ='введите пароль')
        bot.register_next_step_handler(msg, add_password)



def add_password(msg: types.Message):
    passw = msg.text
    person['password'] = passw
    account_data = w_json.json_in_lst('account_data.json')
    account_data.append(person)
    w_json.add_in_json(account_data, 'account_data.json')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('калькулятор')
    markup.add(btn1)

    bot.send_message(chat_id=msg.from_user.id, text ='Регистрация прошла успешно.\nНажмите на кнопку ниже чтоб произвести вычисление', reply_markup=markup)

person = dict(nickname='', password = '')

def get_nickname(msg: types.Message):
    nickname = msg.text
    account_data = w_json.json_in_lst('account_data.json')
    check = True
    for i in account_data:
        if logger.check_data(nickname, i['nickname']):
            bot.send_message(chat_id=msg.from_user.id, text ='введите пароль: ')
            global person
            person = dict(nickname=i['nickname'], password = msg.text)
            bot.register_next_step_handler(msg, get_password)

            check = True
            break
        else:
            check = False
        
    if check == False:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вход в систему')
        btn2 = types.KeyboardButton('Регистрация')
        markup.add(btn1, btn2)

        bot.send_message(chat_id=msg.from_user.id, text ='Такой пользователь не зарегистрирован. ', reply_markup=markup)




def get_password(msg: types.Message):
    nickname = person['nickname']
    passw = msg.text
    account_data = w_json.json_in_lst('account_data.json')

    coincidence = True

    for i in account_data:

        if logger.check_data(nickname, i['nickname']):
            print('сработало совпадение в')

            if logger.check_data(passw, i['password']):
                coincidence = True
                break

            else:
                print('не сработало совпадение')
                coincidence = False
    
    if coincidence == True:


        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('калькулятор')
        markup.add(btn1)
        bot.send_message(chat_id=msg.from_user.id, text ='Вход выполнен.', reply_markup=markup)

    
    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вход в систему')
        btn2 = types.KeyboardButton('Регистрация')
        markup.add(btn1, btn2)

        bot.send_message(chat_id=msg.from_user.id, text = 'пароль не верный\nпопробуйте снова', reply_markup=markup)


bot.polling()