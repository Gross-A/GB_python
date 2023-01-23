

import re


from telebot import TeleBot, types

TOKEN = '5822534129:AAGn65-0aqBL0YSqysQsF-MzSj77yDxU5z8'


bot = TeleBot(TOKEN)



def check_complex(str):


    if len(re.findall(r'[a-z]', str)) > 0:
        # print('комплексное')
        s = re.findall(r'[+-]? ?\d+', str)
        x = complex(int(s[0]), int(''.join(s[1].split())))
        # print(x)
        return x

    else:
        # print('рациональное')
        return float(str)


def calculate(msg: types.Message):
    choice = True
    x_str, sign, y_str = map(str, msg.text.split(','))
    # while choice == True:
        # bot.send_message(chat_id=msg.from_user.id, text = 'напишите знак (+,-,*,/)')


        # s = msg.text

    # if sign == '0':
    #     break
    if sign in ('+', '-', '*', '/'):
        x = check_complex(x_str)
        y = check_complex(y_str)
        match sign:
            case '+':
                bot.send_message(chat_id=msg.from_user.id, text = f'сумма равна: {x+y}')

                # print(x+y)
            case '-':
                bot.send_message(chat_id=msg.from_user.id, text = f'разность равна: {x-y}')

                # print(x-y)
            case '*':
                bot.send_message(chat_id=msg.from_user.id, text = f'произведение равно: {x*y}')

                # print(x*y)
            case '/':
                if y != 0:
                    bot.send_message(chat_id=msg.from_user.id, text = f'результат равен: {x/y}')

                    # print(x/y)
                else:
                    bot.send_message(chat_id=msg.from_user.id, text = 'на ноль делить нельзя')

                    # print("на ноль делить нельзя")
    else:
        bot.send_message(chat_id=msg.from_user.id, text = 'не корректно введен знак')

        # print("не корректно введен знак")
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('калькулятор')
    btn2 = types.KeyboardButton('выход')
    markup.add(btn1, btn2)
    bot.send_message(chat_id=msg.from_user.id, text = 'Если хотите произвести расчет еще раз - нажмите "калькулятор", \nесли желаете выйти - нажмите кнопку "выход"', reply_markup=markup)



    # while msg.text == 'д':
    #     bot.send_message(chat_id=msg.from_user.id, text = 'введите через запятую: число 1, знак(+,-,/,*), число 2')

    #     bot.register_next_step_handler(msg, calculate)

    #     bot.send_message(chat_id=msg.from_user.id, text = 'Повторить? (д/н)')


        # if msg.text == 'д':
        #     choise = True
        # else:
        #     choise = False

        
        # question = input('Повторить? (д/н): ')

        # if question == 'д':
        #     choice = True
        # else:
        #     choice = False
        
    


    