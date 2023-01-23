'''модуль для вывода приветствия, запроса на конкретное действие'''

# import input_data
import add_in_phonebook as add_pers
import input_data
import export_phonebook
import import_phonebook
import search_person as search_p
import present_in_terminal as pres_term

from telebot import TeleBot, types


TOKEN = '5822534129:AAGn65-0aqBL0YSqysQsF-MzSj77yDxU5z8'


bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Ввести информацию об абоненте')
    # btn2 = types.KeyboardButton('Вывести справочник в сообщении')
    btn3 = types.KeyboardButton('Найти абонента в справочнике')
    btn4 = types.KeyboardButton('Выслать справочник файлом')
    btn5 = types.KeyboardButton('Загрузить данные в справочник из Вашего файла')
    btn6 = types.KeyboardButton('Выход')


    markup.add(btn1, btn3, btn4, btn5, btn6)
    bot.send_message(message.from_user.id, 'Здравствуйте!\nЯ - телефонный справочник.\nВыберите действие, которое хотите совершить', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(msg: types.Message):

    if msg.text == 'Ввести информацию об абоненте':

        inp_person = bot.send_message(chat_id=msg.from_user.id, text ='Введите данные об абоненте через пробел'
                                                                    'в формате "Фамилия" "Имя" "Телефон(+79999999999"'
                                                                    'дополнительная информация(при желании)')
        
        bot.register_next_step_handler(msg, input_data.input_person)



    elif msg.text == 'Найти абонента в справочнике':
        bot.send_message(chat_id=msg.from_user.id, text ='введите свой никнэйм: ')
        bot.register_next_step_handler(msg, get_nickname)



    elif msg.text == 'Выслать справочник файлом':
        bot.send_message(chat_id=msg.from_user.id, text = 'введите через запятую: число 1, знак(+,-,/,*), число 2')
        bot.register_next_step_handler(msg, calc_telebot.calculate)

    elif msg.text == 'Выход':
        bot.send_message(chat_id=msg.from_user.id, text = 'досвидания!)')

        pass
    else:
        print('недолет')


bot.polling()

# @bot.message_handler(content_types=['text'])
# def get_text_message(msg: types.Message):

#     if msg.text == 'Регистрация':

#         bot.send_message(chat_id=msg.from_user.id, text ='введите свой никнэйм: ')
#         bot.register_next_step_handler(msg, add_nickname)



#     elif msg.text == 'Вход в систему':
#         bot.send_message(chat_id=msg.from_user.id, text ='введите свой никнэйм: ')
#         bot.register_next_step_handler(msg, get_nickname)



#     elif msg.text == 'калькулятор':
#         bot.send_message(chat_id=msg.from_user.id, text = 'введите через запятую: число 1, знак(+,-,/,*), число 2')
#         bot.register_next_step_handler(msg, calc_telebot.calculate)

#     elif msg.text == 'выход':
#         bot.send_message(chat_id=msg.from_user.id, text = 'досвидания!)')

#         pass
#     else:
#         print('недолет')



# def make_choice():
#     hello = 'Что Вы хотите сделать?:\n1. Ввести информацию об абоненте. \n2. Вывести справочник в консоль. \n3. Найти абонента в справочнике \n4. Экспортировать справочник в файл. \n5. Импортировать данные из файла. \n0. Выход. \nВведите номер пункта и нажмите "ввод"'
#     print(hello)
#     choice = input('Ваш выбор?: ')

#     if choice == '1':
#         return add_pers.add_in_phonebook()
#     elif choice == '2':
#         return pres_term.present_in_terminal()
#     elif choice == '3':
#         return search_p.search_person()
#     elif choice == '4':
#         return export_phonebook.present_data()
#     elif choice == '5':
#         return import_phonebook.import_ph_b()
#     elif choice == '0':
#         return 
   
#     else:
#         print('некорректный ответ')




